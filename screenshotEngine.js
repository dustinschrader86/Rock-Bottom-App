// ===============================
// Rock Bottom Screenshot Engine
// Full Vision + JSON Analyzer
// ===============================

import fs from "fs";
import OpenAI from "openai";

// -------------------------------
// 1. Initialize OpenAI Client
// -------------------------------
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// -------------------------------
// 2. Convert image to Base64
// -------------------------------
function loadImageAsBase64(imagePath) {
  try {
    const fileData = fs.readFileSync(imagePath);
    return fileData.toString("base64");
  } catch (err) {
    console.error("❌ Error loading image:", err);
    return null;
  }
}

// -------------------------------
// 3. Screenshot Analyzer
// -------------------------------
export async function analyzeScreenshot(imagePath) {
  console.log("📸 Loading screenshot:", imagePath);

  const base64Image = loadImageAsBase64(imagePath);
  if (!base64Image) {
    return { error: "Failed to load image" };
  }

  console.log("🤖 Sending screenshot to AI…");

  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content:
          "You are a screenshot analysis engine. Always return structured JSON. No paragraphs. No commentary."
      },
      {
        role: "user",
        content: [
          {
            type: "input_text",
            text: "Analyze this screenshot and return ONLY JSON with: {description, detected_text, ui_elements, warnings}"
          },
          {
            type: "input_image",
            image_url: `data:image/png;base64,${base64Image}`
          }
        ]
      }
    ],
    max_tokens: 500
  });

  const raw = response.choices[0].message.content;

  console.log("📦 Raw AI Output:", raw);

  try {
    const parsed = JSON.parse(raw);
    return parsed;
  } catch (err) {
    console.error("⚠️ JSON parse error:", err);
    return { error: "AI returned non‑JSON output", raw };
  }
}

// -------------------------------
// 4. CLI Runner
// -------------------------------
if (process.argv[2]) {
  const imagePath = process.argv[2];

  analyzeScreenshot(imagePath).then((result) => {
    console.log("\n===============================");
    console.log(" FINAL ANALYSIS RESULT");
    console.log("===============================\n");
    console.log(result);
  });
} else {
  console.log("Usage: node screenshotEngine.js <imagefile>");
}


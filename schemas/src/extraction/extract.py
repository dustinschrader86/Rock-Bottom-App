import json
from datetime import datetime

def extract_screenshot_data(raw_text: str):
    return {
        "screenshot_id": "temp-id",
        "source": {
            "device": "unknown",
            "app": "unknown",
            "captured_at": datetime.utcnow().isoformat()
        },
        "extraction": {
            "raw_text": raw_text,
            "entities": {
                "wallet_addresses": [],
                "token_tickers": [],
                "contract_addresses": [],
                "urls": [],
                "usernames": []
            }
        },
        "on_chain_verification": {
            "network": "solana",
            "tokens": [],
            "wallets": []
        },
        "analysis": {
            "scam_signals": [],
            "risk_level": "unknown",
            "notes": ""
        },
        "tags": [],
        "created_at": datetime.utcnow().isoformat()
    }import re

def detect_entities(raw_text: str):
    return {
        "wallet_addresses": re.findall(r"[1-9A-HJ-NP-Za-km-z]{32,44}", raw_text),
        "token_tickers": re.findall(r"\b[A-Z]{2,6}\b", raw_text),
        "contract_addresses": re.findall(r"[1-9A-HJ-NP-Za-km-z]{32,44}", raw_text),
        "urls": re.findall(r"https?://\S+", raw_text),
        "usernames": re.findall(r"@[A-Za-z0-9_]+", raw_text)
    }

from solana_verify import get_account_info


from extract import extract_screenshot_data

sample_text = """
BUY 3 SOL at 173.22
Wallet: 9xKf2s8Yw3p1u2V7Qk5mZ1t4s9d8f3a2b1c0dEfGh
Visit https://jupiter.exchange
"""

result = extract_screenshot_data(sample_text)

print(result)


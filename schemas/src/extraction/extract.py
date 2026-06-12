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
    }


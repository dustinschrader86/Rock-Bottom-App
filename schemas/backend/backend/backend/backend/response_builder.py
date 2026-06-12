def build_response(ocr_text, entities, chain_results, patterns, metadata):
    return {
        "text_blocks": [
            {
                "text": block["text"],
                "confidence": block.get("confidence", None)
            }
            for block in ocr_text
        ],

        "entities": {
            "wallet_addresses": entities.get("wallet_addresses", []),
            "token_symbols": entities.get("token_symbols", []),
            "urls": entities.get("urls", []),
            "numbers": entities.get("numbers", []),
        },

        "wallets": [
            {
                "address": addr,
                "exists_on_chain": chain_results.get(addr, {}).get("exists", False),
                "balance": chain_results.get(addr, {}).get("balance", None),
                "owner": chain_results.get(addr, {}).get("owner", None),
            }
            for addr in entities.get("wallet_addresses", [])
        ],

        "tokens": [
            {
                "symbol": symbol,
                "exists_on_chain": chain_results.get(symbol, {}).get("exists", False),
                "decimals": chain_results.get(symbol, {}).get("decimals", None),
                "supply": chain_results.get(symbol, {}).get("supply", None),
            }
            for symbol in entities.get("token_symbols", [])
        ],

        "patterns_detected": patterns,

        "metadata": {
            "processing_time_ms": metadata.get("processing_time_ms"),
            "engine_version": metadata.get("engine_version", "1.0.0"),
            "screenshot_hash": metadata.get("screenshot_hash"),
        }
    }


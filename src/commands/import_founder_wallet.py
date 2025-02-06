# src/commands/import_founder_wallet.py
import json
import os
import base58
from solders.keypair import Keypair # type: ignore

def import_founder_wallet():
    if not os.path.exists("wallets/Founder_Wallet.json"):
        with open("wallets/Founder_Wallet.json", "w") as f:
            json.dump({}, f)

    private_key = input("Enter the private key for Founder Wallet: ").strip()

    try:
        # Декодируем base58 строку в байты
        decoded_key = base58.b58decode(private_key)
        keypair = Keypair.from_bytes(decoded_key)

        wallet_data = {
            "public_key": str(keypair.pubkey()),
            "private_key": private_key  # Сохраняем оригинальный base58 ключ
        }

        with open("wallets/Founder_Wallet.json", "w") as f:
            json.dump(wallet_data, f, indent=4)

        print("Founder Wallet imported successfully.")
    except Exception as e:
        print(f"Error importing Founder Wallet: {str(e)}")
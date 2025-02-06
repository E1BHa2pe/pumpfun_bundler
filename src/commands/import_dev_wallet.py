# src/commands/import_dev_wallet.py
import json
import os
import base58
from solders.keypair import Keypair # type: ignore

def import_dev_wallet():
    if not os.path.exists("wallets/Dev_Wallet.json"):
        with open("wallets/Dev_Wallet.json", "w") as f:
            json.dump({}, f)

    private_key = input("Enter the private key for Dev Wallet: ").strip()

    try:
        decoded_key = base58.b58decode(private_key)
        keypair = Keypair.from_bytes(decoded_key)

        wallet_data = {
            "public_key": str(keypair.pubkey()),
            "private_key": private_key
        }

        with open("wallets/Dev_Wallet.json", "w") as f:
            json.dump(wallet_data, f, indent=4)

        print("Dev Wallet imported successfully.")
    except Exception as e:
        print(f"Error importing Dev Wallet: {str(e)}")
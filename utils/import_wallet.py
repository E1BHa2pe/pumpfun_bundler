# src/utils/import_wallet.py
import json
import os
from solders.keypair import Keypair  # type: ignore

def import_wallet(file_path, wallet_name):
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump({}, f)

    # Запрашиваем приватный ключ у пользователя
    private_key = input(f"Enter the private key for {wallet_name}: ").strip()

    try:
        # Преобразуем приватный ключ в байты
        private_key_bytes = bytes(map(int, private_key.strip('[]').split(',')))
        
        # Проверяем длину приватного ключа
        if len(private_key_bytes) != 64:
            print("Invalid private key length. It must be 64 bytes.")
            return
        
        # Создаем Keypair из приватного ключа
        keypair = Keypair.from_bytes(private_key_bytes)
        
        # Сохраняем данные кошелька
        wallet_data = {
            "public_key": str(keypair.pubkey()),
            "private_key": list(keypair.secret())
        }
        with open(file_path, "w") as f:
            json.dump(wallet_data, f, indent=4)
        
        print(f"{wallet_name} imported successfully.")
        print(f"Public Key: {wallet_data['public_key']}")
    except Exception as e:
        print(f"Error importing {wallet_name}: {e}")
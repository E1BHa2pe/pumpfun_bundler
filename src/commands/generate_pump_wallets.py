# src/commands/generate_pump_wallets.py
import json
import os
import base58
from solders.keypair import Keypair # type: ignore

def generate_pump_wallets():
    # Проверяем, существует ли файл Pump_Wallets.json
    if not os.path.exists("wallets/Pump_Wallets.json"):
        with open("wallets/Pump_Wallets.json", "w") as f:
            json.dump([], f)

    # Загружаем существующие кошельки
    with open("wallets/Pump_Wallets.json", "r") as f:
        wallets = json.load(f)

    # Запрашиваем у пользователя количество кошельков для генерации
    try:
        count = int(input("Enter the number of Pump Wallets to generate: "))
        if count <= 0:
            print("Number of wallets must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Генерируем новые кошельки
    new_wallets = []
    for _ in range(count):
        keypair = Keypair()
        wallet = {
            "public_key": str(keypair.pubkey()),
            "private_key": base58.b58encode(bytes(keypair.secret())).decode("utf-8")  # Сохраняем в base58
        }
        new_wallets.append(wallet)

    # Добавляем новые кошельки к существующим
    wallets.extend(new_wallets)

    # Сохраняем обновленный список кошельков
    with open("wallets/Pump_Wallets.json", "w") as f:
        json.dump(wallets, f, indent=4)

    print(f"Successfully generated {count} new Pump Wallets.")
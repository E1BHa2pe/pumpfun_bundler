# src/wallet_manager.py
from commands.generate_pump_wallets import generate_pump_wallets
from commands.import_founder_wallet import import_founder_wallet
from commands.import_dev_wallet import import_dev_wallet
#for wallets
def wallet_manager_menu():
    while True:
        print("\nWallet Manager Menu:")
        print("1. Generate Pump Wallets")
        print("2. Import Founder Wallet")
        print("3. Import Dev Wallet")
        print("0. Back to Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            generate_pump_wallets()
        elif choice == "2":
            import_founder_wallet()
        elif choice == "3":
            import_dev_wallet()
        elif choice == "0":
            break
        else:
            print("Invalid option! Try again.")

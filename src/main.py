import os
import json
from colorama import Fore, Style, init
from tabulate import tabulate
from commands.generate_pump_wallets import generate_pump_wallets
from commands.import_founder_wallet import import_founder_wallet
from commands.import_dev_wallet import import_dev_wallet
from wallet_manager import wallet_manager_menu
import sys

# Добавляем корневую директорию проекта в sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)
# Инициализация colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Fore.RED + """
    ██████╗ ██╗   ██╗ ██████╗     ██████╗ ██╗   ██╗██╗     ██╗     
    ██╔══██╗██║   ██║██╔════╝     ██╔══██╗██║   ██║██║     ██║     
    ██████╔╝██║   ██║██║  ███╗    ██████╔╝██║   ██║██║     ██║     
    ██╔══██╗██║   ██║██║   ██║    ██╔═══╝ ██║   ██║██║     ██║     
    ██║  ██║╚██████╔╝╚██████╔╝    ██║     ╚██████╔╝███████╗███████╗
    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝
    """)
    print(Fore.CYAN + "Telegram: https://t.me/rug_pull_dev\n")

def get_wallet_info():
    # Заглушка - потом подключим реальные данные
    return {
        'pump_wallets_count': 0,
        'pump_balance': 0.0,
        'founder_connected': False,
        'founder_balance': 0.0,
        'founder_public': 'Not connected'
    }

def main_menu():
    while True:
        clear_screen()
        print_banner()
        
        # Получаем информацию о кошельках
        info = get_wallet_info()
        
        # Формируем таблицу с информацией
        info_table = [
            ["Pump Wallets Count", info['pump_wallets_count']],
            ["Pump Wallets Balance SOL", f"{info['pump_balance']:.4f}"],
            ["Founder Wallet Connected", "Yes" if info['founder_connected'] else "No"],
            ["Founder Wallet Balance SOL", f"{info['founder_balance']:.4f}"],
            ["Founder Wallet Public Key", info['founder_public']]
        ]
        
        print(Fore.YELLOW + "STATUS INFORMATION:")
        print(tabulate(info_table, tablefmt="fancy_grid"))
        print("\n")
        
        # Основное меню
        menu_items = [
            "1. Wallet Manager",
            "2. Transfer Sol from F.Wallet to Pump Wallets",
            "3. Transfer Sol Back",
            "4. Withdraw SOL",
            "5. SPAM Buy Token",
            "6. Sell All Tokens",
            "7. Settings",
            "0. Exit"
        ]
        
        print(Fore.GREEN + "MAIN MENU:")
        for item in menu_items:
            print(item)
            
        choice = input("\nSelect option: ")
        
        if choice == "1":
            wallet_manager_menu()
        elif choice == "0":
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid option! Try again.")

def settings_menu():
    while True:
        clear_screen()
        print(Fore.YELLOW + "SETTINGS\n")
        menu_items = [
            "1. Priority Fee",
            "2. Slippage",
            "3. Mode (Fast/Slow)",
            "4. Anti-MEV (On/Off)",
            "0. Back to Main Menu"
        ]
        
        for item in menu_items:
            print(item)
            
        choice = input("\nSelect option: ")
        
        if choice == "0":
            break
        # Добавить обработку других опций
        else:
            print(Fore.RED + "Invalid option!")

if __name__ == "__main__":
    # Создаем папку wallets если ее нет
    if not os.path.exists("wallets"):
        os.makedirs("wallets")
        
    # Создаем пустые файлы если их нет
    for file in ["Pump_Wallets.json", "Founder_Wallet.json", "Dev_Wallet.json"]:
        if not os.path.exists(f"wallets/{file}"):
            with open(f"wallets/{file}", "w") as f:
                json.dump([], f)
    
    main_menu()
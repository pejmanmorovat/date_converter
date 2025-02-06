from datetime import datetime
import jdatetime
from convertdate import islamic, persian, gregorian
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Display author name
print(Fore.CYAN + "\n╔════════════════════════════╗")
print(Fore.CYAN + "║    Date Converter Program  ║")
print(Fore.CYAN + "║    Author: Pejman Morovat  ║")
print(Fore.CYAN + "╚════════════════════════════╝")

def show_calendars():
    gregorian_date = datetime.now()
    persian_date = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
    islamic_date = islamic.from_gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day)
    
    print(Fore.WHITE + "\n╔════════════════════════════╗")
    print(Fore.WHITE + "║      CURRENT CALENDARS     ║")
    print(Fore.WHITE + "╚════════════════════════════╝")
    print(Fore.WHITE + f"\nToday: {persian_date.strftime('%A')}")
    print(Fore.WHITE + f"Persian Date: {persian_date.strftime('%Y/%m/%d')}")
    print(Fore.WHITE + f"Month: {persian_date.strftime('%B')}")
    print(Fore.WHITE + f"\nGregorian Date: {gregorian_date.strftime('%Y/%m/%d')}")
    print(Fore.WHITE + f"Month: {gregorian_date.strftime('%B')}")
    print(Fore.WHITE + f"\nIslamic Date: {islamic_date[0]}/{islamic_date[1]}/{islamic_date[2]}")
    print(Fore.WHITE + f"\nTime: {persian_date.strftime('%H:%M:%S')}")

def solar_to_gregorian(year, month, day):
    return gregorian.from_jd(persian.to_jd(year, month, day))

def gregorian_to_solar(year, month, day):
    return persian.from_jd(gregorian.to_jd(year, month, day))

def main():
    while True:
        print(Fore.CYAN + "\n╔════════════════════════════╗")
        print(Fore.CYAN + "║      DATE CONVERTER       ║")
        print(Fore.CYAN + "╚════════════════════════════╝")
        print(Fore.YELLOW + "\n1. Show Current Calendars")
        print(Fore.GREEN + "2. Convert Solar Hijri to Gregorian")
        print(Fore.BLUE + "3. Convert Gregorian to Solar Hijri")
        print(Fore.RED + "4. Exit")
        
        choice = input(Fore.CYAN + "\nEnter your choice (1-4): ")
        
        if choice == '1':
            show_calendars()
        elif choice == '2':
            year = int(input("\nEnter Solar Hijri year: "))
            month = int(input("Enter Solar Hijri month: "))
            day = int(input("Enter Solar Hijri day: "))
            g_date = solar_to_gregorian(year, month, day)
            print(Fore.GREEN + f"\nGregorian Date: {g_date[0]}-{g_date[1]:02d}-{g_date[2]:02d}")
        elif choice == '3':
            year = int(input("\nEnter Gregorian year: "))
            month = int(input("Enter Gregorian month: "))
            day = int(input("Enter Gregorian day: "))
            p_date = gregorian_to_solar(year, month, day)
            print(Fore.BLUE + f"\nSolar Hijri Date: {p_date[0]}-{p_date[1]:02d}-{p_date[2]:02d}")
        elif choice == '4':
            print(Fore.RED + "\nExiting program...")
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()

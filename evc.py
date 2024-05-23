
pin = "8899"

SalaamBank = 200
pinBank = "9090"

def show_balance():
    balance = 1000
    print("Your balace is:", balance)

def transfer_evc():
    number = input ("Enter the number to transfer : ")
    amount =float(input("Enter the amout to transfer "))
    if amount <=balance:
        balance -= amount
        print(f"Successfuly transferd ${amount} to {number} you Balance is ${balance}")
    else:
        print("ma kugu filno")


def salaam_bank():
        bank_pin = input("Enter Salaam Bank PIN: ")
        if bank_pin == pinBank:
            print("1. Check Salaam Bank Balance")
            print("2. Transfer to Salaam Bank")
            print("3. Transfer from Salaam Bank")
            bank_choice = input("Choose an option: ")

            if bank_choice == "1":
                print("Your Salaam Bank balance is:", SalaamBank)
            elif bank_choice == "2":
                amount = float(input("Enter the amount to transfer to Salaam Bank: "))
                if amount <= balance:
                    balance -= amount
                    SalaamBank += amount
                    print(f"Successfully transferred ${amount} to Salaam Bank. Your new balance is ${balance}. Salaam Bank balance is ${SalaamBank}.")
                else:
                    print("Insufficient balance.")
            elif bank_choice == "3":
                amount = float(input("Enter the amount to transfer from Salaam Bank: "))
                if amount <= SalaamBank:
                    SalaamBank -= amount
                    balance += amount
                    print(f"Successfully transferred ${amount} from Salaam Bank. Your new balance is ${balance}. Salaam Bank balance is ${SalaamBank}.")
                else:
                    print("Incorect Salaam Bank balance.")
            else:
                print("Invalid choice.")
        else:
            print("Incorrect Salaam Bank PIN.")

            

npin = input("Enter PIN: ")

if npin == pin:
    print("1. Itus Haraagaga (Show Balance)")
    print("2. Uwareeji EVC (Transfer EVC)")
    print("3. Salaam Bank")
    choice = input("Choose an option: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        transfer_evc()

        
    elif choice == "3":
         salaam_bank()

    else:
         print("Invalid choice.")
        
else:
    print("PIN Incorrect")

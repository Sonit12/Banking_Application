# Simple Banking Application

balance = 0

print("Welcome to Your World Bank")

name = input("Enter your name: ")

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited successfully.")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you,", name, "for using ABC Bank.")
        break

    else:
        print("Invalid choice. Please try again.")
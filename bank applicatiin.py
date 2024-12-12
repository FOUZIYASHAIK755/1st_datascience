class Bank:
    def __init__(self):
        self.bal = 1000  # Initial account balance
        self.max_withdrawals = 3
        self.withdraw_attempts = 0

    def deposit(self):
        upbal = int(input("Enter amount to be deposited: "))
        if 100 < upbal % 100 == 0 and upbal < 50000:
            self.bal += upbal
            print(f"Updated balance after depositing is: {self.bal}")
        else:
            print("Cannot deposit this amount.")

    def withdraw(self):
        if self.withdraw_attempts >= self.max_withdrawals:
            print("Maximum withdrawal attempts reached for today.")
            return False
        amount = int(input("Enter amount to be withdrawn: "))
        if (
            100 < amount <= 20000 and
            amount % 100 == 0 and
            self.bal - amount >= 500
        ):
            self.bal -= amount
            self.withdraw_attempts += 1
            print(f"Amount {amount} withdrawn successfully. Current balance: {self.bal}")
            return True
        else:
            print("Cannot withdraw this amount.")
            return False

    def balance_check(self):
        print(f"Your current account balance is: {self.bal}")

    def options(self):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Balance Check")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.balance_check()
            elif choice == 0:
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid option entered. Please try again.")

    def validate(self):
        chances = 3
        while chances > 0:
            pin = int(input("Enter your PIN: "))
            if pin == 1234:
                print("Access granted!")
                self.options()
                break
            else:
                chances -= 1
                print(f"Invalid PIN. You have {chances} chances left.")
        if chances == 0:
            print("You have entered the wrong PIN 3 times. Access denied.")

# Create a Bank object and start the program
obj = Bank()
obj.validate()

class Bank:
    def __init__(self):
        self.bal = 10000

    def deposit(self):
        upbal = int(input("Enter amount to be deposited: "))
        if upbal > 100 and upbal % 100 == 0 and upbal < 50000:
            self.bal += upbal
            print(f"Updated amount after depositing is: {self.bal}")
        else:
            print("Cannot deposit this amount")

    def withdraw(self, chances):
        amount = int(input("Enter amount to be withdrawn: "))
        if amount > 100 and amount % 100 == 0 and amount < self.bal and (self.bal - amount) >= 500 and amount < 20000:
            self.bal -= amount
            print(f"Amount {amount} withdrawn from your account. Your current balance is: {self.bal}")
            return True
        else:
            print("Cannot withdraw this amount")
            return False

    def options(self):
        chances = 0
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Check")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.deposit()
            elif choice == 2:
                if chances < 3:
                    if self.withdraw(chances):
                        chances += 1
                    else:
                        print("Maximum withdrawal attempts completed for today")
                else:
                    print("Maximum withdrawal attempts completed for today")
            elif choice == 3:
                print(f"Your current balance is: {self.bal}")
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid option entered.")

    def validate(self):
        chancesv = 3
        while chancesv > 0:
            pin = int(input("Enter your PIN: "))
            if pin == 1234:
                self.options()
                break
            else:
                chancesv -= 1
                print(f"Invalid PIN. You have {chancesv} chances left.")
        if chancesv == 0:
            print("You have entered the wrong PIN 3 times. Access denied.")

obj = Bank()
obj.validate()


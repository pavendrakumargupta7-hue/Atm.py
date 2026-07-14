class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        while True:
            user_input = input("""
Hi, how can I help you?
1. Press 1 to create PIN
2. Press 2 to change PIN
3. Press 3 to check balance
4. Press 4 to withdraw money
5. Press 5 to exit
""")

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw()
            elif user_input == '5':
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice. Try again.")

    def create_pin(self):
        self.pin = input("Enter new PIN: ")
        self.balance = int(input("Enter initial balance: "))
        print("PIN created successfully")

    def change_pin(self):
        old_pin = input("Enter old PIN: ")
        if old_pin == self.pin:
            self.pin = input("Enter new PIN: ")
            print("PIN changed successfully")
        else:
            print("Incorrect PIN")

    def check_balance(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Wrong PIN")


    def withdraw(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful")
                print("Remaining balance:", self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")


# Program start
if __name__ == "__main__":
    atm = Atm()
    atm.menu()

import random

class Customer:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.accounts = []

    def create_account(self, account_type, initial_balance):
        account_number = Bank.generate_account_number()
        account = BankAccount(account_type, initial_balance, self, account_number)
        self.accounts.append(account)
        return account

    def display_customer_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact Number: {self.contact_number}")
        print("Accounts:")
        for account in self.accounts:
            print(f" - {account}")


class BankAccount:
    def __init__(self, account_type, balance, owner, account_number):
        self.account_type = account_type
        self.balance = balance
        self.owner = owner
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited INR {amount}. New balance: INR {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew INR {amount}. New balance: INR {self.balance}")
        else:
            print("Insufficient funds!")

    def __str__(self):
        return f"{self.account_type} Account - Account Number: {self.account_number}, Balance: INR {self.balance}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    @staticmethod
    def generate_account_number():
        return ''.join(random.choice('0123456789') for _ in range(8))

    def display_bank_info(self):
        print(f"Bank Name: {self.name}")
        print("Customers:")
        for customer in self.customers:
            customer.display_customer_info()
            print()

    def find_account_by_number(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account.account_number == account_number:
                    return account
        return None


if __name__ == "__main__":
    my_bank = Bank("My Bank")
    customer_list = []

    while True:
        print("\n1. New Customer")
        print("2. Existing Customer")
        print("3. Show Bank Info")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                print("\nCustomer Registration:")
                name = input("Enter Customer Name: ")
                address = input("Enter Customer Address: ")
                contact_number = input("Enter Customer Contact Number: ")

                customer_obj = Customer(name, address, contact_number)
                customer_list.append(customer_obj)
                my_bank.add_customer(customer_obj)

                while True:
                    acc_type = int(input("\n1. Savings Account\n2. Current Account\n3. Exit\nChoose: "))

                    if acc_type == 1:
                        new_account = customer_obj.create_account("Savings", 1000)
                        print(f"Savings account created. Account Number: {new_account.account_number}")
                        break

                    elif acc_type == 2:
                        new_account = customer_obj.create_account("Current", 1000)
                        print(f"Current account created. Account Number: {new_account.account_number}")
                        break

                    elif acc_type == 3:
                        break

                    else:
                        print("Invalid option...Try again")

            elif choice == 2:
                account_number_input = input("Enter your account number: ")
                account_to_transact = my_bank.find_account_by_number(account_number_input)

                if account_to_transact:
                    print(f"\nWelcome, {account_to_transact.owner.name}!")
                    print(account_to_transact)

                    while True:
                        print("\n1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Exit")

                        option = int(input("Enter option: "))

                        if option == 1:
                            deposit_amount = int(input("Enter amount to deposit: INR "))
                            account_to_transact.deposit(deposit_amount)

                        elif option == 2:
                            withdrawal_amount = int(input("Enter amount to withdraw: INR "))
                            account_to_transact.withdraw(withdrawal_amount)

                        elif option == 3:
                            print("\nAccount Info:")
                            print(account_to_transact)

                        elif option == 4:
                            break

                        else:
                            print("Invalid Option")

                else:
                    print("Account not found.")

            elif choice == 3:
                my_bank.display_bank_info()

            elif choice == 4:
                print("Thank you for using the banking system!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
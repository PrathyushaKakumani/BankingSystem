import os

def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    data = account_number + ',' + name + ',' + str(balance) + '\n'
    with open('accounts.txt', 'a') as f:
        f.write(data)
    print("Account created successfully")

def display_accounts():
    with open('accounts.txt', 'r') as f:
        print(f.read())

def deposit():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    with open('accounts.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.startswith(account_number):
                parts = line.split(',')
                balance = float(parts[2]) + amount
                line = parts[0] + ',' + parts[1] + ',' + str(balance) + '\n'
            f.write(line)
        f.truncate()
    print("Deposit successful")

def withdraw():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    with open('accounts.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.startswith(account_number):
                parts = line.split(',')
                balance = float(parts[2])
                if balance >= amount:
                    balance -= amount
                    line = parts[0] + ',' + parts[1] + ',' + str(balance) + '\n'
                else:
                    print("Insufficient balance")
            f.write(line)
        f.truncate()
    print("Withdrawal successful")

def delete_account():
    account_number = input("Enter account number: ")
    with open('accounts.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if not line.startswith(account_number):
                f.write(line)
        f.truncate()
    print("Account deleted successfully")

def main():
    while True:
        print("1. Create account")
        print("2. Display accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete account")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_account()
        elif choice == 2:
            display_accounts()
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            delete_account()
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

#This is Bank Operations Program in Python

balance = 0.0
transactions = []

def deposite(amount):
    global balance
    balance += amount
    transactions.append(f'Deposited amount: {amount}')  
    print(f'{amount} Deposited succesfully!\n')

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficent Balance")
    else:
        balance -= amount 
        transactions.append(f'Withdraw amount: {amount}')
        print(f'{amount} withdraw succesfully\n')

def checkBalance():
    global balance
    print(f'Avalable Balance: {balance}\n')

def transactionHistory():
    global transactions
    if not transactions:
        print("-----Transaction History-----")
        print("No Transactions yet!...")
    else:
        print("-----Transaction History-----")
        for t in transactions:
            print('--',t)
        deposites = sum(1 for t in transactions if 'Deposited amount' in t)    
        withdrawls = sum(1 for t in transactions if 'Withdraw amount' in t)
        print(f'\nTotal Deposites: {deposites}')
        print(f'\nTotal Withdrawls: {withdrawls}')    
def menu():
    while True:
        print("===Welcome to Pyhon Bank====")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.View Transaction History")
        print("5.Exit")

        
        choice = int(input("Enter your Choice: "))

        if choice == 1:
            amount = float(input("Enter you amount: "))
            deposite(amount)
        elif choice == 2:
            amount = float(input("Enter you amount: "))
            withdraw(amount)
        elif choice == 3:
            checkBalance()
        elif choice == 4:
            transactionHistory()
        elif choice == 5:
            print("Thank you for using arun bank, Visit Agian!")
            break 
        else:
            print("Invalid Choice")
menu()


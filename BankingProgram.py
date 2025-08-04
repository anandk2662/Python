#python banking program
def show_balance(balance):
    print("**********************************")
    print(f"your balance is ${balance:.2f}")
    print("**********************************")

def deposit():
    print("**********************************")
    amount=float(input("Enter amount to deposit: "))
    print("**********************************")
    if amount<0:
        print("**********************************")
        print("That's not a valid amount.")
        print("**********************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("**********************************")
    amount =float(input("Enter amount to withdrawn: "))
    print("**********************************")

    if amount>balance:
        print("**********************************")
        print("Insufficient funds.")
        print("**********************************")
        return 0
    elif amount < 0:
        print("**********************************")
        print("amount must be positive.")
        print("**********************************")
        return 0
    else:
        return amount
    
def main():
    balance=0
    is_running = True

    while is_running:
        print("**********************************")
        print("Banking Program")
        print("**********************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice=input("Enter your choice(1-4):")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance+=deposit()
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("**********************************")
            print("Invalid choice, please try again.")
            print("**********************************")

    print("**********************************")
    print("Thank you for using the Banking Program!")
    print("**********************************")
main()
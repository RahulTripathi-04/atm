
correct_pin =1234
balance = 10000
p = int(input("Enter your PIN:\n"))

if p == correct_pin :
    print("\nWelcome!!")
    def atm_menu():
        print("select your option..")
        print("1. Check balance")
        print("2. Withdrawl ")
        print("3. Deposit")
        print("4. Exit")
    
    def CheckBalance():
        print(f"Your current balance is {balance}")

    def Withdrawl():
        global balance 
        amount = (float(input("Enter amount to withdraw :$ ")))
        if amount > balance :
            print("Insuffecient Balance")
        elif amount <= 0 :
            print("Invalid withdarwl amount ")
        else:
            balance -= amount
            print(f"${amount} Has been withdramn and your balance is ${balance}")  

    def Deposit():
        global balance
        amount = (float(input("Enter amount to withdraw :$ ")))
        if amount > 0:
            balance += amount
            print(f"${amount} has been deposited to your account , your current balance is ${balance}")
        else:
            print("Invalid deposit amount")    
    
    def Exit():
        print("Thank Your For using the atm\ngoodbye!")
        

    def atm_system():
        while True:
            atm_menu()
            c = int(input("Enter your choice(1-4):"))
            if c == 1:
                CheckBalance()
            elif c == 2 :
                Withdrawl()  
            elif c == 3:
                Deposit()
            elif c == 4:
                Exit()
            break                            
        else:
         print("Invalid choice, select valid option")


else:
    print("invalid try-again")

atm_system()    
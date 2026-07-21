balance = 10000
print("=== ATM SYSTEM ===")
print("1 Check Balance")
print("2 Deposit Money")
print("3 Withdraw Money")
print("4 Exit")

choice = int (input("Enter your choice: "))

if choice == 1:
    print("Your Balance is:",balance)
elif choice == 2 :
    amount = float(input ("Enter amount to deposit:"))
    if amount > 0:
        balance += amount 
        print ("Money Deposited Successfully !")
        print("New Balance:",balance )
    else :
        print ("Invalid Amount:")
elif choice == 3:
    amount = float (input("Enter amount to withdraw:"))
    if amount <=0:
        print("Invalid Amount!")
    elif amount > balance:
        print("Insufficient Balance !")
    else :
        balance -= amount
        print("Please collect your cash. ")
        print("Remaining Balance",balance)
elif choice == 4:
    print("Thankyou for using our ATM!")
else:
    print("Invalid choice")
           

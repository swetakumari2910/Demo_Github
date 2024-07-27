# ATM Machine Project In Python

print("welcome to BOI Bank \n\n Please Insert your card..")

password = 2324
balance = 12000

choice = 0

pin = int(input("Enter your four digit pin number: "))

if(pin == password):
   while(choice !=4): 
    print("\n\n___Menu___")
    print("1 == balance")
    print("2 == deposite")
    print("3 == withdraw")
    print("4 == cancel\n")

    choice = int(input("\nEnter your option: "))

    if(choice == 1):
        print("Balance = Rs", balance)

    elif(choice == 2):
        deposite = int(input("Enter your deposite: Rs "))
        balance += deposite
        print("\ndeposited amount: Rs", deposite)
        print("Total Balance = Rs", balance)

    elif(choice == 3):
        withdraw = int(input("Enter the amount to withdraw: Rs "))
        balance -= withdraw
        print("\nwithdraw amount: Rs", withdraw)
        print("total balance = Rs", balance)
    elif(choice == 4):
        print("\nSession Ended!!!")
else:
    print("Incorrect Pin Number!! Please try again...!")

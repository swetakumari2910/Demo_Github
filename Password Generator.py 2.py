import random
#password "!@#$%^&*(){}[]":;'|\>.<,?/"
#length_password = int(input("Enter the length of the password"))
#a = "".join(random.sample(password,length_password))
#print(f"Your password is {a}")

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol ='()[]{};_#*._' 
number ='0123456789'

all = lower + upper + number + symbol
length = 10
password = "".join(random.sample(all,length))
print("The Generated Password is: ", password)
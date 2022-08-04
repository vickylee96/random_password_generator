from operator import truediv
import random

print("====================================================")
print("Welcome to Lerato's random password generator")
print("=====================================================")
amt = int(input("How many passwords would you like to generate? "))
chars =",./';[]-"
number = "0123456789"
upper_cases ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_cases =upper_cases.lower()
password =""
passText = open('password.text','w')


lower_letters = True
upper_Letters= True
numbers= True
symbols  = True

if upper_Letters:
    password += upper_cases
if lower_letters:
    password += lower_cases
if numbers:
    password += number
if symbols :
    password += chars

for i in range(amt):
    new_password = "".join(random.sample(password,8))  
    passText.write(new_password+"\n")
    print(new_password)


passText.close()    
  
    
       
     

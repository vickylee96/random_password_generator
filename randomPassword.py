from operator import truediv
import random


chars =",./';[]-"
number = "0123456789"
upper_cases ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_cases =upper_cases.lower()
password =""

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


new_password = "".join(random.sample(password,8))     
print(new_password)         

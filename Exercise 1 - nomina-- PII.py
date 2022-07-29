Legal = [1000000]

Health = [0.04]
Pension = [0.04]

CC = (int(input("Write your ID number")))

while name.isalpha() != True:
    print("What is your name? ")
    name = input()

    print("What is your lastname?")
last = input()
while last.isalpha() != True:

    print("what is your salary? ")
salary = int(input())
while salary.isalpha() != True:

    print("How many days did you work?")
WD = int(input())

if salary == 1000000:
    Salt = 117172
    print(f"Your transportation benefit is : {Salt}")
else:
    print("Your do not have transportation benefit")

SXD = (salary*WD)/30
print(f"Your total salary for days worked:{SXD}")
BXH = (SXD*0.04)
print(f"Your benefit health is :{BXH}")
BXP = (SXD*0.04)
print(f"Your benefit pension is :{BXP}")
print(f"Your total for benefits is: {BXH+BXP}")





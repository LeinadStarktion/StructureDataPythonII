Legal = [1000000]
Nomina = True
Health = [0.04]
Pension = [0.04]
CC = (int(input("Write your ID number")))


print("What is your name? ")
name = input()
 
print("What is your lastname?")
last = input()

print("What is your position?")
position = input()

print("What is your work type ?")
Type = input()
print("what is your salary? ")
salary = int(input())

print("How many days did you work?")
WD = int(input())

if salary == 1000000:
    Salt = 117172
    print(f"Your transportation benefit is : {Salt}")
else:
    print("Your do not have transportation benefit")

print ("")    
print ("----------------------------------------------------")
print ("|                                                  |")
print (f"Name : {name}")
print (f"Latname : {last}")
print (f"Id number : {CC}")
print (f"Position :{position}")
SXD = (salary*WD)/30
print(f"Your total salary for days worked :{SXD}")
BXH = (SXD*0.04)
print(f"Your benefit health is :{BXH}")
BXP = (SXD*0.04)
PORCFOURTY = (salary*0.4)
print (f"Your porcentual of quotation is : {PORCFOURTY}")
print(f"Your benefit pension is : $ {BXP}")
BXHP = BXH+BXP
print (f"Your total benefits is : {BXHP}")
TOTAL = salary-BXHP
print (f"Your total salary is : $ {TOTAL}")
print ("")
print ("----------------------------------------------------")
print ("|                                                  |")
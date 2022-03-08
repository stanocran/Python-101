import string


accNo=int
firstname =string
lastname=string
deposit =int
acctype=string

print("************************************************************")
print("========== WELCOME TO MY BANK ==========")
print("************************************************************")
print("========== A. Open New Client Account ============")
print("========== B. Check Account Type ============")
print("========== C. Check Account Balance ============")
print("========== X. Quit ============")
print("************************************************************")
EnterLetter = input("Select a Letter from the Above Box menu : ")
if EnterLetter =="A":
 print(" Openning New Account")
elif EnterLetter =="a":
    print(" Openning New Account")
else : 
    print("Select valid option")

if EnterLetter=="A":
    firstname = input("Enter first name ")
    lastname= input("Enter last name ")
    acctype=input("Enter Account Type:Current or Savings C/S ")
if acctype=="C":
    acctype="Current Account"
elif acctype=="c":
    acctype="Current Account"
elif acctype=="S":
    acctype="Savings Account"
elif acctype=="s":
    acctype="Savings Account"        
print("Account Number should follow format::111222333xxx ")
accNo=input("Enter Account Number ")
print("Name: ",firstname,lastname)
print ("Account Number: ",accNo)
print("Account Type: ",acctype)
if EnterLetter=="a":
    firstname = input("Enter first name ")
    lastname= input("Enter last name ")
    acctype=input("Enter Account Type:Current or Savings C/S ")
if acctype=="C":
    acctype="Current Account"
elif acctype=="c":
    acctype="Current Account"
elif acctype=="S":
    acctype="Savings Account"
elif acctype=="s":
    acctype="Savings Account"
print("Account Number should follow format::111222333xxx ")
accNo=input("Enter Account Number ")
print("Name: ",firstname,lastname)
print ("Account Number: ",accNo)
print("Account Type: ",acctype)

if EnterLetter =="B":
 print("Checking Account Type")
elif EnterLetter =="a":
    print("Checking Account Type")
else : 
    print("Select valid option")
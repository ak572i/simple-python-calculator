print("Basic Calculator")
def addition(n1,n2):
  print("The answer is " + str(n1+n2))
def substraction(n1,n2):
  print("The answer is " + str(n1-n2))
def multiplication(n1,n2):
  print("The answer is " + str(n1*n2))
def division(n1,n2):
  if n2 != 0:
    print("The answer is " + str(n1*n2))
  else:
    print("Cannot divide by 0!")
def modulus(n1,n2):
  if n2 != 0:
    print("The answer is " + str(n1%n2))
  else:
    print("Cannot modulus by 0!")
def calc():
  print("Enter 1 for Addition")
  print("Enter 2 for Substraction")
  print("Enter 3 for Multiplication")
  print("Enter 4 for Division")
  print("Enter 5 for Modulus")
  print(" ")
  sel = int(input("Enter here: "))
  if sel in range(1,6):
    nu1 = int(input("Enter first number here: "))
    nu2 = int(input("Enter second number here: "))
    if sel == 1:
      addition(nu1,nu2)
    elif sel == 2:
      substraction(nu1,nu2)
    elif sel == 3:
      multiplication(nu1,nu2)
    elif sel == 4:
      division(nu1,nu2)
    elif sel == 5:
      modulus(nu1,nu2)
  else:
    print("Invalid Number!")
while True:
  calc()
  con = input("Continue? (y/n): ")
  if con == "n":
    print("Goodbye!")
    break
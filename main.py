print("Basic Calculator")
numb1 = 0
numb2 = 0
def add(n1,n2):
    print(f"{n1} + {n2} = {n1+n2}")
def sub(n1,n2):
    print(f"{n1} - {n2} = {n1-n2}")
def mult(n1,n2):
    print(f"{n1} * {n2} = {n1*n2}")
def div(n1,n2):
    print(f"{n1} + {n2} = {n1/n2}")
def clerror(test):
    while True:
        try:
            clean = int(input(test))
            return clean
        except ValueError:
            print("Enter a Number!")
def calc():
    global numb1
    global numb2
    print("Enter 1 for Addition.\nEnter 2 for Substraction\nEnter 3 for Multiplication\nEnter 4 for Division.")
    while True:
        try:
            choice = int(input("Enter Choice here: "))
            if choice not in [1,2,3,4]:
                continue
            break
        except ValueError:
            print("Enter a Number!")
            continue
    numb1 = clerror("Enter First number here! ")
    numb2 = clerror("Enter second number here! ")
    if choice == 1:
        add(numb1,numb2)
    if choice == 2:
        sub(numb1,numb2)
    if choice == 3:
        mult(numb1,numb2)
    if choice == 4:
        div(numb1,numb2)
while True:
    calc()
    cont = input("Continue? (y/n)")
    while True:
        if cont not in ["y","n"]:
            print("Enter either (y/n).")
            cont == input("Continue? (y/n)")
        elif cont in ["y","n"]:
            break
    if cont == "y":
        continue
    if cont == "n":
        print("Goodbye!")
        break
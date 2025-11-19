from random import choice

history=[]
def add(x , y):
    return x + y
def subtract(x , y):
    return x - y
def multiply(x , y):
    return x * y
def divide(x, y):
    if y == 0:
        print("invalid output, divided by 0")
    else:
        return x / y
def get_number(prompt):
    while True:
        try :
            return float(input(prompt))
        except ValueError:
            print("invalid number try again")
while True:
    print("select operation")
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    while True:
        try:
            choice = int(input("Enter choice(1/2/3/4)"))
            if choice in (1, 2, 3, 4):
                break
            else:
                print("invalid choice, enter between 1 and 4")
        except ValueError:
            print("invalid input, please enter a number")
    x=get_number("enter the value of x")
    y=get_number("enter the value of y")
    if choice==1:
        print(add(x , y))
    elif choice==2:
        print(subtract(x , y))
    elif choice==3:
        print(multiply(x , y))
    elif choice==4:
        print(divide(x , y))
    else:
        print("invalid input")
    result = None
    if choice ==1:
        result=add(x,y)
    elif choice ==2:
        result=subtract(x,y)
    elif choice ==3:
        result =multiply(x,y)
    elif choice ==4:
        result =divide(x,y)
    print ("result", result)
    if result is not None:
        history.append(f"{x} {['+','-','*','/'][choice-1]} {y} = {result}")
    for h in history:
        print(h)
    cont = str(input("continue? y/n"))
    if cont=="y" or cont=="Y":
        continue
    else:
        break

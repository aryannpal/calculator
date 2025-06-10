# import art
# print(art.logo)
def add(n1, n2):
    return n1 + n2

def  sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations={"+": add ,
            "-": sub ,
            "*": multiply ,
            "/": divide}

def calculation():
    num1 = float(input("Enter your's First Number\t"))
    condition=True
    while condition:
        print("+\n-\n*\n/")
        operator = input("Pick a Operator\t")
        num2 = float(input("Enter your's Second Number\t"))
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} : {result}")
        continue_or_not = input(f"Type 'y' for continue with the Result {result}\n or Type 'n' to start a new calculation\t")
        if continue_or_not=='n':
            condition =False
            print("\n"*30)
            calculation()
        else:
            num1=result

calculation()






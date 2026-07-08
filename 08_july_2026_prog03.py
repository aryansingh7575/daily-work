# simple calculator
a=int(input("enter number: "))
b=int(input("enter number: "))

c = input("Enter Operator: ")

match c:
    case "+":
        print("Addition is", a+b)

    case "-":
        print("substraction is", a-b)
    
    case "*":
        print("division is", a/b)
    
    case "/":
        print("multipication is", a*b)
    
    case "%":            
        print("mod is", a%b)
    
    case _:
        print("Enter Valid Input.")
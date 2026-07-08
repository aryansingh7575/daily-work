# simple calculator
a=int(input("enter number: "))
b=int(input("enter number: "))

c = input("Enter Operator: ")

if c == "+":
    print("addition is", a+b)

elif c == "-":
    print("subtraction is", a-b)

elif c == "*":
    print("multipication is", a*b)

elif c == "/":
    print("divion is", a/b)

else:
    print("Enter Valid Operator.")            

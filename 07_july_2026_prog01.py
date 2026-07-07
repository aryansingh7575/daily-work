# print first 10 numbers of fibonacci series
num1=0
num2=1
print(num1,num2)
for i in range(1,11):
    num3=num1+num2
    print (num3)

    num1=num2
    num2=num3

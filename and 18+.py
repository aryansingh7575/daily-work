# eligible for voting & senior citizen
print("enter your age")
a=int(input())
if a < 18:
    print("not eligible for vote")
elif a > 18 and a < 60:
    print("eligible for vote")
else:
    print("eligible for vote, senior citizen")    

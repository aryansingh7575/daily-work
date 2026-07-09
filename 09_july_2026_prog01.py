#Star Right Angle Pattern
for i in range(0,6):
        print("*\t" * i)

rows = 5
for i in range(1,rows+1):
    for j in range(i):
        print("*\t", end=" ")
    print("\n")

for i in range (6, 0, -1):
    print("*\t" * i)

rows = 5
for i in range (rows,1,-1):
    for j in range(i):
        print("*\t", end=" ") 
    print("\n")    
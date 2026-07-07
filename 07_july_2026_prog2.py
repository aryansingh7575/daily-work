# check if user number is prime

a = int(input())

is_prime = True

for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break

if a > 1 and is_prime:
    print("prime")
else:
    print("not prime")
# Task 1:
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
    
# Task 2:
total = 0

for i in range(1, 51):
    total += i

print("The sum of integers from 1 to 50 is:", total)

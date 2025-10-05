n = int(input("Enter a number: "))

print(f"Even numbers from 1 to {n}:")
for i in range(2, n + 1, 2):
    print(i, end=" ")

a = float(input("Enter the number of units consumed: "))
b = 50

if a <= 100:
    rate = 5
elif a <= 200:
    rate = 7
else:
    rate = 10

c = rate * a

print("-" * 10, "Electricity Bill", "-" * 10)
print(f"Units Consumed: {round(a, 2)}")
print(f"Energy Charge: ₹{round(c, 2)}")
print(f"Fixed Charge: ₹{round(b, 2)}")
print("-" * 39)
print(f"Total Bill: ₹{c + b}")
print("Thanks for using our service...")

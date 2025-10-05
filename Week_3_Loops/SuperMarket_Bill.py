# Welcome_msg
print("Welcome to the Supermarket Billing System!\n")

# inputs
a = float(input("How many kg of Apples: "))
b = float(input("How many dozen of Bananas: "))
c = float(input("How many liter of Milk: "))

# Initialize totals
total_cost = 0
apple_total = 0
milk_total = 0
banana_total = 0

# subtotal

apple_total = a*120
milk_total = c*50
banana_total = b*60

# total
total = (apple_total+milk_total+banana_total)

# discount
if total >= 500:
    discount = total * 0.05
else:
    discount = 0

# Invoice
print("-"*45)
print(f"You have purchased {a} kg of Apple")
print(f"You have purchased {b} dozen of Banana")
print(f"You have purchased {c} liter of Milk")
print("-"*45)
print(f"Apple total is ₹{apple_total}")
print(f"Banana total is ₹{banana_total}")
print(f"Milk total is ₹{milk_total}")
print("-"*45)
print(f"Your total before discount ₹{total}")
print(f"Your final payable amount is ₹{total-discount}")

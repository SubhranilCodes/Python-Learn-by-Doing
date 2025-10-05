print("Welcome to the Cinema Ticket Billing System!\n")

# Number of tickets
num_tickets = int(input("How many tickets do you want to buy? "))

# Initialize totals
total_cost = 0
children_total = 0
adult_total = 0
senior_total = 0

# Loop for each ticket
for i in range(num_tickets):
    age = int(input(f"Enter the age of person {i+1}: "))

    if age <= 12:
        price = 100
        children_total += price
    elif age <= 59:
        price = 200
        adult_total += price
    else:
        price = 150
        senior_total += price  # senior_total = senior_total + price

    total_cost += price

# Apply discount if applicable
if num_tickets >= 5:
    discount = total_cost * 0.10
else:
    discount = 0

final_total = total_cost - discount

# Print bill
print("\n" + "-"*40)
print("Cinema Ticket Bill")
print("-"*40)
print(f"Children tickets total: ₹{children_total}")
print(f"Adult tickets total: ₹{adult_total}")
print(f"Senior tickets total: ₹{senior_total}")
print("-"*40)
print(f"Total before discount: ₹{total_cost}")
print(f"Discount applied: ₹{discount}")
print(f"Final amount to pay: ₹{final_total}")
print("-"*40)
print("Thank you for visiting the cinema!")

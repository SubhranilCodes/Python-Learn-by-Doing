apple = float(input("How many KG Apples you bought: "))
milk = float(input("How many Litters Milk you bought: "))
bananas = float(input("How many Dozen Bananas you bought: "))

appleprice = 120
milkprice = 50
bananaprice = 60

apb = apple * appleprice
mpb = milk * milkprice
bpb = bananas * bananaprice

print("_"*35)
print(f"Apples: {apple} kg × ₹{appleprice} = ₹{apb}")
print(f"Milk: {milk} lt × ₹{milkprice} = ₹{mpb}")
print(f"Bananas: {bananas} dozen × ₹{bananaprice} = ₹{bpb}")

total = apb+mpb+bpb
print("_"*35)
print(f'Total = ₹ {total}')

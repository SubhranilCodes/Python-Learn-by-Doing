principle = float(input("How much money you want to borowed: "))
rate = float(input("What is the rate of interest (%): "))
time = float(input("How may year you need the money for: "))

si = (principle*rate*time)/100

print(f"Your Principle ammount was: {principle}")
print(f"Rate: {rate}%")
print(f"Time: {time}")
print(f"Simple Interest: {si}")
print(f"Your Total payable ammount will be {principle+si}")

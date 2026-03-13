print("Mobile Recharge Plan Suggestion")
amount =int(input("Enter your recharge amount: "))
if amount>= 349:
    print("You can choose ₹349 Plan (Unlimited calls + Data)")
elif amount>= 299:
    print("You can choose ₹299 Plan (1.5GB/day)")
elif amount>= 199:
    print("You can choose ₹199 Plan (1GB/day)")
else:
    print("Please enter a higher recharge amount")

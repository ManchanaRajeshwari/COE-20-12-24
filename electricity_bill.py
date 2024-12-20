def calculate_bill(units):
    if units<=100:
        rate=1.5
    elif units<=200:
        rate=2.5
    else:
        rate=3.5
    return units*rate
units=float(input("Enter electricity units consumed:"))
print(f"Total electricity bill is ₹ {calculate_bill(units):.2f}")
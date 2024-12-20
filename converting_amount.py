def convert_amount(amount):
    usd_inr=83.0
    usd_eur=0.92
    usd_gbp=0.79
    return amount*usd_inr,amount*usd_eur,amount*usd_gbp
amount=float(input("Enter amount"))
inr,eur,gbp=convert_amount(amount)
print(f"Amount in INR {inr},Amount in EUR {eur},Amount in GBP {gbp}")
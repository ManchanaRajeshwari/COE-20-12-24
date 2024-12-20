def calculate_total(cart):
  total=0
  if not  cart.items():
      return "empty"
  for  cart_item in cart.values():
    if cart_item>25000:
        total+=cart_item
        if 20000>total<50000:
             total*=(1-0.1)
             return total
        elif total>50000:
            total*=(1-0.15)
            return total
cart={'Laptop':50000,'Headphones':2000,'Mouse':35000,'Keyboard':1500,'Monitor':8000,'USB Drive':1000}
print(f"Cart items:{cart}")
print(f"Total price:{calculate_total(cart)}")
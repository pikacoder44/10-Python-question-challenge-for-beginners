# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def discount_calc(price,discount):
    
    discounted_price = (discount/100)*price

    final_price = price-discounted_price
    return final_price

price = int(input("Enter the price: "))
disc = int(input("Enter the discount: "))

print(f"After applying {disc}% to {price}, The final price is: ${discount_calc(price,disc)}")
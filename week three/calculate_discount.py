# Create a function that calculates discount and calculate the final price

def calculate_discount(price, discount_percentage):

    price = float(input('Input the price of item: '))
    discount_percentage = float(input('Input discount percentage: ') / 100)
    final_price = price - (price * discount_percentage)

    if discount_percentage >= 20%:
        return final_price
    else:
        return price


def calculate_total_price(price, quantity, tax_rate):
    """
    Calculates the total price of an item based on the given price, quantity, and tax rate.
    """
    """
    Args:
    price (float): The price of the item.
    quantity (int): The quantity of the item.
    tax_rate (float): The tax rate as a decimal value.
    
    Returns:
    float: The total price of the item including tax.
    """
    tax_amount = price * quantity * tax_rate
    total_price = price * quantity + tax_amount
    return total_price

def greet(name):
    """
    Greets the given name.
    """
    print(f"Hello, {name}!")

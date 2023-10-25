#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        discount = 0.9 if item.price > 100 else 0.95
        if item.quantity > 0:
            total += item.price * discount
    return total

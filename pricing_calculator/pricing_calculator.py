def calculate_depop_price(retail_price, condition, shipping_cost):
    # Define markup percentages based on condition
    condition_markup = {
        'New with tags': 0.7,
        'Gently used': 0.5,
        'Vintage/Unique': 0.6,
        'Worn': 0.3
    }
    
    markup = condition_markup.get(condition, 0.5)
    suggested_price = retail_price * markup
    total_price = suggested_price + shipping_cost
    
    return round(suggested_price, 2), round(total_price, 2)

# Example usage:
retail = float(input("Enter retail price: "))
condition = input("Enter condition (New with tags/Gently used/Vintage/Unique/Worn): ")
shipping = float(input("Enter shipping cost: "))
suggested, total = calculate_depop_price(retail, condition, shipping)
print(f"Suggested Depop Price: ${suggested}")
print(f"Total Price to List (including shipping): ${total}")

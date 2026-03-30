def calculate_discount(price, discount_rate):
    """
    Calculate discount amount based on price and discount rate.
    Raises ValueError if inputs are invalid.
    """
    # Validate price
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a numeric value")
    if price < 0:
        raise ValueError("Price must be non-negative")
    
    # Validate discount rate
    if not isinstance(discount_rate, (int, float)):
        raise ValueError("Discount rate must be a numeric value")
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Discount rate must be between 0 and 1")
    
    # Calculate discount amount
    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):
    """
    Apply discount amount to original price and return new price.
    Raises ValueError if discount would make price negative.
    """
    # Validate price
    if not isinstance(price, (int, float)):
        raise ValueError("Price must be a numeric value")
    if price < 0:
        raise ValueError("Price must be non-negative")
    
    # Validate discount amount
    if not isinstance(discount_amount, (int, float)):
        raise ValueError("Discount amount must be a numeric value")
    if discount_amount < 0:
        raise ValueError("Discount amount must be non-negative")
    if discount_amount > price:
        raise ValueError("Discount amount cannot exceed original price")
    
    # Apply discount and return new price
    new_price = price - discount_amount
    return new_price


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": 500, "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        try:
            price = product["price"]
            discount_rate = product["discount_rate"]
            
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()
        except ValueError as e:
            print(f"ERROR processing {product['name']}: {e}")
            print("Please check the product data and try again.")
            print()
        except TypeError as e:
            print(f"TYPE ERROR processing {product['name']}: {e}")
            print("Invalid data type detected. Please ensure price and discount rate are numbers.")
            print()
        except Exception as e:
            print(f"UNEXPECTED ERROR processing {product['name']}: {e}")
            print()

# Program entry point
if __name__ == "__main__":
    main()

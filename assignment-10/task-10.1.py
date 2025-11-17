def discount(price, category):
    DISCOUNT_RULES = {
        # category: (price_threshold, high_discount_rate, low_discount_rate)
        "student": (1000, 0.10, 0.05),
        "default": (2000, 0.15, 0.00),
    }

    rules = DISCOUNT_RULES.get(category, DISCOUNT_RULES["default"])
    threshold, high_discount, low_discount = rules

    if price > threshold:
        discount_rate = high_discount
    else:
        discount_rate = low_discount

    return price * (1 - discount_rate)


# Main block to test the function with different data
if __name__ == "__main__":
    test_cases = [
        {"price": 500, "category": "student", "case": "Student, low price"},
        {"price": 1200, "category": "student", "case": "Student, high price"},
        {"price": 1500, "category": "regular", "case": "Regular, low price"},
        {"price": 2500, "category": "regular", "case": "Regular, high price"},
        {"price": 3000, "category": "vip", "case": "VIP (default), high price"},
    ]

    print("--- Testing Discount Function ---")
    for test in test_cases:
        original_price = test["price"]
        category = test["category"]
        discounted_price = discount(original_price, category)
        print(
            f'{test["case"]}: Original: ${original_price}, Category: {category}, Final: ${discounted_price:.2f}'
        )

def calculate_bill(prices, items_bought):
    total = 0
    for item in items_bought:
        if item in prices:
            total += prices[item]
    return total


prices = {"apple": 0.5, "banana": 0.3, "orange": 0.7}

print(calculate_bill(prices, ["apple", "banana"]))
print(calculate_bill(prices, ["apple", "apple", "orange"]))
print(calculate_bill(prices, ["banana", "grape"]))
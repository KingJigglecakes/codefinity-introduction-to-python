prices = [29.99, 45.50, 12.75, 38.20]

discount_factor = [0.10, 0.20, 0.15, 0.05]

for index in range(len(prices)):
    prices[index] -= prices[index] * discount_factor[index]
    print(f"Updated price for item {index + 1}: ${prices[index]:.2f}")

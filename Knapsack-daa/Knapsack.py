def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Calculate value per unit weight for each item
    value_per_weight = [(values[i] / weights[i], values[i], weights[i], i) for i in range(n)]
    
    # Sort items based on value per unit weight in descending order
    value_per_weight.sort(reverse=True)
    
    total_value = 0  # Total value in the knapsack
    knapsack = [0] * n  # Fraction of each item in the knapsack
    
    for i in range(n):
        if capacity == 0:
            break
        
        ratio, value, weight, index = value_per_weight[i]
        
        # Take the whole item if it fits in the knapsack
        if weight <= capacity:
            knapsack[index] = 1
            total_value += value
            capacity -= weight
        else:
            # Take a fraction of the item to fill the knapsack
            fraction = capacity / weight
            knapsack[index] = fraction
            total_value += fraction * value
            capacity = 0

    return total_value, knapsack


# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, knapsack_items = fractional_knapsack(values, weights, capacity)

print("Maximum value in Knapsack =", max_value)
print("Fraction of each item in the Knapsack =", knapsack_items)

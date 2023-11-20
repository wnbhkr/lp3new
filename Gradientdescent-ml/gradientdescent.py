# Define the function y = (x + 3)^2
def objective_function(x):
    return (x + 3) ** 2


# Define the gradient of the function
def gradient(x):
    return 2 * (x + 3)


# Gradient Descent parameters
learning_rate = 0.1  # Adjust the learning rate as needed
num_iterations = 100  # You can adjust the number of iterations

# Initial starting point
x = 2

# Gradient Descent optimization
for i in range(num_iterations):
    # Compute the gradient at the current point
    grad = gradient(x)

    # Update x using the gradient and learning rate
    x = x - learning_rate * grad

    # Print the current iteration and x value
    print(f"Iteration {i + 1}: x = {x}, y = {objective_function(x)}")

# Print the final result
print("\nLocal minimum:")
print(f"x = {x}, y = {objective_function(x)}")





#orrrrr


# Gradient Descent function
def gradient_descent(initial_x, learning_rate, num_iterations):
    x = initial_x

    # Define the function y = (x + 3)^2
    def function_to_minimize(x):
        return (x + 3)**2

    # Derivative of the function y = (x + 3)^2
    def derivative(x):
        return 2 * (x + 3)

    # Perform gradient descent iterations
    for _ in range(num_iterations):
        gradient = derivative(x)
        x = x - learning_rate * gradient

    return x, function_to_minimize(x)

# Example usage:
initial_x = 2.0
learning_rate = 0.1
num_iterations = 100

local_minima_x, minima_value = gradient_descent(initial_x, learning_rate, num_iterations)

print(f"Local Minima at x = {local_minima_x}")
print(f"Minimum value of the function: {minima_value}")

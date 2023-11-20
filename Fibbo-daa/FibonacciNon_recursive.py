def iterative_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


# Example usage:
n = 37  # Change this to calculate Fibonacci for a different value of n
result = iterative_fibonacci(n)
print(f"The {n}-th Fibonacci number is {result}")




# Time Complexity Analysis:
# Non-Recursive (Iterative):

# Time Complexity: O(n)
# The iterative solution has a linear time complexity since it iterates through the range from 2 to n once.
# Recursive:

# Time Complexity: O(2^n)
# The recursive solution has an exponential time complexity. This is because it makes two recursive calls for each Fibonacci number, leading to repeated calculations and an exponential increase in function calls.
# Space Complexity Analysis:
# Non-Recursive (Iterative):

# Space Complexity: O(1)
# The iterative solution has a constant space complexity. It only uses two variables (a and b) regardless of the input size.
# Recursive:

# Space Complexity: O(n) (considering the function call stack)
# The recursive solution has a linear space complexity proportional to the depth of the recursion, which is equal to the input value n.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)
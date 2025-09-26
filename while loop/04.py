n = int(input("Enter n (0 ≤ n ≤ 20): "))

def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

if 0 <= n <= 20:
    print(f"{n}! = {factorial(n)}")
else:
    print("Error: n must be between 0 and 20")
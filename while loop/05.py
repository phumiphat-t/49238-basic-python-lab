def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:   
        if n % i == 0:
            return False
        i += 1
    return True

while True:
    n = int(input())
    if n == 0:
        break
    if is_prime(n):
        print(f"{n}: prime")
    else:
        print(f"{n}: not prime")
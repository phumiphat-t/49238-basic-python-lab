n = int(input("Enter your number"))
limit = int(input("Enter limit"))

def show_table(n, limit):
    i = 1
    while i <= limit:
        print(f"{n} x {i} = {n * i}")
        i += 1

show_table(n, limit)
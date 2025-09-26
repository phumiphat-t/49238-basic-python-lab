import random

secret = random.randint(1, 20)

count = 0

while True:
    num = int(input("ทายเลข (1-20): "))
    count += 1

    if num < secret:
        print("น้อยไป")
    elif num > secret:
        print("มากไป")
    else:
        print(f"ถูกต้อง! คุณทายทั้งหมด {count} ครั้ง")
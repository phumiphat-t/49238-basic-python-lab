n = int(input("n= "))
if n <= 0:
    print("จำนวน n < 0")
else:
    number = []
    for i in range(n):
        num = int(input(f"กรอกตัวเลขตัวที่ {i+1}: "))
        number.append(num)

    total = max(number)
    total2 = min(number)
    print(total)
    print(total2)
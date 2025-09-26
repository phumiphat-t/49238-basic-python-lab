n = int(input("n = "))
a = []
for i in range (n):
    num = int(input(f"ป้อนค่าที่ {i+1}: "))
    if (10< num < 50):
        a.append(num)
print(a)
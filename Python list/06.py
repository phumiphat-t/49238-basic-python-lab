n = int(input("n= "))
count = 0
for i in range (n):
    num = int(input(f"ป้อนค่าที่ {i+1}: "))
    if (10< num < 50):
        count += 1
print(count)
numbers = []

while True:
    data = input()
    if data.lower() == "end": 
        break
    try:
        num = float(data)       
        numbers.append(num)
    except ValueError:
        print("กรุณาป้อนตัวเลขหรือ 'end' เพื่อจบ")

if len(numbers) == 0:
    print("ไม่มีข้อมูล")
else:
    print(f"Max = {max(numbers)}")
    print(f"Min = {min(numbers)}")
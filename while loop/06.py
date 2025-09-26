def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b


while True:
    print("\n===== เมนู =====")
    print("1. บวกเลขสองจำนวน")
    print("2. ลบเลขสองจำนวน")
    print("3. คูณเลขสองจำนวน")
    print("4. ออก")
    
    choice = input("เลือกเมนู (1-4): ")
    
    if choice == "4":
        print("จบโปรแกรม")
        break
    
    if choice in ["1", "2", "3"]:
        a = float(input("ป้อนเลขตัวที่ 1: "))
        b = float(input("ป้อนเลขตัวที่ 2: "))
        
        if choice == "1":
            print(f"{add(a, b)}")
        elif choice == "2":
            print(f"{sub(a, b)}")
        elif choice == "3":
            print(f"{mul(a, b)}")
    else:
        print("กรุณาเลือกเมนูที่ถูกต้อง")
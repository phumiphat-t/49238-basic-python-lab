score = int(input("คะแนน"))

if 0 <= score <= 100:
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("กรอกคะแนนช่วง 0 ถึง 100 เท่านั้น")
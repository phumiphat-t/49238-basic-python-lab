score_a = int(input("กรอกคะแนนเก็บ (0-30): "))
score_b = int(input("กรอกคะแนนกลางภาค (0-30): "))
score_c = int(input("กรอกคะแนนปลายภาค (0-40): "))

total = score_a + score_b + score_c

if total >= 80:
    print("A")
elif total >= 75:
    print("B+")
elif total >= 70:
    print("B")
elif total >= 65:
    print("C+")
elif total >= 60:
    print("C")
elif total >= 55:
    print("D+")
elif total >= 50:
    print("D")
else:
    print("F")
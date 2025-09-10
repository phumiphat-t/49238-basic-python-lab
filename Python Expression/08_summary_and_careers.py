ba, tp, np = map(float, input("bill amout, Tip percent, number of people").split())
ta = ba * (tp / 100)
tb = ba + ta
app = tb / np
print(f"Each person per pays : {app:.2f}")
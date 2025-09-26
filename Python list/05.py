n = int(input("n= "))
odd = []; even = []
for i in range (n):
    skibiditoilet = int(input())
    if ((skibiditoilet % 2)==0):
        even.append(skibiditoilet)
    else:
        odd.append(skibiditoilet)
print(odd)
print(even)
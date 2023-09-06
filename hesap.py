import os
while True:
    os.system("cls")
    a = input()
    if "." in a:
        a = a.replace(".","")
    if "," in a:
        a = a.replace(",",".")
    a = float(a)
    print(a / 1.18)
    input()
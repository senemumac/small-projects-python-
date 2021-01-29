yan = int(input("Yan Giriniz:"))
dik = int(input("Dik Giriniz:"))

for i in range(dik):
    if i == 0:
        print("- "*(yan))
    elif i == dik-1:
        print("- "*(yan))
        print()
    else:
        print("|"+"  "*(yan-2)+" |")

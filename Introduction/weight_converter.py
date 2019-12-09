name = input('Weight ')
weight = int(name)

flag = input("(L)bs or (K)g :")

if flag.upper()=="L":
    weight = weight * 0.45
    print(f"You are {weight} kilos")
elif flag.upper()=="K":
    weight = weight * 2.20
    print(f"You are {weight} pounds")
else:
    print("Invalid input")




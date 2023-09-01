#House Pattern in Python

for i in range(1, 24):
    for j in range(1, 41):
        if 1 <= i <= 11:
            if i == 1 and 11 <= j <= 30:
                print("-", end="")
            elif i > 1 and (12 - i) == j:
                print("/", end="")
            elif i > 1 and (29 + i) == j:
                print("\\", end="")
            elif i <= 11 and (10 + i) == j:
                print("\\", end="")
            elif (12 - i) <= j <= (10 + i):
                print("S", end="")
            elif (10 + i) <= j <= (29 + i):
                print("Y", end="")
            else:
                print(" ", end="")
        elif i <= 16:
            if j == 1 or j == 21 or j == 40:
                print("|", end="")
            else:
                print("#", end="")
        else:
            if j == 1 or j == 21 or j == 40:
                print("|", end="")
            elif j <= 6 or (15 <= j <= 21):
                print("@", end="")
            elif j == 7 or j == 14:
                print("|", end="")
            elif j == 22 or j == 39:
                print("@", end="")
            elif i <= 20:
                if j == 23 or j == 38:
                    print("|", end="")
                else:
                    print(" ", end="")
            else:
                if 23 <= j <= 38:
                    print("@", end="")
                else:
                    print(" ", end="")
    print()
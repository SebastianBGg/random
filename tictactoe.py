bord = ["S","S","S","S","S","S","S","S","S"]
x = 1
def brett():
    print(bord[0], bord[1], bord[2])
    print(bord[3], bord[4], bord[5])
    print(bord[6], bord[7], bord[8])
def spiller1():
    y2 = 1
    while y2 == 1:
        svar = int(input("Si et tall mellom 1 til 9: "))
        svar -= 1
        if bord[svar] != "S":
            print("Den er tatt")
        if bord[svar] == "S":
            bord[svar] = "X"
            y2 = 0
def spiller2():
    y1 = 1
    while y1 == 1:
        svar2 = int(input("Si et tall mellom 1 til 9: "))
        svar2 -= 1
        if bord[svar2] != "S":
            print("Den er tatt")
        if bord[svar2] == "S":
            bord[svar2] = "O"
            y1 = 0
def check():
    if bord[0] == "O":
        if bord[3] == "O":
            if bord[6] == "O":
                print("O vant")
                x = 0
        if bord[1] == "O":
            if bord[2] == "O":
                print("O vant")
                x = 0
        if bord[4] == "O":
            if bord[8] == "O":
                print("O vant")
                x = 0
    if bord[8] == "O":
        if bord[5] == "O":
            if bord[2] == "O":
                print("O vant")
                x = 0
        if bord[8] == "O":
            if bord[6] == "O":
                print("O vant")
                x = 0
    if bord[0] == "X":
        if bord[3] == "X":
            if bord[6] == "X":
                print("X vant")
                x = 0
        if bord[1] == "X":
            if bord[2] == "X":
                print("X vant")
                x = 0
        if bord[4] == "X":
            if bord[8] == "X":
                print("X vant")
                x = 0
    if bord[8] == "X":
        if bord[5] == "X":
            if bord[2] == "X":
                print("X vant")
                x = 0
        if bord[8] == "X":
            if bord[6] == "X":
                print("X vant")
                x = 0

while x == 1:
    brett()
    spiller1()
    check()
    brett()
    spiller2()
    check()

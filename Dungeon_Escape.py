import random
import datetime

startTime = datetime.datetime.now().time().minute
endTime = startTime + 2

xValue = [0, 1, 2, 3]
yValue = [0, 1, 2, 3]
px = random.choice(xValue)
xValue.remove(px)
py = random.choice(yValue)
yValue.remove(py)
kx = random.choice(xValue)
xValue.remove(kx)
ky = random.choice(yValue)
yValue.remove(ky)
ex = random.choice(xValue)
xValue.remove(ex)
ey = random.choice(yValue)
yValue.remove(ey)
print(xValue)
print(yValue)


play = 1
print()
print("""█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")
print()
print("From this moment, you will have 2 minutes to end this game!")
while play == 1:
    for y in range(4):
        for x in range(4):
            if x == px and y == py:
                print("P", end=" ")
            elif x == kx and y == ky:
                print("K", end=" ")
            elif x == ex and y == ey:
                print("E", end=" ")
            else:
                print("-", end=" ")
        print()

    print()
    move = input("Your move(W, A, S, D)?").lower()
    nowTime = datetime.datetime.now().time().minute
    if nowTime >= endTime:
        print("You`ve runned out of time!")
        play = 0
    print()
    require = 0

    while move != 'w' and move != "s" and move != "a" and move != "d":
        print()
        print('''─────────▄▄───────────────────▄▄──
──────────▀█───────────────────▀█─
──────────▄█───────────────────▄█─
──█████████▀───────────█████████▀─
───▄██████▄─────────────▄██████▄──
─▄██▀────▀██▄─────────▄██▀────▀██▄
─██────────██─────────██────────██
─██───██───██─────────██───██───██
─██────────██─────────██────────██
──██▄────▄██───────────██▄────▄██─
───▀██████▀─────────────▀██████▀──
──────────────────────────────────
──────────────────────────────────
──────────────────────────────────
───────────█████████████──────────
──────────────────────────────────
──────────────────────────────────''')
        move = input("Please enter W, A, S or D!").lower()
        print()
    if move == "w":
        pyn = py - 1
        pxn = px
    elif move == "s":
        pyn = py + 1
        pxn = px
    elif move == "a":
        pxn = px - 1
        pyn = py
    elif move == "d":
        pxn = px + 1
        pyn = py

    if pxn == kx and pyn == ky:
        kx = 5
        ky = 5
        px = pxn
        py = pyn
        print()
        print('''▒▒▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
▒▒▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█
▒▒▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄
▒▒▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█
▒▒█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█
▒▒▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█
▒▒▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█
▒▒▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█
▒▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█
▒▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█''')
        print()
        print("You`ve picked up a key!!!")
        print()
    if pxn == ex and pyn == ey:
        if kx == 5 and ky == 5:
            print('''░░░░░░░░░░░░▄▄▄█▀▀▀▀▀▀▀▀█▄▄▄░░░░░░░░░░░░
░░░░░░░░▄▄█▀▀░░░░░░░░░░░░░░▀▀█▄▄░░░░░░░░
░░░░░░▄█▀░░░░▄▄▄▄▄▄▄░░░░░░░░░░░▀█▄░░░░░░
░░░░▄█▀░░░▄██▄▄▄▄▄▄▄██▄░░░░▄█▀▀▀▀██▄░░░░
░░░█▀░░░░█▀▀▀░░▄██░░▄▄█░░░██▀▀▀███▄██░░░
░░█░░░░░░▀█▀▀▀▀▀▀▀▀▀██▀░░░▀█▀▀▀▀███▄▄█░░
░█░░░░░░░░░▀▀█▄▄██▀▀░░░░░░░░▀▄▄▄░░░▄▄▀█░
█▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀▀▀░░▀█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄██░░▀█░░░█
█░░░░░░░░░░░░░░█░░░▄▄▄█▀▀▀░░░▄█▀░░░░░░░█
█░░░░░░░░░░░░░░░░░░▀░░░░░░░░█▀░░░░░░░░░█
█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█
░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░
░░░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█░░░
░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░
░░░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░░░''')
            print()
            print("Congrats, you`ve just escaped the dungeon!")
            play_again = input("Do you want to play again?(y/n)").lower()
            while play_again != "n" and play_again != "y":
                print('''─────────▄▄───────────────────▄▄──
──────────▀█───────────────────▀█─
──────────▄█───────────────────▄█─
──█████████▀───────────█████████▀─
───▄██████▄─────────────▄██████▄──
─▄██▀────▀██▄─────────▄██▀────▀██▄
─██────────██─────────██────────██
─██───██───██─────────██───██───██
─██────────██─────────██────────██
──██▄────▄██───────────██▄────▄██─
───▀██████▀─────────────▀██████▀──
──────────────────────────────────
──────────────────────────────────
──────────────────────────────────
───────────█████████████──────────
──────────────────────────────────
──────────────────────────────────''')
                play_again = input("Please answer yes or no!(y/n)").lower()
                print()
            if play_again == "n":
                play = 0
                print()
                print("Bye!!!")
                print()
                print('''_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██''')
                print()
            elif play_again == "y":
                print()
                print('''★ ☆ ✰ ✯ ✡ ✪ ✶ ✱ ✲ ✴ ✼ ✻ ✵ ❇ ❈ ❊ ❖ ❄ ❆ ❋ ❂ ⁂ ★ ☆ ✰ ✯ ✡ ✪ ✶''')
                print()
                startTime = datetime.datetime.now().time().minute
                endTime = startTime + 2
                require = 1
                xValue = [0, 1, 2, 3]
                yValue = [0, 1, 2, 3]
                px = random.choice(xValue)
                xValue.remove(px)
                py = random.choice(yValue)
                yValue.remove(py)
                kx = random.choice(xValue)
                xValue.remove(kx)
                ky = random.choice(yValue)
                yValue.remove(ky)
                ex = random.choice(xValue)
                xValue.remove(ex)
                ey = random.choice(yValue)
                yValue.remove(ey)
        else:
            require = 1
            print('''░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█''')
            print()
            print("You can't exit, please acquire the key(s) first!")
            print()
    if pxn < 0 or pyn < 0 or pxn >= 4 or pyn >= 4:
        print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')
        print()
        print("You are not allowed to get out of the map!")
        print()
    else:
        if require == 0:
            px = pxn
            py = pyn


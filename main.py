from consoleio import *
from maindefs import *
from os import system

p1: str = " "
p2: str = " "
p3: str = " "
p4: str = " "
p5: str = " "
p6: str = " "
p7: str = " "
p8: str = " "
p9: str = " "
round: int = 1
win: str = "0"
choise: int = None
againint: int = 1

system('cls')

while (againint == 1):

    print(f" 1 | 2 | 3 ")
    print(f" --+---+--")
    print(f" 4 | 5 | 6 ")
    print(f" --+---+--")
    print(f" 7 | 8 | 9 ")

    while win == "0":
        choise = bekeres(round, p1, p2, p3, p4, p5, p6, p7, p8, p9)
        if round %2 == 1:
            match choise:
                case "1":
                    p1 = "O"
                case "2":
                    p2 = "O"
                case "3":
                    p3 = "O"
                case "4":
                    p4 = "O"
                case "5":
                    p5 = "O"
                case "6":
                    p6 = "O"
                case "7":
                    p7 = "O"
                case "8":
                    p8 = "O"
                case "9":
                    p9 = "O"
        else:
            match choise:
                case "1":
                    p1 = "X"
                case "2":
                    p2 = "X"
                case "3":
                    p3 = "X"
                case "4":
                    p4 = "X"
                case "5":
                    p5 = "X"
                case "6":
                    p6 = "X"
                case "7":
                    p7 = "X"
                case "8":
                    p8 = "X"
                case "9":
                    p9 = "X"
        system('cls')
        printtable(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        round += 1
        win = checkwin(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    if win == "1":
        print(f"X nyert!")
        againint = again()
        win = "0"
    elif win == "2":
        print(f"O nyert!")
        againint = again()
        win = "0"
    elif win == "3":
        print("Döntetlen")
        againint = again()
        win = "0"

    p1: str = " "
    p2: str = " "
    p3: str = " "
    p4: str = " "
    p5: str = " "
    p6: str = " "
    p7: str = " "
    p8: str = " "
    p9: str = " "



#Even: X - Win: 1
#Odd: O - Win: 2
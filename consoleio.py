from os import system

def printtable(p1: str, p2: str, p3: str, p4: str, p5: str, p6: str, p7: str, p8: str, p9: str) -> None:
    print(f" {p1} | {p2} | {p3}            1 | 2 | 3 ")
    print(f" --+---+--            --+---+--")
    print(f" {p4} | {p5} | {p6}            4 | 5 | 6 ")
    print(f" --+---+--            --+---+--")
    print(f" {p7} | {p8} | {p9}            7 | 8 | 9 ")

def bekeres(round, p1, p2, p3, p4, p5, p6, p7, p8, p9) -> str:
    if round %2 == 0:
        now = "X"
    else:
        now = "O"
    print(f"{now} is up. (1-9): ", end="")
    choise = None
    while choise == None:
        choise = input()
        if choise.isnumeric():
            if int(choise) > 0 and int(choise) < 10:
                choisematch = str(choise)
                match choisematch:
                    case "1":
                        if p1 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "2":
                        if p2 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "3":
                        if p3 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "4":
                        if p4 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "5":
                        if p5 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "6":
                        if p6 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "7":
                        if p7 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "8":
                        if p8 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
                    case "9":
                        if p9 != " ":
                            print(f"Error! There is already another simbol. {now} is up. (1-9)", end="")
                            choise = None
                        else:
                            return str(choise)
            else:
                print("Error! Give a number between 1 and 9!")
                choise = None
        else:
            print("Error! Give a number!")
            choise = None

def again() -> int:
    strvar: str = None
    while strvar == None:
        print("Do you want to play again? (Y/N): ", end="")
        strvar = input()
        if strvar == "y" or strvar == "Y":
            system('cls')
            return 1
        elif strvar == "n" or strvar == "N":
            system('cls')
            return 0
        else:
            print("Error! Not proper answer. Play again: Y / Exit: N")
            strvar = None
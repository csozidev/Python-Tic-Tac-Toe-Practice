#na
def checkwin(p1, p2, p3, p4, p5, p6, p7, p8, p9) -> str:
    if (p1 == p2 and p2 == p3 and p1 != " "):
        if p1 == "X":
            return "1"
        else:
            return "2"
    elif (p4 == p5 and p5 == p6 and p4 != " "):
        if p4 == "X":
            return "1"
        else:
            return "2"
    elif (p7 == p8 and p8 == p9 and p7 != " "):
        if p7 == "X":
            return "1"
        else:
            return "2"
    elif (p1 == p4 and p4 == p7 and p1 != " "):
        if p1 == "X":
            return "1"
        else:
            return "2"
    elif (p2 == p5 and p5 == p8 and p2 != " "):
        if p2 == "X":
            return "1"
        else:
            return "2"
    elif (p3 == p6 and p6 == p9 and p3 != " "):
        if p3 == "X":
            return "1"
        else:
            return "2"
    elif (p1 == p5 and p5 == p9 and p1 != " "):
        if p1 == "X":
            return "1"
        else:
            return "2"
    elif (p3 == p5 and p5 == p7 and p3 != " "):
        if p3 == "X":
            return "1"
        else:
            return "2"
    elif (p1 != " "  and p2 != " "  and p3 != " "  and p4 != " "  and p5 != " "  and p6 != " "  and p7 != " "  and p8 != " "  and p9 != " "):
        return "3"
    else:
        return "0"

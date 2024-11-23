a1 = 11
a2 = 22
a3 = 33
a4 = 44
a5 = 55

if a1 > a2:
    if a1 > a3:
        if a1 > a4:
            if a1 > a5:
                print("a1 is highest")
            else:
                print("a5 is highest")
        else:
            if a4 > a5:
                print("a4 is highest")
            else:
                print("a5 is highest")
    else:
        if a3 > a4:
            if a3 > a5:
                print("a3 is highest")
            else:
                print("a5 is highest")
        else:
            if a4 > a5:
                print("a4 is highest")
            else:
                print("a5 is highest")
else:
    if a2 > a3:
        if a2 > a4:
            if a2 > a5:
                print("a2 is highest")
            else:
                print("a5 is highest")
        else:
            if a4 > a5:
                print("a4 is highest")
            else:
                print("a5 is highest")
    else:
        if a3 > a4:
            if a3 > a5:
                print("a3 is highest")
            else:
                print("a5 is highest")
        else:
            if a4 > a5:
                print("a4 is highest")
            else:
                print("a5 is highest")
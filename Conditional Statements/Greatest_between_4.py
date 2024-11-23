num1 = 2000
num2 = 100
num3 = 500
num4 = 3000

if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("num1 is highest")
        else:
            print("num4 is highest")
    else:
        if num3 > num4:
            print("num3 is highest")
        else:
            print("num4 is highest")
else:
    if num2 > num3:
        if num2 > num4:
            print("num2 is highest")
        else:
            print("num4 is highest")
    else:
        if num3 > num4:
            print("num3 is highest")
        else:
            print("num4 is highest")
b1 = 100
b2 = 200
b3 = 300
b4 = 400

if b1 < b2:
    if b1 < b3:
        if b1 < b4:
            print("b1 is lowest")
        else:
            print("b4 is lowest")
    else:
        if b3 < b4:
            print("b3 is lowest")
        else:
            print("b4 is lowest")
else:
    if b2 < b3:
        if b2 < b4:
            print("b2 is lowest")
        else:
            print("b4 is lowest")
    else:
        if b3 < b4:
            print('b3 is lowest')
        else:
            print("b4 is lowest")

var = 30

# Nested if blocks---->>
if var % 2 == 0:
    print('Div by 2')
    if var % 3 == 0:
        print("Div by 3")
        if var % 4 == 0:
            print("Div by 4")
            if var % 5 == 0:
                print("Div by 5")

# Normal if blocks---->>
if var % 2 == 0:
    print("Div by 2")

if var % 3 == 0:
    print("Div by 3")

if var % 4 == 0:
    print("Div by 4")

if var % 5 == 0:
    print("Div by 5")
from turtle import *
def plastve(vel):
    for i in range(6):
        forward(vel)
        left(60)
    forward(vel)
    right(60)
    for i in range(6):
        for i in range(5):
            forward(vel)
            left(60)
        left(120)

def ctverec(vel):
    for i in range(4):
        forward(vel)
        left(90)

def sestiuhelnik(vel1):
    for i in range(6):
        forward(vel1)
        left(60)
        
def objekt():
    try: x = int(input("Zadejte velikost: "))
    except UnboundLocalError or ValueError: print("Špatná velikost")
    if(tvar=="ctverec"):
        ctverec(x)
        exitonclick()
    elif(tvar=="sestiuhelnik"):
        sestiuhelnik(x)
        exitonclick()
    elif(tvar=="plastve"):
        plastve(x)
        exitonclick()
    else: print("Špatný tvar")
tvar = input("Zadejte tvar? (ctverec, sestiuhelnik nebo plástve: ")
objekt()

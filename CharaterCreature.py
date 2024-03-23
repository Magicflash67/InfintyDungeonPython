import random
stats = [8,8,8,8,8,8]
def DiceRoller(num, MaxValue):
    d =0
    MaxValue = MaxValue + 1
    Overall = 0
    while d != num:
        Overall = random.randrange(1, MaxValue, 1)
        d = d + 1
    return Overall
def CCC(classs):
    if classs == "fighter" or classs == "rouge" or classs == "druid" or "paladin" or "ranger":
        return True
    else: 
        while True:
            dclass = input("please input a (fighter, rouge, druid, paladin, ranger.\n)")
            CCC(dclass)
def ABS(username, dclass):
    ABT =  None
    ABSP = 27
    ABT = input("ahh its you, "+username+" the "+dclass+"\n now did you train to get your skill (pointbuy), or did you get lucky (4d6 dropthe lowest)\n so type  \"by you\" for stats made by you or \"lucky\" to for 4d6 drop the lowest with your abilty rolls\n")
    if ABT == "by you":
        print("you have 27 point minum 8 go to ever stat max of 15 for every stats")
        stats[1]=input("how many points to Strength")
        while (stats[1] <8 or stats[1] > 15):
            if (stats[1] <8):
              input("you needed a minum of 8 points to Strength \ntry again\n")
            if (stats[1] > 15):
               input("can only have a max of 15 points to Strength\n try again\n")
        ABSP = ABSP - (stats[1] - 8)
        if (ABSP <= -1):
            print("your out of points, point buy is over")
            return None
        stats[2]=input("how many points to dexstrity\n")
        while (stats[2] <8 or stats[1] > 15):
            if (stats[2] <8):
               input("you needed a minum of 8 points to dexstrity \ntry again\n")
            if (stats[2] > 15):
               input("can only have a max of 15 points to dexstrity\n try again\n")
        ABSP = ABSP - (stats[2] - 8)
        if (ABSP <= -1):
            print("your out of points, point buy is over")
            return None
        stats[3]=input("how many points to Constuison\n")
        while (stats[3] <8 or stats[1] > 15):
            if (stats[3] <8):
               input("you needed a minum of 8 points to dexstrity \ntry again\n")
            if (stats[3] > 15):
               input("can only have a max of 15 points to dexstrity\n try again\n")
        ABSP = ABSP - (stats[3] - 8)
        if (ABSP <= -1):
            print("your out of points, point buy is over")
            return None
        stats[4]=input("how many points to Inteligence")
        while (stats[4] <8 or stats[4] > 15):
            if (stats[4] <8):
              input("you needed a minum of 8 points to Inteligence \ntry again\n")
            if (stats[4] > 15):
               input("can only have a max of 15 points to Inteligence\n try again\n")
        ABSP = ABSP - (stats[4] - 8)
        if (ABSP <= -1):
            print("your out of points, point buy is over")
            return None
        stats[5]=input("how many points to wisdom\n")
        while (stats[5] <8 or stats[5] > 15):
            if (stats[5] <8):
               input("you needed a minum of 8 points to wisdom \ntry again\n")
            if (stats[5] > 15):
               input("can only have a max of 15 points to wisdom\n try again\n")
        ABSP = ABSP - (stats[5] - 8)
        if (ABSP <= -1):
            print("your out of points, point buy is over")
            return None
        stats[6]=input("how many points to Charisma\n")
        while (stats[6] <8 or stats[1] > 15):
            if (stats[6] <8):
               input("you needed a minum of 8 points to Charisma \ntry again\n")
            if (stats[6] > 15):
               input("can only have a max of 15 points to Charisma\n try again\n")
        ABSP = ABSP - (stats[6] - 8)
        if (ABSP <= -1):
            print("your out of points, point buy is over")
            return None
        i = 0
    if ABT == "lucky":
        while (i != 6):        
            v1 = DiceRoller()
            v2 = DiceRoller()
            v3 = DiceRoller()
            v4 = DiceRoller()
            v5 = DiceRoller()
            v6 = DiceRoller()
            vv1 = max(v1, v2)
            vv2 = max(v3, v4)
            vv3 = max(v5, v6)
            TV1 = vv1+vv2+vv3
def charCreator():

    username = input("hello Young Adventurese what would your name be?\n")
    dclass = input("Now what in your class (fighter, rouge, druid, paladin, ranger.")
    CCC(dclass)
    ABS(username, dclass)
charCreator()
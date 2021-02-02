# MyRPG
#My first game that i ever made, im still working on it, ill ad a lv up system to it soon 
#This is the first update, ill ad image to evry fight soon, if you have any tips, please share it below. 


import random
import sys

atack1 = 0
hp1 = 0

atack2 = 0
hp2 = 0


did1 = random.randint(1,4)
did2 = random.randint(1,5)



#def math(hp,atack):
 #   feels_bad=(hp-atack)
  #  return feels_bad



def stats(atack, hp):
    global atack1
    global hp1
    atack1 += atack
    hp1 += hp
    return print("Atack=" + str(atack1), "\nHP=" + str(hp1))


def stats2(x, y):
    global atack2
    global hp2
    atack2 += x
    hp2 += y
    return print("Atack, of your enemy: " + str(atack2) + "\nHP, of your enemy: " + str(y))



character_class = input("""Enter a class:ninja or warrior or wizard: 
""").lower()

while character_class == "wizard" or "warrior" or "ninja" :
        if character_class == "wizard":
            stats(4,2)
            break
        elif character_class == "warrior":
            stats(2,4)
            break
        elif character_class == "ninja":
            stats(3,3)
            break
        else:
            sys.exit("You Enter a valid value, please re-run the game the game.")
            break


input("Now, u find with your first enemy, ")
Archanioł=stats2(did1,did2)
input("ATACK HIM!!!")



def loop_battle():
    global hp2,hp1,atack2,atack1
    hp2 -= atack1
    if hp2 <=0:
        WINMESSAGE = print("You win!! atack + 1")

    else:
        hp1 -= atack2

        if hp1 <= 0:
            print("Sorry you lose hp - 1")
        elif hp1 > 0:
            loop_battle()

#This is the loop for last fight
def loop_battle2():
    global hp2,hp1,atack2,atack1
    hp2 -= atack1
    if hp2 <=0:
        WINMESSAGE = print("You win the game congratulations! :)")

    else:
        hp1 -= atack2

        if hp1 <= 0:
            print("Sorry you lose, maybe next time! :) ")
        elif hp1 > 0:
            loop_battle()

loop_battle()

#hp1 is my hp also attack1 is my atack
#hp2 is hp of the enemy so now i have to restart the hp of both
if hp1 <=0:
    atack1 = 0
    hp1 = -1

    atack2 = 0
    hp2 = 0
elif hp2 <= 0:
    atack1 = 1
    hp1 = 0

    atack2 = 0
    hp2 = 0


while character_class == "wizard" or "warrior" or "ninja" :
        if character_class == "wizard":
            stats(4,2)
            break
        elif character_class == "warrior":
            stats(2,4)
            break
        elif character_class == "ninja":
            stats(3,3)
            break
        else:
            sys.exit("You Enter a valid value, please re-run the game the game.")
            break



input("You find another enemy this time, he is stronger then before!!!")
did3 = random.randint(1,5)
did4 = random.randint(1,6)
stats2(did3,did4)
input("Fight him!!")
loop_battle()

if hp1 <=0:
    atack1 = 0
    hp1 = -2

    atack2 = 0
    hp2 = 0
elif hp2 <= 0:
    atack1 = 2
    hp1 = 0

    atack2 = 0
    hp2 = 0

while character_class == "wizard" or "warrior" or "ninja":
    if character_class == "wizard":
        stats(4, 2)
        break
    elif character_class == "warrior":
        stats(2, 4)
        break
    elif character_class == "ninja":
        stats(3, 3)
        break
    else:
        sys.exit("You Enter a valid value, please re-run the game the game.")
        break



input("Now you fight your boss!!!")
did5 = random.randint(2,6)
did6 = random.randint(2,7)
stats2(did5,did6)
input("Fight him!!")
loop_battle2()

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
makaron=stats2(did1,did2)
input("ATACK HIM!!!")


def loop_battle():
    global hp2,hp1,atack2,atack1
    hp2 -= atack1
    if hp2 <=0:
        WINMESSAGE = print("You win!!")

    else:
        hp1 -= atack2

        if hp1 <= 0:
            print("Sorry you lose")
        elif hp1 > 0:
            loop_battle()

loop_battle()







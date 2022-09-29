import random

# items
doorkey = 0
map = 0
oxygentank = 0
flare = 0
axe = 0
planks = 0
jewel = 0
amulet = 0
dwarfkey = 0
flag = 0

# progression
sleep = 0
question = 1
inventory = []
playerinv = "\n".join(inventory)
number = (random.randrange(1, 10))


print("""You slowly open your eyes, still feeling drowsy.
You shoot up like a rocket, remembering today is your coming of age ritual.
The ritual is not easy, every person that reaches 18 years old has to climb the sacred mountain.
However, you feel determined to press on, and get out of bed.\n""")

print("""You rush out bed, getting dressed in most of your climbing hear along the way.
You now stand in your room, with an old creaky door infront of you, the faintest ray of light shining trough.
To your left is an unremarkable nightstand, and behind you is the bed you just left.""")

while question == 0:
  print("game over, for now")

while question == 1:
    loc1 = input("What do you do?: ").lower()
    if loc1 == "inventory" or loc1 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    if ("open" and "door") in loc1 and doorkey == 0:
        print("You try to open the door, but it is locked.")
    elif ("open" and "door") in loc1 and doorkey == 1:
        print("You use the key on the door and head outside.\n")
        question = 2
        break
    elif loc1 == "open nightstand" or loc1 == "look in nightstand":
        print("You haven't even looked at the nightstand yet.")
    elif loc1 == "look under bed" or loc1 == "check under bed":
        print("Apart from the heaps of dust and a few lost socks, you see nothing of value.")
    while loc1 == "look at nightstand" or loc1 == "inspect nightstand":
        print("""You see nothing on top of the nightstand except a simple lamp.
The shoddy drawers of the stand hang loose ever so slightly.""")
        standquestion = input("What do you do with the nightstand?: ").lower()
        while "nightstand" and ("open" or "look in") in standquestion:
          if doorkey == 1:
            print("You already grabbed your key, no reason to be back here again.")
            standquestion = ""
            loc1 = ""
            continue
          else:
            print("""You open the nightstand's loose drawers and find a familiar key inside.
This is your house key.""")
            keyquestion = input("What do you do with the key?: ").lower()
            if ("grab" or "take") and "key" in  keyquestion: 
                print("You grab your house key.")
                doorkey = 1
                inventory.append("House key")
                playerinv = "\n".join(inventory)
                loc1 = ""
                standquestion = ""
                continue
            elif keyquestion == "go back" or keyquestion == "leave":
                standquestion = ""
                continue
            else: print("You can't do that right now.")
        if standquestion == "look at lamp" or standquestion == "inspect lamp":
            print("It is just a lamp.")
        elif standquestion == "leave" or standquestion == "go back":
            loc1 = ""
            continue
    

print("""As you swing open the front door, the cold breeze travelling down the mountain hits you like a punch in the nose.
You suddenly realize the strenuous journey you are about to undertake and take a deep sigh. """)
print("""As you look around, you see an old man sitting on the stump of a ginormous tree. He seems to want to give you something.
There is also an oxygen tank planted against the wall of your house, someone must've left it out.
To the north of you, you see the sacred mountain, standing sturdy as always. The mountain range stretches as far as the eye can see.""")

while question == 2:
    loc2 = input("What do you do?: ").lower()
    if loc2 == "inventory" or loc2 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    elif loc2 == "go north" or loc2 == "climb mountain":
        print("You shake off your anxiety, and begin your ascent to the mountain peak.")
        question = 3
        break
    while ("talk" or "approach") in loc2 and "old man" in loc2 and map == 1:
        print("You've already talked to the old man.")
        loc2 = ""
        continue
    while ("talk" or "approach") in loc2 and "old man" in loc2:
        print("""You approach the old man, before you can open your mouth he says:
\"Hello son! Today's your big day, eh?\"
\"Well, let me give you this map of the mountain, without it, you'll surely get lost!\"
You make sure to put the map to the mountain firmly in your backpack.""")
        map = 1
        loc2 = ""
        inventory.append("Map of the Mountain")
        playerinv = "\n".join(inventory)
        continue
    while "inspect" in loc2 and oxygentank == 1 or "look at" in loc2 and oxygentank == 1 or "oxygen tank" in loc2 and oxygentank == 1:
        print("You've already picked up the oxygen tank.")
        loc2 = ""
        continue
    while "inspect" in loc2 or "look at" in loc2 and "oxygen tank" in loc2:
        print("""It looks like a regular oxygen tank, yet it feels familiar. 
This might come in handy later on.""")
        oxyquestion = input("What do you do with the oxygen tank?: ")
        if "pick up" in oxyquestion or "grab" in oxyquestion:
            print("You grab the oxygen tank and tightly strap it to your back.")
            oxygentank = 1
            loc2 = ""
            inventory.append("Oxygen Tank")
            playerinv = "\n".join(inventory)
            continue
        elif "leave" in oxyquestion or "go back" in oxyquestion:
            print("You leave the oxygen tank.")
            loc2 = ""
            continue
        else: 
            print("You can't do that right now.")
            continue
        
        
if question == 3 and map == 0:
    print("""After aimlessly walking around the mountain for hours, you get lost. 
No matter where you turn to, it all looks the same.
After enough time of wasting your energy, you starve to death.
(Maybe you should've gotten the map from that old man?)""")
    question = 0
    while question == 0:
        print("game over, temporary")
        break
elif question == 3 and map == 1:
    print("""After travelling for a while, you stumble onto a roadblock. 
The path you've taken all this way has been completely blocked out by a snowslide a few hours prior.
You see an icy cave to your left, with nowhere else to turn you cautiously enter the cave.\n""")
    print("""You enter the cave, both eerie and beautiful alike. The cave almost seems to be in stasis between freezing and melting.
You now stand in the middle of the cave, A ray of light shines trough a hole at the top, inviting you to it's only exit, and your only way forward.
With what will you make the climb however? You cannot climb the wall to the top with your hands.
To your left you spot the dead body of a previous adventurer, almost perfectly preserved due to the cold.""")

while question == 3:
    loc3 = input("What will you do?: ").lower()
    if loc3 == "inventory" or loc3 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    elif ("climb" and "wall") in loc3 and axe == 0:
        print("Still you try to scale the wall, but your hands dont grip the icy surface.")
    elif ("climb" and "wall") in loc3 and axe == 1:
        question = 4
        print("""You use the ice axe you found to climb to the top of the cave.
With a small glance to the unfortunate adventurer down below, you press on and are determined you will not meet the same fate.""")
        continue
    elif loc3 == "look at cave" or loc3 == "inspect cave":
        print("The strange beauty of the cave mystifies you. The juxtaposition of the corpse against the alluring cave makes you sick to your stomache.")
    elif loc3 == "look at hole" or loc3 == "inspect hole":
        print("The claustrophic hole at the top of the cavern is almost taunting you, letting you taste the adventure ahead yet granting you no passage.")
    elif ("leave") in loc3:
        print("And then what? This cave is your only way forward.")
    while ("look at" or "inspect" or "check") and ("body") in loc3:
        print("""\nThe corpse of a man lies before you, his body as rigid as the ice it is laying on.
After closely inspecting the man's gear, most of it has decayed beyond use. However there are two items that catch your eye.
His ice axe is firmly hung up by rope on his side, and there seems to be a usable flare gun in his backpack, with one flare left.\n""")
        while ("look at" or "inspect" or "check") and ("body" or "corpse") in loc3:
            bodyquestion = input("What do you do with the body? (Type \"leave\" to go back.): ")
            if ("grab" or "pick up") and ("axe" or "ice axe") in bodyquestion and axe == 1:
                print("You have already picked up the ice axe.")
                continue
            elif ("grab" or "pick up") and ("flare" or "flare gun") in bodyquestion and flare == 1:
                print("You have already picked up the flare gun and flare.")
                continue
            elif ("grab" or "pick up") and ("axe" or "ice axe") in bodyquestion:
                print("You grab the axe off his corpse, and hang it off your hip.\n")
                axe = 1
                inventory.append("Ice axe")
                playerinv = "\n".join(inventory)
                continue
            elif ("grab" or "pick up") and ("flare" or "flare gun") in bodyquestion:
                print("You grab the flare gun and the singular flare out of the man's backpack, and store it in your backpack.")
                flare = 1
                inventory.append("Flare gun")
                playerinv = "\n".join(inventory)
                continue
            elif bodyquestion == "leave" or bodyquestion == "go back":
                loc3 = ""
                continue
            else: print("I do not know that command.")

if question == 4:
  print("""Climbing a vertical wall was no joke, it's getting pretty late and the fatigue is starting to catch up with you.
However in the corner of the eye, you cannot believe how lucky you are.
You spot a log cabin, it's inviting warm colour almost pulling you in.""")       
while question == 4:
    loc4 = input("What do you do?: ").lower()
    if loc4 == "inventory" or loc4 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    elif loc4 == "keep walking" or loc4 =="continue" or loc4 == "keep going" or "ignore" in loc4:
        print("""\nYou decide you don't need sleep, and alternatively need the extra hours of the night to travel.
The back of your head still questioning if this is the right choice, you continue on your journey.""")
        question = 5
        sleep = 0
        break
    while loc4 == "inspect cabin" or loc4 == "go to the cabin" or loc4 == "enter cabin":
        print("""You slowly peek open the door, noticing it's not locked. As far as you know, there is no one inside either.
The cabin is a rather desolate place, however there is one thing that you desperately need. A bed.""")
        cabinquestion = input("What do you do in the cabin?: ").lower()
        if "sleep" in cabinquestion or "stay" in cabinquestion:
            print("""You take off your gear and head to bed, even under itchy covers you quickly drift off to sleep.
The next morning, you get dressed and head out.""")
            sleep = 1
            question = 5
            loc4 = ""
        elif "leave" in cabinquestion or "go back" in cabinquestion:
            print("""Even while looking at the bed, you still decide you need to continue your journey.
You leave the cabin and keep going.""")
            loc4 = ""
            question = 5
            continue
        

if question == 5 and sleep == 0:
    print("""You've decided to press on against your body's demand and kept going forward trough the trial.
You have to put serious effort into making sure your eyelids don't shut on their own. 
However this feeling doesn't last long. 
The growl of a snow leopard pierces your body like the sharpened edge of a dagger, and you are now face-to-face with it.\n""")

elif question == 5 and sleep == 1:
    print("""Feeling rested, you make your way along the mountain, making sure to make use of your map along the way. 
It is at this moment that you feel a bit off, like something isn't right.
Your suspicions were quickly affirmed when you spot a snow leopard stalking you.\n""")

while question == 5:
    if flare == 0:
        print("""You scramble for something to defend yourself with, and in panic you swing the ice axe fastened to your hip.
However, this leopard doesn't seem to care about your trivial little ice axe, and instantly mauls you.
Game over.
(Only the flare will defend you against this animal.)""")
        question = 0
        break
    elif flare == 1:
        print("""You chaotically scavenge for anything of use, in an act of quick thinking you remember your flare gun.
You fire off the flare gun towards the direction of the leopard, and luckily for you it scurries off.
You decide to throw away the flare gun, it is of no use to you now anyways.
With a long sigh and after wiping some sweat off your brow, you continue onwards.""")
        inventory.remove("Flare gun")
        flare = 0
        question = 6
        break


if question == 6:
    print("Ravine arrival, you see a broken hut")
    if question == 6 and oxygentank == 0:
        print("You've ran out of oxygen and died")
        question = 0
        
    while question == 6 and oxygentank == 1:
        loc6 = input("What do you do?: ")
        if loc6 == "inventory" or loc6 == "check inventory":
            if playerinv == "":
                print("You have nothing in your inventory")
            else:
                print("Inventory\n********")
                print(playerinv)
            
        if "jump" in loc6:
            print("You tried to jump across the ravine but the gap was too big and you died")
            question = 0
            break
        elif "cross" and "ravine" in loc6 and planks == 0:
            print("the gap is too big maybe there's something i can use to close the gap")
        elif "cross" and "ravine" in loc6 and planks == 1:
            print(" You use the planks to make a makeshift bridge and cross the ravine")
            question = 6
            loc6 = ""
        if "inspect" in loc6 or "look at" in loc6 and "hut" in loc6:
            print("You approach the torn apart hut")
            hutquestion = input("What do you do at the hut?: ")
            if "grab" in hutquestion or "take" in hutquestion and "planks":
                print("You take the wooden planks with you")
                planks = 1
                inventory.append("Planks")
                playerinv = "\n".join(inventory)
                loc6 =""
                hutquestion = ""
                continue

        
if question == 9:
    print("You see a yeti standing in your path, you carefully approach the yeti")
    while question == 9:
        loc9 = input("What do you do?: ")
        if loc9 == "inventory" or loc9 == "check inventory":
            if playerinv == "":
                print("You have nothing in your inventory")
            else:
                print("Inventory\n********")
                print(playerinv)

        if "run" in loc9:
            print("you can't run away")
        elif "approach" in loc9 or "talk" in loc9:
            print("The yeti breaks your ice axe tell you that it will let you go trough if you can guess which number he's thinkign about ")
            yetiquestion = int(input("Guess what number the yeti is thinking about: "))
            if yetiquestion == number:
                print("You shall pass")
                inventory.remove("axe")
                question = 10
            elif yetiquestion < number:
                print("too low guess again")
                yetiquestion =""
                continue
            elif yetiquestion > number:
                print("too high guess again")
                yetiquestion = ""
                continue


if question == 11:
    print("You enter the icy cave using the amulet you got from the dwarves you see a elevator built by the dwarves")
    while question == 11:
        loc11=input("what do you do?: ")
if "inspect" or "check" and "elevator" in loc11:
    print("You approach the elevator, its missing a key and seems dormant ")
    elevatorquestion = input("What do you do at the elevator")
    if "enter" or "open" in elevatorquestion and dwarfkey == 1:
        print("the elevator is still dormant, maybe your key could activate it")
    elif "use key" or "activate" and "elevator" in elevatorquestion:
        print("You insert the mysterious key into the keyhole, the cave shakes as the elevator starts running")
        

    

 
        




        
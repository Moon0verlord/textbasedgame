import random
# items
doorkey = 0
map = 0
oxygentank = 0
flare = 0
axe = 0
planks = 0
gem = 0
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
        if "pick up" in oxyquestion or "grab" in oxyquestion or "take" in oxyquestion:
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
    print("""You enter the cave, both eerie and beautiful alike. The cave almost seems to flicker and glow.
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
The back of your head still questioning if this is the right choice, you continue on your journey anyways.""")
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
            question = 7
            loc6 = ""
        if "inspect" in loc6 or "look at" in loc6 and "hut" in loc6:
            print("You approach the torn apart hut")
            hutquestion = input("What do you do at the hut?: ")
            if "grab" in hutquestion or "take" in hutquestion or "pick up"  in hutquestion and "planks":
                print("You take the wooden planks with you")
                planks = 1
                inventory.append("Planks")
                playerinv = "\n".join(inventory)
                loc6 =""
                hutquestion = ""
                continue


if question == 7:
    print("""You can feel the peak of the mountain getting closer, however you also know that the dangers have not waned yet.
You keep marching forward until you come across a giant wall of seemingly solid ice. It's mysterious blue glow is very captivating to you.
Although there is an even MORE captivating glow inside the wall itself, just out of reach lodged inside the wall is a glowing yellow gem.
You almost feel urged to get it for some reason, yet you also feel like you are wasting time and should continue.""")


while question == 7:
    loc7 = input("What do you do?: ")
    if loc7 == "inventory" or loc7 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    elif ("keep going" in loc7 or "continue" in loc7 or "head north" in loc7) and gem == 0:
        print("You decide to keep going, and leave the gem behind. It's not worth the effort and/or time.")
        question = 8
        break
    elif ("keep going" in loc7 or "continue" in loc7 or "head north" in loc7) and gem == 1:
        print("You've decided to get the gem, it was too captivating to leave behind. With the gem stashed safely in your backpack, you continue.")
        question = 8
        break
    elif (loc7 == "grab gem" or loc7 == "get gem" or loc7 == "pick up gem") and gem == 1:
        print("You already have the gem in your inventory.")
    elif (loc7 == "grab gem" or loc7 == "get gem" or loc7 == "pick up gem") and gem == 0:
        print("""You frantically try to get the gem by force, but your hands just aren't enough to break trough the ice.
Maybe you should use an item of some kind?""")
    elif ("grab gem") and ("with axe") in loc7 and gem == 1 or ("get gem") and ("with axe") in loc7 and gem == 1:
        print("You've already gotten the gem in the wall.")
    elif ("grab gem") and ("with axe") in loc7 or ("get gem") and ("with axe") in loc7 and gem == 0:
        print("""You decide to use your climbing ice axe as a makeshift pickaxe to mine the gem out.
With some frantic mining work, you finally obtain the gem and stash it in your backpack.""")
        gem = 1
        inventory.append("Yellow Gem")
        continue

if question == 8:
    print("""You feel like you near the end of your journey, just a bit left. 
But it seems as soon as that thought crosses your mind, you see something that makes your heart sink. 
There is a big dwarven checkpoint infront of you, and it is your only way forward towards the peak of the mountain.
Taking your chances, you approach the checkpoint.\n""")

    print("""The loud cheering and clanking of ale mugs are heard from a good 50 meters away.
As you approach, a dwarven guard speaks to you from ontop of a large stonework wall.
"Oi! What do ye want?" he says. You explain to him you require passage towards the peak.
"I'm sorry but I cannae do that. There is an annual festival goin' on right now and I can't grant ye passage.
You sigh, and can't decide what to do. However you remember dwarves are a greedy people, and you might be able to bribe them.
But with what?\n""")

while question == 8:
    loc8 = input("What do you do?: ")
    if loc8 == "inventory" or loc8 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    elif "go back" in loc8 and gem == 1 or "leave" in loc8 and gem == 1:
        print("There's no reason to go back to the wall.")
    elif "go back" in loc8 and gem == 0 or "leave" in loc8 and gem == 0:
        print("You decide to go back to the wall, and get the beautiful yellow gem to try and bribe the dwarves.")
        question = 7
        break
    while "bribe" in loc8 and gem == 1 or "give gem" in loc8 and gem == 1:
        print("""You approach the dwarf guard again, and reluctantly offer him the gem in your backpack.
He seems stunned by your offer, and within a second the main gate retracts up into the large stonework wall.
A stubby dwarf with a beard half his body length comes jogging out, clad in ornamented plate armor.
"This cannae be!, this gem is the most beautiful thing I've ever laid me eyes on!"
He seems to hesitate a bit, but he grants you passage in exchange for the gem.

The dwarf warns you, the peak has shifted and is currently inaccessible by foot. 
Because the gem you gave him is so beautiful, he gives you two items to bypass the shifted peak.
He gives you an amulet that will show you a hidden wall into the mountain itself.
He also gives you a dwarven key, that can operate an elevator inside the mountain to bring you to the peak.
You continue on your journey towards the peak, you are surely close now.""")
        inventory.remove("Yellow Gem")
        inventory.append("Dwarven Amulet")
        inventory.append("Dwarven Key")
        amulet = 1
        dwarvenkey = 1
        question = 9
        break
    while "bribe" in loc8 and gem == 0 or "give gem" in loc8 and gem == 0:
        print("You have nothing to bribe the dwarves with. Something really shiny would work.")
        loc8 = ""
        continue


if question == 9:
    print("""With the warning from the dwarf still fresh in your mind, you can already see the peak grow larger and larger.
Your enthusiasm does not last long. A gigantic white-furred Yeti jumps infront of you, seemingly waiting for a traveller to pass by.
Before you can even react he lunges for your axe and snaps it in half like the twig of a birch tree.
He tells you can't pass unless you succeed at his number guessing game, and if you lose, you die.
(Talk with the Yeti to proceed to the guess game.)""")
    inventory.remove("Ice axe")
    axe = 0
    while question == 9:
        loc9 = input("What do you do?: ")
        if loc9 == "inventory" or loc9 == "check inventory":
            if playerinv == "":
                print("You have nothing in your inventory")
            else:
                print("Inventory\n********")
                print(playerinv)
        elif "run" in loc9:
            print("Each 10 steps you take is 1 for the Yeti, you can't outrun him.")
        elif "fight" in loc9:
            print("""The Yeti laughs at your feeble attempt of rebellion. 
With a single swipe of his claw you get thrown off the cliffside, and die in an instant.
(Maybe next time don't try to challenge an ape the size of a house)""")
            question = 0
            break
        elif "talk" in loc9 or "speak" in loc9 or "interact" in loc9:
            print("""\"I will think of a number and give you 5 tries to guess it. 
If you haven't guessed the number after those 5 tries, you will not leave this mountain.\"""")
            for counter in range(5):
                yetiquestion = input("Guess what number the Yeti is thinking about: ")
                if yetiquestion.isdigit():
                    yetiquestion = int(yetiquestion)
                    if number < yetiquestion:
                        print("Too high.")
                    elif number > yetiquestion:
                        print("Too low.")
                    else:
                        print("""\"I can't believe it, you actually guessed my number. 
I always keep my word, you may continue on your journey and I will not bother you anymore."
You pass by the Yeti, and you look like a human geyser with the amount of sweat evaporating from your body.
Atleast you take some solace in the fact the worst is most likely now over, and continue on.""")
                        question = 11
                        break
                else:
                    print("Give me a whole number, this will still count as a guess by the way.")
            else: 
                print(f"""You failed to guess the number in the amount of tries given.
The yeti laughs: "You fool, the number was {number}. I am going to enjoy this.
You try to run away, but before you took even a single step, the Yeti grabbed you by the head and crushed it like a melon.""")
                question = 0
                break 


if question == 10: 
    print("""You narrowly escaped the Yeti's cruel tricks, and now stand near the peak of the mountain.
As the dwarf said, the peak has shifted and the "road" you followed has been blocked by a gigantic pack of snow.
You surely won't cross this, and you don't see any other way to get to the peak.
Finally your mind catches up with you, and you remember the items the dwarf gave you. Maybe that amulet works here.
Infront of you is a big mountain wall, and to the right is the snow that impossible to cross.""")

while question == 10:
    loc10 = input("What do you do?: ")
    if loc10 == "inventory" or loc10 == "check inventory":
        if playerinv == "":
            print("You have nothing in your inventory")
        else:
            print("Inventory\n********")
            print(playerinv)
    elif loc10 == "look at wall" or loc10 == "inspect wall" or loc10 == "observe wall" or loc10 == "wall":
        print("It just looks like a regular mountain side to you. Even when you touch the wall physically, nothing seems off.")
    elif loc10 == "look at snow" or loc10 == "inspect snow":
        print("""The huge pack of snow blocks anything trying to cross it. So tightly packed it might aswell be an iron sheet.
You aren't a bad climber, but even this one would be impossible for you.""")
    elif loc10 == "use amulet on wall" or loc10 == "hold amulet to wall" or loc10 == "use amulet with wall":
        print("""You decide to hold the amulet next to the wall, hoping the dwarf told you the truth. 
Luckily, not long after the wall seems to shift, twist and turn before it completely dissapears from view.
You now see a grand hallway, made out of beautiful stonework with dwarven architecture.
Without hesitating, you enter the hallway.""")
        question = 11
        break


if question == 11:
    print("""After walking trough the grandiose hallway for what seems an eternity, you come across a large inner sanctum.
The sactum is very detailed and ornamented, however there is not much of use in there except for a large central elevator.""")
    while question == 11:
        loc11=input("What do you do?: ")
        if loc11 == "inventory" or loc11 == "check inventory":
            if playerinv == "":
                print("You have nothing in your inventory")
            else:
                print("Inventory\n********")
                print(playerinv)
        if "approach" in loc11 or "inspect" in loc11 or "enter" in loc11 and "elevator" in loc11:
            print("""You approach the elevator, it is large and radial. 
In the middle of the elevator platform there is a small floor stand with a keyhole slot. The stand doesn't reach higher than your hips.
There is also a large mechanical button on the side of the stand.""")
            while "approach" in loc11 or "inspect" in loc11 or "check" in loc11 or "enter" in loc11 and "elevator" in loc11:
                elevatorquestion = input("What do you do at the elevator: ")
                if "ride" in elevatorquestion and dwarfkey == 0 or "use button" in elevatorquestion and dwarfkey == 0\
                or "press button" in elevatorquestion and dwarfkey == 0:
                        print("""You press the large mechanical button on the side of the stand, the elevator starts rising up slowly.
It looks like it hasn't been used for a while, you have to dodge some small debris that gets shaken loose during the ascent.
After a while of ascending, the elevator comes to a stop. You get dropped off at another dwarven sanctum inside the mountain.
This time it is alot smaller, however. You leave the sanctum and approach the peak of the mountain.""")
                        question = 12
                        loc11 == ""
                        break
                elif "use key" in elevatorquestion and dwarfkey == 1 or "activate" in elevatorquestion and dwarfkey == 1:
                    print("""You insert the dwarven key into the keyhole, the elevator immediately reacts and starts running.
The elevator shakes and vibrates so violently you are nearly knocked off your feet. You assume you now need to press the button to make it go up.""")
                    dwarfkey = 0
                    inventory.remove("Dwarven Key")
                elif "ride" in elevatorquestion and dwarfkey == 1 or "use button" in elevatorquestion and dwarfkey == 1\
                or "press button" in elevatorquestion and dwarfkey == 1:
                    print("""You try to use the button on the side, however the elevator is still dormant and nothing happens. 
You should try to use your key first.""")

    
if question == 12:
  print("""After leaving the sanctum, the chill nearly freezes you solid.
You have finally reached the summit after all your hardships, and continue to walk to the highest peak.
There, on the peak you see the thing you came all this way for. The flag that will complete your trial."""
        )
  while question == 12:
    loc12 = input("What do you do?: ")
    if loc12 == "inventory" or loc12 == "check inventory":
      if playerinv == "":
        print("You have nothing in your inventory")
      else:
        print("Inventory\n********")
        print(playerinv)
    elif ("inspect" in loc12 or "approach" in loc12 or "go to" in loc12
          or "look at" in loc12) and "flag" in loc12:
      print("""You approach a slightly frozen line of flags on top of the peak.
The flag is next to alot of other flags in a row, all hung from a line. You can see a few ripped off by previous villagers.
""")
    while True:
      flagquestion = input("What do you do with the flag?: ")
      if "grab" in flagquestion or "take" in flagquestion or "get" in flagquestion or "rip off" in flagquestion:
        print(
          "You rip a flag right off the line, and stash it in your backpack.")
        inventory.append("Flag")
        playerinv = "\n".join(inventory)
        flag = 1
        question = 0
        epilogue = 1
        break

 
        




        
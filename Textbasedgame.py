# items
doorkey = 0
chart = 0
oxygentank = 0
flare = 0
axe = 0
planks = 0
jewel = 0
amulet = 0
dwarfkey = 0
flag = 0

# progression
question = 1



print("""You slowly open your eyes, still feeling drowsy.
You shoot up like a rocket, remembering today is your coming of age ritual.
The ritual is not easy, every person that reaches 18 years old has to climb the sacred mountain.
However, you feel determined to press on, and get out of bed.""")

print("""You rush out bed, getting dressed in most of your climbing hear along the way.
You now stand in your room, with an old creaky door infront of you, the faintest ray of light shining trough.
To your left is an unremarkable nightstand, and behind you is the bed you just left.""")

while question == 1:
    loc1 = input("What do you do?: ").lower()
    if "open" and "door" in loc1 and doorkey == 0:
        print("You try to open the door, but it is locked.")
    elif "open" and "door" in loc1 and doorkey == 1:
        print("You use the key on the door and head outside.")
        question = 2
        break
        
    while loc1 == "look at nightstand" or loc1 == "inspect nightstand":
        print("""You see nothing on top of the nightstand except a simple lamp.
        The shoddy drawers of the stand hang loose ever so slightly.""")
        standquestion = input("What do you do with the nightstand?: ").lower()
        if "nightstand" and ("open" or "look in") in standquestion:
            print("""You open the nightstand's loose drawers and find a familiar key inside.
            This is your house key.""")
            keyquestion = input("What do you do with the key?: ").lower()
            if ("grab" or "take") and "key" in  keyquestion: 
                print("You grab your house key.")
                doorkey = 1
                loc1 = ""
                continue
            elif keyquestion == "go back" or keyquestion == "leave":
                continue
            else: print("You can't do that right now.")
        elif standquestion == "look at lamp" or standquestion == "inspect lamp":
            print("It is just a lamp.")
        elif standquestion == "leave" or standquestion == "go back":
            loc1 = ""
            continue
            
        else: print("I don't know that command.")

while question == 2:
  loc2 = input()


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

# progression
question = 1
prologue = 1
counter = 0


print("""You slowly open your eyes, still feeling drowsy.
You shoot up like a rocket, remembering today is your coming of age ritual.
The ritual is not easy, every person that reaches 18 years old has to climb the sacred mountain.
However, you feel determined to press on, and get out of bed.""")

while prologue == 1:
    print("""You rush out bed, getting dressed in most of your climbing hear along the way.
    You now stand in your room, with an old creaky door infront of you, the faintest ray of light shining trough.
    To your left is an unremarkable nightstand, and behind you is the bed you just left.""")
    prologue = 0

while question == 1:
    loc1 = input("What do you do?: ").lower()
    if "open" and "door" in loc1 and doorkey == 0:
        print("You try to open the door, but it is locked.")
    elif "open" and "door" in loc1 and doorkey == 1:
        print("You use the key on the door and head outside.")
        question = 2
        break
      
    elif "nightstand" and "look" or "inspect" or "check" in loc1:
        print("""You see nothing on top of the nightstand except a simple lamp.
        The shoddy drawers of the stand hang loose ever so slightly.""")
        standquestion = input("What do you do?: ").lower()
        counter = 1
        if "nightstand" and ("open" or "look in") in standquestion:
            print("""You open the nightstand's loose drawers and find a familiar key inside.
            This is your house key.""")
            keyquestion = input("What do you do?: ").lower()
            if ("grab" or "take") and "key" in  keyquestion: 
                print("You grab your house key.")
                doorkey = 1
                continue
        elif standquestion == "look at lamp" or standquestion == "inspect lamp":
            print("It is just a lamp.")

print("You unlock the front door and swing it open, as you're standing there you feel a slight breeze from the cold mountain air")
print("You see an old wise man sitting by a chopped tree with the montain range behind him, There's an oxygen tank laying beside him ")

while question == 2:
  loc2 = input("What do you do")
    

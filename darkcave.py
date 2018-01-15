from random import *
import time
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
#NOTES
#print(.GREEN + "Hello World") Color text
#print (Style.RESET_ALL) Reset text
#print ('Hello World !' ) Bold text
#TODO
#Unicorns
menu = True
print ("> Welcome to the Dark Cave!\n")
print ("> Type S to start" )
print ("> Type I for info" )
print ("> Type U for update info")
print ("> Type Q to quit" )
choice = input (">>> ")
while menu == True:
  if choice == "S":
    print ("Start Game Selected")
    menu = False
  elif choice == "I":
    print ("The Dark Cave: Created by DaveedDigs")
    print ("Get ready for an awesome RPG game made to look old and also very cool!\n**Notice: Starting game after prompt!**")
    input ("Press enter to start > ")
    menu = False
  elif choice == "U":
    print ("Update info: Last Updated 01/15/18")
    print ("> Released OP version 1.1\n> Released DAL version D.1.2\n> Removed DEV and ALPHA versions to reduce code bugs and to increase productivity\n> Started accepting personal requests for versions 1.1+ and DAL D.2.0\n Added 2 death endings")
    print ("<<Future Update Info>>\n> More endings to win or die\n> Pictures to go along with scenarios")
    print ("Requests to be/that are implemented: ACCEPTING REQUESTS\n> Unicorns! Requested by: Nat and Kel! ANNOUNCED: D.1.1")
    input ("Press Enter To Continue")
    menu = False
  elif choice == "Q":
    print("Exiting Dark Cave!")
    exit()
  else:
    print ("Error > Please type in S, I, U, or Q!")
    choice = input ("> ")
print ("Starting Game... ")
print ("OP Mode Selected")

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#     Game starts here      |
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/

health = 10
hunger = 10
thirst = 10
courage = 5
sanity = 7
print ("Game > The game has been loaded!")
input ("\nPress Enter to start...\n")
print ("You > 'Ugh. Where am I?'")
input ("")
print ("Game > A blinding light flashes in your eyes as you feel the trickle of water from a nearby stream run down your face. You find yourself lying on a cold rock deep down. Unable to move much because of your body aching all over, you look to the side where you see a pitch black cave area.")
input ("")
print ("Game > You hear a sound much like a horse down in the cave. It's almost like it's coming closer to you as you ask yourself why you are down in here in the first place. Although you can hear the noise, you can't quite make out the exact creature that is making that noise")
input ("")
print ("Game > After a while, you finally make the effort to stand up. You don't hear anything else except the birds chirping in the forest above.")
input ("")
choice = input ("Game > You wonder if you should take a risk into the dark cave. Type Y to explore the cave or N to stay here!\n\n> ")
valid = True
while valid == True:
  if choice == "Y":
    courage += 1
    sanity = sanity/2
    print ("Game > You bravely enter the dark area of the cave, wondering what is in the pitch black area. You want to survive, so you might as well try to find food and water. Sounds around you start to annoy you as you walk further into the cave. It's almost as... they are watching you.\n")
    print ("Status > +1 Courage [Your courage is now " + str(courage) + "]")
    print ("Status > -Half of your Sanity [Your sanity is now " + str(sanity) + "]")
    valid = False
  elif choice == "N":
    courage -= 2
    sanity -= 2
    health -= 4
    print ("Game > You decide to stay behind waiting for someone to notice that you are gone. As you wait, you kick the wall in frustration and rocks from above fall down. They hit you in the head and knock you out.\n")
    print ("Status > -2 Courage [Your courage is now " + str(courage) + "]")
    print ("Status > -2 Sanity [Your sanity is now " + str(sanity) + "]")
    print ("Status > -4 Heath [Your health is now " + str(health) + "]")
    valid = False
    input ("")
  else:
    print ("Error > Please type in Y or N!")
    choice = input ("> ")
    
if choice == "Y":
  input ("")
  print ("Game > You are getting very scared as you walk further into the cave. Darkness starts to surroud you like a pool of water. It's getting colder and colder as the light fades away. You hear that horse sound you just heard earlier. You walk in the direction that the sound came from. Of course with your luck, this is the exact opposite way of the light.")
  input ("")
  print ("Game > You start to wonder if this is a good idea when suddenly this raindowish creature appears out of the dark. You believe that this is where the sound came from so you use your best judgement to identify the creature.")
  input ("")
  print ("You > 'Good horsey...'")
  input ("")
  print ("??? > Nheheheh")
  input ("")
  choice2 = input ("Game > It seems to be waiting for you to identify it correctly. Type what it is! (Please type all letters in capital)\n")
  if choice2 == "UNICORN":
    sanity += 1
    courage += 2
    trust = 1
    print ("By its delighted expression, you must've gotten it correct. You feel acomplishment as it throws you on its back. You feel safer and more stable!\n")
    print ("Status > +2 Courage [Your courage is now " + str(courage) + "]")
    print ("Status > +1 Sanity [Your sanity is now " + str(sanity) + "]")
    print ("Status > [Special] Trust from pink named creatures")
    #+1 sanity
    #+2 courage
    #+Possible army of Tems --Request--
  else:
    print ("Game > The creature backs away in horror as you identified it. It seems to be that it hides in the dark. As it disappears, you get a sick feeling in your stomach.")
    input ("")
    print ("Game > A bunch of creatures come out of the dark, but the creature is no where to be seen. You feel where that sick feeling comes from when you see the demon eyes on them. A storm is brewing!")
    input ("")
    print ("??? > 'ARGHGHGH'")
    input ("")
    print ("Game > After a short battle of you harmlessly whapping the creatures, you finally lay down, and take your final look at the world.\n")
    time.sleep(1)
    print ("                  GAME OVER                  ")
    print (" 'Those little creatures wouldn't let you go'")
    exit()
elif choice == "N":
  print ("Game > After those hard hits on the head by the rocks, you seem a bit hungry. You see a tree branch up above that has berries on it. It looks close enough that you can reach it by climbing up the rocks. Still not enough to get out but you need food to survive.")
  surviven = randint(1, 2)
  input ("")
  survivei = input ("Game > Will you take the risk of grabbing the berries to replenish your hunger? (Your hunger is at 5) Type 1 for a chance to get up, 2 for a chance to get up, and N to stay down:\n> ")
  thirst == 7
  if str(survivei) == str(surviven):
    print ("Game > You jump up to the berries pulling on branches to get up. As you start picking berries from the branch, you can see there is enough to replenish your hunger.\n")
    hunger = 10
    thirst += 2
    print ("Status > +5 Hunger [Your hunger is now " + str(hunger) + "]")
    print ("Status > +2 Thirst [Your thirst is now " + str(hunger) + "]")
    if hunger == 10:
      print ("Status > Your hunger has been replenished!")
      input ("")
    else:
      input ("")
  elif survivei == "N":
    print ("Game > Cowardly actions overpower you as you back away from underneath the berries. You wonder if that was the right choice as you sit on the side of the cave, super hungry and thirsty.\n")
    sanity -= 2
    courage -= 2
    thirst -= 2
    hunger = 2
    print ("Status > -3 Hunger [Your hunger is now " + str(hunger) + "]")
    print ("Status > -2 Thirst [Your thirst is now " + str(hunger) + "]")
    print ("Status > -2 Courage [Your courage is now " + str(hunger) + "]")
    print ("Status > -2 Sanity [Your sanity is now " + str(hunger) + "]")
    print (str(surviven))
    print (str(survivei))
  else:
    print ("Game > As you try to jump up to where the berries are sitting, your foot slips on a wet rock. As you fall down from a height, your life flashes be your eyes. You hit the cold hard ground, breathing heavily, you close your eyes trying to avoid the pain.")
    input ("")
    print ("You feel your last moments creeping up to you...")
    time.sleep(2)
    print ("             GAME OVER             ")
    print (" 'Better footwork is the key' ")
    exit()
    print (str(surviven))
    print (str(survivei))
  
  
  
  
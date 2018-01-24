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
#Tem Army
menu = True
print ("> Welcome to the Dark Cave!\n")
print ("> Type S to start" )
print ("> Type I for info" )
print ("> Type U for update info")
print ("> Type Q to quit" )
choice = input ("> ")
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
    print ("**Please go to the GitHub to get updates as they come! https://github.com/HDLOfficial/Dark-Cave")
    input ("Press Enter To Continue")
    menu = False
  elif choice == "Q":
    print("Exiting Dark Cave!")
    exit()
  else:
    print ("Error > Please type in S, I, U, or Q!")
    choice = input ("> ")
print ("Starting Game... ")
print ("\nNOTICE: PLEASE READ THE GITHUB WIKI FOR INFO AND NO CONFUSION ABOUT THE GAME! THERE MAY BE RANDOM EVENTS THAT WILL HAPPEN THAT WILL CHANGE EVERY SINGLE GAME!\n")
input ("")

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
    print ("Game > By its delighted expression, you must've gotten it correct. You feel acomplishment as it throws you on its back. You feel safer and more stable!\n")
    print ("Status > +2 Courage [Your courage is now " + str(courage) + "]")
    print ("Status > +1 Sanity [Your sanity is now " + str(sanity) + "]")
    print ("Status > [Special] Trust from mythical creatures")
    #+1 sanity
    #+2 courage
    #+Possible army of Tems --Request--
    input ("")
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
    print ("Status > -2 Thirst [Your thirst is now " + str(thirst) + "]")
    print ("Status > -2 Courage [Your courage is now " + str(courage) + "]")
    print ("Status > -2 Sanity [Your sanity is now " + str(sanity) + "]")
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
#                                              #
#----------------------------------------------#
# After Y/N choice has been made - continue on #
#----------------------------------------------#
#                                              #

if choice == "Y":
  hunger = 4
  print ("Game > You continue walking into the dark cave. It's getting more humid as you go farther in!")
  input ("")
  print ("You > 'It's too dark and humid to keep trotting along. But if I stop here, I may starve'")
  input ("")
  choice2 = input ("Game > You can either stop for safety, or keep going to find food. Type S to stop here and type G to keep going.\n> ")
  if choice2 == "S":
    print ("Game > You decide to stop to avoid running into more trouble. You get off the unicorn and sit on the cold stone ground. You feel a sharp object underneath you. As you get up and shine your phone towards it, you see that it's a locked bag.\n")
    hunger -= 1
    courage -= 1
    print ("Status > -1 Courage [Your courage is now " + str(courage) + "]")
    print ("Status > -1 Hunger [Your courage is now " + str(hunger) + "]")
    input ("")
    bag = input ("Do you want to open the bag even though it may hurt your fingers trying to pry it open? Type Y to open it and N to leave it be.\n> ")
    if bag == "Y":
      health -= 2
      print ("Game > You pry the bag open with your fingers, you feel a small pain in your fingers.\n")
      print ("Status > -2 Health [Your health is now " + str(health) + "]")
      input ("Press enter to open the bag\n")
      fsupply = 1
      wsupply = 1
      knife = 1
      print ("Item > Bread 'A little moldy on the outside'")
      print ("Item > Bottled Water 'Mmmm... Warm water'")
      print ("Item > Butter Knife 'Still a little buttery'")
      hunger += 3
      print ("Status > +3 Hunger [Your hunger is now " + str(hunger) + "]")
      ##Add health and also thirst
      input ("")
    print ("Game > You sit in this place for what seems like hours, even though it is just 5 minutes. You hear another sound in the distance as your phone light flickers out.")
    input ("")
    print ("??? > YaYA")
    input ("")
    print ("You > 'What is that... Ehh, it must be my imagination'")
    input ("")
    print ("Game > Minutes pass one by one and you can't keep your mind off of that sound that came. You start to feel worried, biting on side of the bag.")
    input ("")
    print ("??? > YaH")
    input ("")
    print ("Game > A creature comes out of the darkness only to pass you, go back into the darkness, and scare the heeby geebies out of you. You don't know whether to attack it, or leave it be.")
    input ("")
    choice3 = input ("Type A to attack or P to leave it be\n> ")
    if choice3 == "P":
      print ("Game > You decide to leave it be, but your pet unicorn runs into the darkness to the creature.")
      input ("")
      print ("Game > You see sparks in the distance. You can't see what is making the sparks.")
      input ("")
      choice4 = input ("Do you want to run in the other direction, or find out what the sparks are from? (Type R to run or I to find out)\n> ")
      event = randint(1, 2)
      if str(event) == "1" and choice4 == "R":
        print ("Game > You try to run, but falling crush you as you run. You try to regret your choice as you are being turned into a breakfast food.")
        time.sleep(2)
        print ("        GAME OVER        ")
        print (" '*Just a random event*' ")
        exit()
      elif str(event) == "2" and choice4 == "R":
        print ("Game > You run, leaving your pet unicorn behind. You just need to survive. A guilty feeling overtakes you, as you fall down on the group breathing heavily.")
        courage -= 2
        sanity -= 2
        print ("Status > -2 Courage [Your courage is now " + str(courage) + "]")
        print ("Status > -2 Sanity [Your sanity is now " + str(sanity) + "]")
        ##Continue
      elif str(event) == "1" and choice4 == "I":
        health -= 3
        print ("Game > You slowly creep forward to the sparks. A bat comes from the darkness and slaps you in the head. You fall to the cold ground, with an aching pain on the side of your cheek.")
        print ("Status > -3 Health [Your health is now " + str(health) + "]")
        input ("")
        print ("Game > With that bat scaring you, you decide to leave the area.")
      elif str(event) == "2" and choice4 == "I":
        print ("Game > You creep closer and closer to the place where the sparks came from. Another bunch of sparks explodes closer than you think they did before. You see your pet unicorn, fighting this creature, which is still undescribable to you.")
        input ("")
        print ("Game > As a person who doesn't like violence, you want to tame the new creature. ")
        input ("")
        print ("Game > You feel like you want to try what you did before with the unicorn to tame it, but you don't have any idea what this thing is. You decide to do what all people would do in meeting something.")
        input ("")
        print ("You > 'Um, Hi?'")
        input ("")
        print ("It looks at you in confusion. Maybe it doesn't speak English. The creature looks like it is going to say something.")
        input ("")
        print ("??? > HoOmAN?")
        input ("")
        print ("Game > You think it's saying 'human?' but you are not too sure since you are tired.")
        input ("")
        print ("??? > TeM. TeM mEeT HoOmAN.")
        input ("")
        print ("Game > You feel very scared that this creature thing, calling itself tem, it actually communicating with you. You very carefully back away inch by inch. It steps forward as you move back.")
        tame = input ("Game > Try to do the same as you did with the unicorn, by identifing it.\n> ")
        if tame.lower() == "tem":
          print ("Game > The creature, known as tem, looks happy! You're 2 for 2 today!")
          input ("")
          print ("Game > You let out a sigh of relief. Your unicorn and a tem is here. It can't get much weirder than this for you.")
          input ("")
          print ("Game > The tem speaks to you again in its high pitched voice.")
          input ("")
          print ("Tem > HoOmAN sTUcK. TeM cAN hElP.")
          input ("")
          print ("Game > Once again, you feel weird talking to a creature, but it may be your only way out.")
          time.sleep(1)
          print ("Status > [Special] Tem")
          input ("")
          print ("You > Ok...")
          input ("")
          print ("Game > You wait as the 'Tem' runs back into the darkness.")
          input ("")
          print ("Game > Time passes and you still don't see the 'Tem' again.")
          input ("")
          print ("Game > You hear a sound, then more sounds, then lots more sounds surrounding you.")
          input ("")
          final = input ("Game > Do you want to hide or face all of the sounds that seem to be coming to you? (Type H to hide and F to face the sounds)\n> ")
          if final == "H":
            print ("Game > You scramble to find a hiding place. You feel safer that you are not in danger anymore from the many sounds that were coming to you.")
          elif final == "F":
            print ("Game > You decide to face the sounds coming for you, in the chance that they are friendly creatures.")
            input ("")
            rocks = randint(1,2)
            if str(rocks) == "1":
              print ("Game > You finally see the first glances of the creatures. You see that it is a 'tem', and another 'tem', annnd another 'tem'. There is an army of about 50 'tems' surrounding you.")
              print ("TeMs > TeMs s...")
              time.sleep(2)
              print ("Game > Right as the 'tems' start to speak, rocks from above crush you!")
              print ("TeMs > NuuUuU")
              time.sleep(2)
              print ("      GAME OVER       ")
              print ("   'Random Events!'   ")
              exit()
            elif str(rocks) == "2":
              print ("Game > You finally see the first glances of the creatures. You see that it is a 'tem', and another 'tem', annnd another 'tem'. There is an army of about 50 'tems' surrounding you.")
              input ("")
              print ("TeMs > TeMs sAVe!!!")
              input ("")
              print ("Game > The 'tems' move closer to you. You now feel very worried and scared. Are they actually helping you?")
              input ("")
              print ("Game > They suddenly leap forward to you. Normally you would shreak, but you feel trust in these creatues.")
        else:
          print ("Incorrect")
          ##Continue
    elif choice3 == "A":
      if bag == "Y":
        print ("Game > You grab your water bottle and slash the creature across the face, its head turning on impact.")
        input ("")
      else:
        print ("Game > You whap the creature in the face with your hand, trying to hurt it. Its head turns on impact.")
        input ("")
      print ("Game > It turns back to face you, its smile still plastered on its face. You can still see it's white fur bristle.")
      time.sleep(1)
      print ("Game > Then, without warning, it screams.")
      input ("")
      print ("??? > TeMs")
      time.sleep(1)
      print ("??? > BAkuP")
      input ("")
      print ("Game > Out of the darkness, shapes appear and begin to creep towards you. They step out of the shadows, revealing 50 more of these assumed 'Tems'.")
      input ("")
      print ("Game > You step back, sweating, to hear a warning snarl. Turning to look behind you, you see around 50 more closing in on you.")
      input ("")
      print ("Game > Glancing around, you see no escape.")
      input ("")
      print ("TeM > HooMaN No GuD *growls*")
      input ("")
      print ("TeM > TeMs!!!")
      time.sleep(2)
      print ("TeM > Atak!!!")
      input ("")
      print ("The Tems swarm forward, leaping and climbing over each other to get to you.")
      input ("")
      print ("Soon, you can hardly see over all the Tems on you, pulling you to the ground. The scratching and biting becomes too much and the white fur blurs together to make a blinding light.")
      time.sleep(1)
      print ("        GAME OVER        ")
      print ("   'NeVr hit a TEM!!!'   ")
      time.sleep(2)
      print ("")
      print ("Shoutout to Nat (Tem) for making this ending! :3")
      exit()

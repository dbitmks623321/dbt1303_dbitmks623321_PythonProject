#This is a text-based interactive adventure game with all outcomes relying on the users choices

import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sword = 0
fooddish = 0

required = ("\nUse only A, B, or C\n") #To Reduce duplication of choices

#The story is broken into sections, starting with "intro"
def intro():
  print (" ------------W E L C O M E   TO  S U R V I V O R------------- \n\nAfter a day hiking in the forest with your friends, you decide "
  "to wander further into the forest by yOurself to enjoy the serene enviroment by yourself." 
  "\nYou sit by a tree and fall asleep. You wake up in the evening with the sun almost setting, "
  "and no sign of your friends. \nAll of a sudden you hear a roar behind you and see a lion running towards you!"
  "\nWhat will you do?:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the lion
  B. Lie down and wait to be mauled
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWell, that was stupid! "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe lion is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou pick up another rock, as if the first " 
    "rock thrown did much damage.\nYou panic and miss!\nThe rock flew well over the Lion!\n"
     "\nYou died!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark. "
  " Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? really!"
    "You do know Lions can see very well in the dark right?"
    "You died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou lay in wait. You get on a rock near the cave entrance "
    "and wait for the lion who thought you were no match. \nAs he walked "
    "closer and your heart skips rapidly as you leap on to it\n"
    "thrusting the sword in it multiple times until it falls down dead!\na"
    "\nCongratulations! You survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the Lion enters the dark cave, you silently "
    "sneak out. You're several feet away, \nbut the lion smells you and turns "
    "to see you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the Lion's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an Lion. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. \nYou quickly reach down and grab it, "
  "as you run frightened but panic and miss. \nYou try to calm your "
  "heavy breathing as you hide behind a building, waiting for the \nlion to come charging around the corner."
  "\n You notice a half eaten food dish "
  "in a trash can next to you. \n\nDo you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    fooddish = 1 #adds a fooddish
  else:
    fooddish = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending Lion!.")
  time.sleep(1)
  if fooddish > 0:
    print ("\nYou quickly throw the food dish to it, somehow "
    "hoping it will stop the Lion. It does! The Lion just wanted a snack! "
    "\n\nYou slip away while it munches away!"
    "You survived!")
  else: #If the user didn't grab the fooddish
     print ("\nMaybe you should have picked up the food dish. "
     "\n\nYou died!")


intro()

print('''
*******************************************************************************
                              _.-.
                             /  99\
                            (      `\
                            ||   ,  ,|
                    __      | v_____/
              ,.--"`-.".   /   `---'
          _.-'          '-/      |
      _.-"   |   '-.             |_/_
,__.-'  _,.--\      \      ((    /-\
',_..--'      `\     \      ((_ /
                `-,   )      |(' 
                  |   |-.,,-" (  
                  |   |   `\   `',_
                  )    \    \,(\(\-'
                  \     `-,_
                   \_(\-(\`-`
*******************************************************************************
''')

print("Welcome to ~Shama's ARK Escape~.\n")
print("Your mission is to get home from the woods without getting caught by dinosaurs.\nThen stop playing and go eat dinner with your family.\n\nThey miss you.\n")
loud_noise = input("You're in the woods heading home while rocking some prehistoric Heelys.\nYou hear a loud roar up ahead.\nDo you go towards it?\nYes or no: ")
if loud_noise.lower() == "no":
  print("You die by playing without risks.\nGame Over.")
elif loud_noise.lower() == "yes":
  dino = input("\nYou go towards the noise.\nIt's a dinosaur! AAAAAAA\nDo you run or hide? ")
  if dino.lower() == "run":
    print("\nThe dinosaur spots you running and chases.\nYou get gobbled like a turkey.\nGame Over.")
  elif dino.lower() == "hide":
    path = input("\nThe dinosaur walks away while you hide behind bushes.\nYou see your house in the distance!\nYou start walking towards it but there's three paths left to your house.\nThe left path is filled with tall grass.\nThe right path has another house in the distance you haven't seen before.\nThere's also a Decepticon that just rolled out in front of your home.\nDo you go left, right, or skrt past the Decepticon with your prehistoric Heelys?\nLeft, right, or skrt: ")
    if path.lower() == "left":
      print("\nYou walk through the tall grass.\nYou're almost to the end when suddenly, you open a patch of grass to a T-Rex!\nGame Over.")
    elif path.lower() == "right":
      print("\nYou walk over to the random house you haven't seen before.\nYou open the door without knocking, which was a bad move!\nYou woke up May in her own home!\nMay chases you out of her home and feeds you to her pet dinosaur you hid from earlier.\nGG, May wins.")
    elif path.lower() == "skrt":
      print("\nYou skrt past the Decepticon like a G.\nThey can't keep up because you're too slick with it when wearing prehistoric Heelys.\nYou made it home!\nYou save your game and close it, finally ready to go eat dinner with your family. :)\nGG!")
    else:
      print("Your input is invalid. Did you type something wrong?")
  else:
    print("Your input is invalid. Did you type something wrong?")
else:
  print("Your input is invalid. Did you type something wrong?")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

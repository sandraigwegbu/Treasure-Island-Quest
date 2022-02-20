#TREASURE ISLAND QUEST
#Welcome message
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

#First choice
crossroads = input('You are at a crossroads.\nWhere do you want to go?\nType "left" or "right": ').lower()
if crossroads == "left":
  #Second choice
  lake = input('\nYou have come to a lake.\nThere is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across: ').lower()
  if lake == "wait":
    #Third choice
    door = input('\nYou arrive at the island unharmed.\nThere is a house with 3 doors. One "red", one "yellow", and one "blue".\nWhich colour do you choose?: ').lower()
    if door == "red":
      print("\nAhhh! It's a room full of fire!\nGAME OVER.")
    elif door == "blue":
      print("\nUnlucky! You enter a room full of beasts.\nGAME OVER.")
    elif door == "yellow":
      print("\nYou found the treasure!\nYOU WIN!")
    else:
      print("\nYou chose a door that doesn't exist.\nGAME OVER.")
  else:
    print("\nOh no! You were attacked by trout and you have drowned.\nGAME OVER.")
else:
  print("\nUh oh! You have fallen into a hole and broken your legs!\nGAME OVER.")


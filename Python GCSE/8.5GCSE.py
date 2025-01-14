valid_option = ['A', 'B', 'C']
inventory = []
inventoryoptions = ["p","a","g","q"]

def menu():
  print("\t\tGame Menu\n")
  print("\t\tA - Enter Name\n\t\tB - Play Game\n\t\tc - Quit")
  
  selection = input("Please enter your choice:\t").upper()
  while selection not in valid_option:
    print("That is not a valid choice")
    selection = input("Please enter your choice:\t").upper()
  print("That is a valid choice")
  return selection

def main():
  selection = menu()
  if selection == valid_option[0]:
    name = input("Please enter your name:\t")
    print(f"Welcome, {name}")
    main()

  if selection == valid_option[1]:
    print("Game is starting...")
    game()
    
  if selection == valid_option[2]:
    print("Thank you for playing!")

def game():
  x=(len(inventory)-1)
  optionsmenu = input("******Options Menu******\nEnter 'p' to print inventory\nEnter 'a' to add item to inventory\nEnter 'g' to get item out of inventory\nEnter 'q' to quit\n>>> ")
  if optionsmenu == inventoryoptions[0]:
    if len(inventory) == 0:
      print("You have nothing in your inventory...")
      game()
    else:
      print(inventory)
      game()
  elif optionsmenu == inventoryoptions[1]:
    additem = input("Please input an object to add to your inventory:\t")
    inventory.append(additem)
    game()
  elif optionsmenu == inventoryoptions[2]:
    if len(inventory) != 0:
      for i in inventory:
        print(f"{inventory[x]} - {x}")
        if x != 0:
          x=x-1
      removeitem = int(input(f"Please pick the number that represents your item that you would like to remove (pick between 0-{len(inventory)-1})\n>>> "))
      inventory.remove(inventory[removeitem])
      game()
    else:
      print("There is nothing in your inventory...")
      game()
  elif optionsmenu == inventoryoptions[3]:
    main()

main()
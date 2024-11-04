cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter the name of your cat: ")
cat_colour = input("Enter the colour of your new cat ")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats 4. Feed it 5. Put it to sleep 6. exit game ")

    if option == '1':
        # change the cat's attributes here
       if cat_attributes['energy'] < 5:
          print(str(name)+" is too tired to play")
       else:
          cat_attributes["energy"] -=10
          cat_attributes["intelligence"]+=5
          print("You played with " + str(name))
    elif option == "2":
        if cat_attributes["energy"]<5:
           print(str(name) + " is too tired to play")
        else:
            cat_attributes["intelligence"]+=10
            cat_attributes["energy"]-=10
    elif option == "3":
        print(cat_attributes)
    elif option == "4":
        cat_attributes["energy"]+=10
        cat_attributes["weight"]+=5
        print("You fed "+ str(name))
    elif option == "5":
        cat_attributes["energy"]+=15
        cat_attributes["weight"]+=5
    elif option == "6":
        print("End of game")
        break
    else:
        print("Invalid choice. Please enter again ")

               

    # finish off the if statements below
    if cat_attributes['energy'] <= 0:
        cat_attributes["energy"] = 0
        print(str(name)+ " has no energy left, you cannot play with your cat. ")
    else:
        print(str(name) + " has enough energy to continue ")

    # elif ...
    
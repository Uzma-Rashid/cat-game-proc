class Cat:
    #the constructor:
    #the constructor will create a cat for us in code 
    #to create a cat,we need given_name and given _colour
    #self is the cat that we are creating 
    def __init__(self,given_name,given_colour):
        self.name = given_name
        self.colour= given_colour
        self.energy = 50
        self.intelligence=5
        self.weight=5
        self.age=0
    

    def train(self):
        print(f"{self.name} is training")
        self.energy -=5
        self.intelligence +=10
        self.age+=0.1

    def feed(self):
        print(f"{self.name} is eating")
        self.energy +=10
        self.weight +=1
        self.age+=0.1

    def play(self):
        print(f"{self.name} is playing")
        self.energy -= 5
        self.age += 0.1

    def sleep(self):
        print(f"{self.name} is sleeping ")
        self.energy +=5

#sid = Cat("sid", "black")
#mista = Cat("mista", "white")

#sid.train()
#print(sid.intelligence)
#print(mista.intelligence)




print("Welcome to my cat game ")
name = input("Enter a cat name ")
colour = input("Enter a colour ")


my_Cat=Cat(name,colour)
while True:
    action = input("what would you like to do 1. train 2. feed 3. play 4. sleep 5. show stats 6. end game ")
    if action == "1":
        my_Cat.train()
    elif action == "2":
        my_Cat.feed()
    elif action == "3":
        my_Cat.play()
    elif action == "4":
        my_Cat.sleep()
    elif action == "5":
        print(f"\nCurrent stats for {my_Cat.name}:")
        print(f"Colour:  {my_Cat.colour}")
        print(f"Intelligence {my_Cat.intelligence}")
        print(f"Energy {my_Cat.energy}")
        print(f"Weight {my_Cat.weight}:")
        print(f"Age {my_Cat.age:1f}\n")
    elif action == "6":
        print("End of game")
        break
    else:

        print("Invalid choice ")
    
    if my_Cat.energy <0:
        my_Cat.energy = 0
        print(f"{my_Cat.name} has no energy left")









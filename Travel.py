import ast, random

cities_text = open("Cities.txt", "r")
Cities = cities_text.readlines()
del Cities[0]
for city in Cities:
    Cities[Cities.index(city)] = ast.literal_eval(city)
cities_text.close()

class TravelClass:

    #Get's players location and tells you if you are in a city
    def get_location(self):
        print("You are currently at: "  + str(self.x) + "," + str(self.y))
        for city in Cities:
            if self.x == city[1] and self.y == city[2]:
                print("You are in " + city[0])

    #look at the map
    def map(self, player):
        have_map = False
        for item in player.inventory:
            if "Map" in item:
                have_map = True
                for city in Cities:
                    print(city[0] + " = " + " (" + str(city[1]) + "," + str(city[2]) + ")")
        if have_map == False:
            print("You need a map to check it")
    #Methods for moving East, West, North, South
    def move(self):
        choice = input("Which direction would you like to move in:\n- East\n- West\n- North\n- South\n>>")
        #Player chooses direction and if it isn't valid it will except or else
        if choice.lower() == "east":
            try:
                amount = int(input("How many units do you want to move East?\n>> "))
                if amount + self.x > 100:
                    print("Out of bounds")
                else:
                    self.x += amount
                    print("You are now at: " + str(self.x) + "," + str(self.y))
            except ValueError:
                print("Use a number")


        elif choice.lower() == "west":
            try:
                amount = int(input("How many units do you want to move West?\n>> "))
                if self.x - amount < 0:
                    print("Out of bounds")
                else:
                    self.x -= amount
                    print("You are now at: " + str(self.x) + "," + str(self.y))
            except ValueError:
                print("Use a number")


        elif choice.lower() == "north":
            try:
                amount = int(input("How many units do you want to move North?\n>> "))
                if self.y + amount > 100:
                    print("Out of bounds")
                else:
                    self.y += amount
                    print("You are now at: " + str(self.x) + "," + str(self.y))
            except ValueError:
                print("Use a number")

        elif choice.lower() == "south":
            try:
                amount = int(input("How many units do you want to move South?\n>> "))
                if self.y - amount < 0:
                    print("Out of bounds")
                else:
                    self.y -= amount
                    print("You are now at: " + str(self.x) + "," + str(self.y))
            except ValueError:
                print("Use a number")

        else:
            print("\n\tINVALID CHOICE\n")
            self.move()
                  

    #Methods for looking in a particular direction
    def look(self):
        choice = input("Which direction would you like to look in:\n- East\n- West\n- North\n- South\n>>")
        if choice.lower() == "east":
            count = 0
            for city in Cities:
                if self.y == city[2]:
                    if city[1] > self.x:
                        print("There's a city " + str(city[1] - self.x) + " units east.")
                        count += 1

                    else:
                        pass

                else:
                    pass

            if count == 0:
                print("\nThere's nothing East")
            

        elif choice.lower() == "west":
            count = 0
            for city in Cities:
                if self.y == city[2]:
                    if city[1] < self.x:
                        print("There's a city " + str(self.x - city[1]) + " units west.")
                        count += 1

                    else:
                        pass

                else:
                    pass

            if count == 0:
                print("\nThere's nothing West")

        elif choice.lower() == "north":
            count = 0
            for city in Cities:
                if self.x == city[1]:
                    if city[2] > self.y:
                        print("There's a city " + str(city[2] - self.y) + " units north.")
                        count += 1

                    else:
                        pass

                else:
                    pass

            if count == 0:
                print("\nThere's nothing North")
                      

        elif choice.lower() == "south":
            count = 0
            for city in Cities:
                if self.x == city[1]:
                    if city[2] < self.y:
                        print("There's a city " + str(self.y - city[2]) + " units south.")
                        count += 1

                    else:
                        pass

                else:
                    pass

            if count == 0:
                print("\nThere's nothing South")

        else:
            print("\n\tINVALID CHOICE\n")

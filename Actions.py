import random, ast, sys

#Getting users created cities
cities_text = open("Cities.txt", "r")
Cities = cities_text.readlines()
del Cities[0]
for city in Cities:
    Cities[Cities.index(city)] = ast.literal_eval(city)
cities_text.close()

#Getting users created bosses
bosses_text = open("Bosses.txt", "r")
Bosses = bosses_text.readlines()
del Bosses[0]
for line in Bosses:
	Bosses[Bosses.index(line)] = ast.literal_eval(line)
bosses_text.close()

class ActionsClass:


    #Method for creating the enemy and then starting the fight loop
    def combat_mode(self, mob):
        print("A wild " + mob.name + " appeared! You can no longer use any idle commands and must either attack or drink a potion!")
        while mob.is_alive == True:
            choice = input(">>> ")
            if choice == "attack":
                self.attack(mob)
            elif choice == "potion":
                if self.potions > 0:
                    self.potions -= 1
                    self.hp = 10 + self.level
                    print("You drank a potion and regained your hp")
                    print("Potions Remaining: " + str(self.potions))
                else:
                    print("No Potions")
            else:
                print("You may only attack or drink a potion")


    #Combat mode for bosses
    def boss_combat_mode(self, boss):
        print("You are now facing " + boss.name + " and can only attack.")
        while boss.is_alive == True:
            choice = input(">>> ")
            if choice == "attack":
                self.attack(boss)
            else:
                print("\nYou may only attack\n")
                boss.en_attack(self)
        self.add_xp(200)
        self.add_coins(50)
        
    #Method for player dealing damage to enemy          
    def attack(self, enemy):
        damage = self.damage / enemy.toughness
        enemy.hp -= damage
        print("You hit " + enemy.name + " for " + str(damage) + " damage.")
        print("Enemy hp: " + str(enemy.hp))

        if enemy.hp <= 0:
            enemy.en_die(self)
        else:
            enemy.en_attack(self)

    #Method for enemy dealing damage to player
    def en_attack(self, player):
        damage = self.damage / player.toughness
        player.hp -= damage
        print(self.name + " hit you for " + str(damage) + " damage.")
        print("Your hp is now: " +  str(player.hp))

        if player.hp <= 0:
            player.die()

    #Enemy death method, sorts out rewards
    def en_die(self, player):
        print("You killed " + self.name + "\n")
        self.is_alive = False
        player.add_xp(50)
        player.add_coins(10)

    #Player dieing
    def die(self):
        print("\n\n\tYOU DIED\n\n")
        input("Press Enter To Exit")
        sys.exit()


    #MISC ACTIONS

    #Shows stats
    def stats(self):
        print("Name: " + self.name)
        print("HP: " + str(self.hp))
        print("Attack: " + str(self.damage))
        print("Toughness: " + str(self.toughness))
        print("XP: " + str(self.xp) + "/100")
        print("Level: " + str(self.level))

    #Add coins
    def add_coins(self, amount):
        self.wallet += amount
        print("You recived " + str(amount) + " coins.")

    # deals with xp and levels
    def add_xp(self, xp_gain):
        self.xp += xp_gain
        print("XP Gained: " + str(xp_gain) + "\n")
        while self.xp >= 100:
            self.xp -= 100
            self.level += 1
            print("You leveled up and gained a hp point, you are now level: " + str(self.level))

        if self.hp < (10 + self.level):
            self.hp += ((10 + self.level) - self.hp)

    #prints commands
    def get_help(self):
        print("""Commands (CASE SENSITIVE):
              - help: displays this message
              - look: look in a direction, East, West, North or South
              - move: Move in a direction, East, West, North or South
              - location: Gets current location (x and y coord)
              - map: lists cities x and y coords
              - stats: displays stats
              - read note: reads quest instructions
              - inventory: checks inventory
              - attack: attacks enemy
              - wallet: checks wallet
              - potions: checks amount of potions left
              - check x: where x is an item name, it checks its description
              - boss: face a cities boss
              - shop: visit a cities shop
              - victory: Check if you have won
              - save: saves game
              - load: loads last save
              - quit: Quits game
              """)

    #INSTRUCTIONS
    def read_note(self):
        print("Obtain a seal from each cities boss then type 'victory' to win.")


    #lists inventory
    def check_inventory(self):
        for item in self.inventory:
            print(item[1])

    #Displays Items Description
    def check_item(self, item):
        for i in self.inventory:
            if item.lower() == i[1].lower():
                #Uses [-1] So It Always Prints Final Section Of List
                print(i[-1])
        

    #Display's Users Potions
    def check_potions(self):
        print("Potions: " + str(self.potions))

    # Add item to inventory list
    def get_item(self, item):
        if item[0] == "weapon":
            for thing in self.inventory:
                if item[0] == thing[0]:
                    print("The weight was too much so you dropped " + thing[1])
                    del self.inventory[self.inventory.index(thing)]
        elif item[0] == "armour":
            for thing in self.inventory:
                if item[0] == thing[0]:
                    print("The weight was too much so you dropped " + thing[1])
                    del self.inventory[self.inventory.index(thing)]
        elif item[0] == "potion":
            for thing in self.inventory:
                if item[0] == thing[0]:
                    del self.inventory[self.inventory.index(thing)]
        else:
            pass
        self.inventory.append(item)
        print("You got : " + item[1])
        self.stat_update(item)


    # Updating player stats with item in form [type, name, value]
    def stat_update(self, item):
        if item[0].lower() == "weapon":
            self.damage = item[2]
        elif item[0].lower() == "armour":
            self.toughness = item[2]
        else:
            pass

    #Checks players wallet
    def coins(self):
        print("Coins : " + str(self.wallet))

    #Allows user to buy items
    def shop(self):
        shop_50 = {"shortsword": ["weapon", "Shortsword", 2, "A slighty worn shortsword"], "cadin'sor": ["armour", "Cadin'sor", 2, "An Aielmans garments, they smell unwashed..."]}
        shop_100 = {"longsword": ["weapon", "Longsword", 3, "A long blade with some rust at the hilt"], "plate mail": ["armour", "Plate Mail", 4, "A set of armour consisting of plates of metal" ]}
        shop_200 = {"heron-marked blade": ["weapon", "Heron-Marked Blade", 5, "A sword with the legendary heron mark of a blademaster"],
                    "callindor mail": ["armour", "Callindor Mail", 6, "A cumbersome set of armour with a faint magic auora"]}
        shop_misc = {"potion": ["potion", "Potion", "A potion imbuded with healing magic"] ,
                     "map": ["other", "Map" , "A map showing the various cities in this land"],
                     "mysterious talisman": ["other", "Mysterious Talisman", "An ancient talisman with a faded inscription that seems to read 'West of Tar Valon...22...'"]}
        shop_misc_prices = {"potion": 30, "map":50, "mysterious talisman": 100}
        print("Greetings, " + self.name + ".")
        print("""Stock:
    - Weapons:
      - Shortsword (Attack: 3) = 50 coins
      - Longsword (Attack: 5) = 100 coins
      - Heron-Marked Blade (Attack: 8) = 200 coins
    - Armour:
      - Cadin'sor (Toughness: 8) = 50 coins
      - Plate Mail (Toughness: 12) = 100 coins
      - Callindor Mail (Toughness: 20) = 200 coins
    - Other
      - Potion = 30 coins
      - Map = 50 coins
      - Mysterious Talisman = 100 coins

    Note: You can only hold 1 of each weapon and armour so stats will be replaced""")
        leave = ""
        #Loop for player buying items
        while leave != "y":
            print("What would you like to purchase: ")
            self.coins()
            choice = input(">>> ")
            if choice.lower() in shop_50:
                if self.wallet >= 50:
                    self.get_item(shop_50[choice.lower()])
                    self.wallet -= 50
                    self.coins()
                else:
                    print("Not enough coins")
            elif choice.lower() in shop_100:
                if self.wallet >= 100:
                    self.get_item(shop_100[choice.lower()])
                    self.wallet -=100
                    self.coins()
                else:
                    print("Not enough coins")
            elif choice.lower() in shop_200:
                if self.wallet >= 200:
                    self.get_item(shop_200[choice.lower()])
                    self.wallet -= 200
                    self.coins()
                else:
                    print("Not enough coins")
            elif choice.lower() in shop_misc_prices:
                if self.wallet >= shop_misc_prices[choice.lower()]:
                     self.get_item(shop_misc[choice.lower()])
                     self.wallet -= shop_misc_prices[choice.lower()]
                     self.coins()
                     if choice.lower() == "potion":
                         self.potions += 1
            else:
                print(choice + "?, " + "Not in Stock")

            #Checking if the player is finished
            leave = input("Is that all y/n: ")
            if leave == "y":
                pass
            elif leave == "n":
                pass
            else:
                print("Invalid choice, use y or n")

        print("Thanks for stopping by, " + self.name)
            

    #Checks if the player has beaten all the bosses
    def victory(self):
        count = 0
        for boss in Bosses:
            if boss[5][1] in self.inventory:
                count += 1
        if count == len(Cities):
            print("You have won, so yeah..")
        else:
            print("You need all five seal pieces to win")


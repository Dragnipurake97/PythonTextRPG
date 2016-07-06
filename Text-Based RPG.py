import sys, ast, Actions, Travel, random

#Creates player object
class Player(Actions.ActionsClass):

    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.damage = 1
        self.toughness = 1
        self.inventory = [["other", "Note", "A note with some writing on it"],
                          ["weapon", "Fists", 1, "Your bare hands"],
                          ["armour", "Loincloth", 1, "A soiled rag"]]
        self.level = 0
        self.xp = 0
        self.wallet = 100
        self.potions = 0

#Creates enemy object
class Enemy(Actions.ActionsClass):
    def __init__(self, name, hp, damage, toughness):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.toughness = toughness
        self.is_alive = True

# Class with the players x and y coordinates
class PlayerLocation(Travel.TravelClass):
    def __init__(self):
        self.x = 10
        self.y = 10

class SaveLoad:
    def save(player, travel):
        file = open("SaveFile.txt", "w")
        file.write(player.name + "\n")
        file.write(str(player.hp)+ "\n")
        file.write(str(player.damage)+ "\n")
        file.write(str(player.toughness)+ "\n")
        file.write(str(player.inventory)+ "\n")
        file.write(str(player.level)+ "\n")
        file.write(str(player.xp)+ "\n")
        file.write(str(player.wallet)+ "\n")
        file.write(str(player.potions) + "\n")
        file.write(str(travel.x)+ "\n")
        file.write(str(travel.y))
        file.close()

    def load(player, travel):
        file = open("SaveFile.txt", "r")
        load_data = file.readlines()
        file.close()
        for element in load_data:
            load_data[load_data.index(element)] = element.rstrip()
        player.name = load_data[0]
        player.hp = float(load_data[1])
        player.damage = int(load_data[2])
        player.toughness = int(load_data[3])
        player.inventory = ast.literal_eval(load_data[4])
        player.level = int(load_data[5])
        player.xp = int(load_data[6])
        player.wallet = int(load_data[7])
        player.potions = int(load_data[8])
        travel.x = int(load_data[9])
        travel.y = int(load_data[10])
        
        
        

#Method for the gameloop so I don't have to re-write it
def gameloop(player, travel):
    choice = ""
    while choice != "quit":
        choice = input(">>> ")
        # using commands
        if choice == "help":
            Actions.get_help(player)
        elif choice == "look":
            Travel.look(travel)
        elif choice == "move":
            Travel.move(travel)
            in_city = False
            for city in Cities:
                if travel.x == city[1] and travel.y == city[2]:
                    print("You are now in " + city[0])
                    in_city = True
                else:
                    pass
            if in_city == False:
                name, hp, attack, toughness = random.choice(Enemies)
                mob = Enemy(name, hp, attack, toughness)
                
                Actions.combat_mode(player, mob)
                
        elif choice == "location":
            Travel.get_location(travel)
        elif choice == "map":
            Travel.map(travel, player)
        elif choice == "stats":
            Actions.stats(player)
        elif choice == "read note":
            Actions.read_note(player)
        elif choice == "inventory":
            Actions.check_inventory(player)
        elif choice == "potions":
            Actions.check_potions(player)
        elif choice.partition(" ")[0] == "check":
            try:
                Actions.check_item(player, choice.partition(" ")[2])
            except IndexError:
                print("You need an item to check")
        elif choice == "boss":
            in_city = False
            for city in Cities:
                if travel.x == city[1] and travel.y == city[2]:
                    in_city = True
                    if city_completion[city[0]] == True:
                        print("You have already killed this cities boss")
                    else:
                        for boss in Bosses:
                            if city[0] in boss:
                                name, hp, attack, toughness = boss[1], boss[2], boss[3], boss[4]
                                boss_mob = Enemy(name, hp, attack, toughness)
                                Actions.boss_combat_mode(player, boss_mob)
                                Actions.get_item(player, boss[5])
                                city_completion[city[0]] = True
                else:
                    pass
            if in_city == False:
                print("Bosses are in each city")
        elif choice == "wallet":
            Actions.coins(player)
        elif choice == "shop":
            in_city = False
            for city in Cities:
                if travel.x == city[1] and travel.y == city[2]:
                    in_city = True
                    Actions.shop(player)
                else:
                    pass
            if in_city == False:
                print("There is a shop in each city")
        elif choice == "attack":
            print("You slash the air")
        elif choice == "victory":
            Actions.victory(player)
        elif choice == "save":
            SaveLoad.save(player, travel)
        elif choice =="load":
            SaveLoad.load(player, travel)        
        elif choice == "quit":
            sys.exit()
        else:
            print("invalid choice - type 'help' for commands")


#Game Initialisation
def main():
    player = Player(input("What's your name: "))
    choice = ""
    travel = PlayerLocation()
    Actions.get_help(player)
    gameloop(player, travel)


#Getting users created enemy list
enemies_text = open("Enemies.txt", "r")
Enemies = enemies_text.readlines()
del Enemies[0]
for enemy in Enemies:
    Enemies[Enemies.index(enemy)] = ast.literal_eval(enemy)
enemies_text.close()

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

#The start code
Actions = Actions.ActionsClass
Travel = Travel.TravelClass
#Make sure you can only kill bosses once
city_completion = {}
for city in Cities:
    city_completion[city[0]] = False

main()
input("press enter to continue")


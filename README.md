# Python-Test-RPG
This is project I created for a university coursework assignment in 2015. It is a basic text based adventure where the player can explore a map with different cities and the player must defeat a boss in each city. 
##Commands
- help: displays commands
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


##Stats
The player or enemy has the stats:
- HP (Health Points)
- Toughness (Reduces damage)
- Attack (Damage dealt)
- XP (Level progression)
- Level (Current level)
These stats can be upgraded from leveling up or upgrading their items.

##World
The world consists of a map (100x100 grid) where a player can move either North, South, East or West for any amount of steps (provided it doesn't go out of bounds). A player can also look in each direction too see what is there. A player can add or chamge the cities by editing the Cities.txt file, not having this file or it being in the wrong format will cause the game to not work.

##Combat
Combat is simple in that a player can either attack or drink a potion and then the enemy will attack. Players can progress to make combat easier by buying new items or getting more potions.

##Items
Items can be bought from the shop with gold earned from killing enemies and bosses. These items are:
- **Armour**:
- Cadin'Sor
- Plate Mail
- Callindor Mail
- **Weapons**:
- Shortsword
- Longsword
- Heron-Marked Blade
Each items has its own stats as well as a description that can be read with the "check" X (X = item name).

##Saving
A player can save the game, but only have 1 save state at a time. The data is saved in a textfile.

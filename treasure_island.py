print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You're at a cross road. Where do you want to go? Type 'left' or 'right'.")
dir=input().lower()
if dir=="right":
	print("You had an accident. Game over.")
if dir=="left":
	print("You walk and reach a lake with an island in the middle. Do you 'wait' for a boat or try to imitate Michael Phelps and 'swim'?")
	dec=input().lower()
	if dec=="swim":
		print("You really thought you could do it? You didnt make it. Game over.")
	if dec=="wait":
		print("A boat arrives and takes you to the island. You find a castle with 3 doors. One red, one yellow and one blue. Which one do you choose to open?")
		door=input().lower()
		if door=="blue":
			print("You have entered a dungeon and have been eaten by a beast. Game over.")
		if door=="red":
			print("The room turns red and you fall into a volcano. Game over.")
		if door=="yellow":
			print("You did it! You found the treasure!")
		else:
			print("You have been tricked into thinking there was another door. Game over.")
	else:
		print("You have been attacked by a shark. Game over.")
else:
	print("Seems like you are not interested in finding the treasure. Game over.")

print("This is a proof of concept - Player Weapon Management Module")
print ("\nPlease select a starting weapon\n")

#Weapons List Module
weapons = ['sword', 'dagger', 'staff', 'claws', 'club', 'war axe', 'spear']
for num, item in enumerate(weapons,0):
  print(num, '. ' + item.title(), sep='')
  
#User Selection Input Module
user_choice = input("\nPlease select a starting weapon by entering the item number: ")
user_choice = int(user_choice)
print(f"{'You have selected '}{weapons[user_choice].title()}")
print("\nSelection has been added to your inventory.")
print("CONCEPT - Player Items Management Module")
print('Author: R3 Studios / OKNERD')
print('Version: 0.0.1')
print('Date: 2021')

# Internal Code Vars
menu_lock = 'x'

# Weapons List
weapons = ['longsword', 'shortsword', 'spiked gloves', 'mace', 'halberd', 'dagger', 'staff', 'claws', 'club',
           'war hammer', 'war axe', 'spear', 'longbow', 'bow', 'crossbow', 'none']

# Gear & Armor List
gearHelm = ['leather helm', 'iron helm', 'steal helm', 'none']
gearCuirass = ['leather cuirass', 'iron cuirass', 'steal cuirass', 'none']
gearGreaves = ['leather greaves', 'iron greaves', 'steal greaves', 'none']
gearGauntlets = ['leather gauntlets', 'iron gauntlets', 'steal gauntlets', 'none']
gearBoots = ['leather boots', 'iron boots', 'steal boots' 'none']

# Lists All in-Game Weapons
print("\nPlease select a weapon\n")
for num, item in enumerate(weapons, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - First Weapon Selection
while True:
    try:
        user_choice = int(input("Please choose a weapon:  "))
        if 0 <= user_choice <= 15:
            print('')
            print(f"{'You have selected: '}{weapons[user_choice].title()}")
            print("\nWeapon has been added to your inventory...\n")
            break
        else:
            print("Provide an listed item value...")
    except ValueError:
        print("Provide an listed item value...")
        continue

# PlayerInput - Second Weapon Selection
while True:
    try:
        user_choice = int(input("Please choose a weapon:  "))
        if 0 <= user_choice <= 15:
            print('')
            print(f"{'You have selected: '}{weapons[user_choice].title()}")
            print("\nWeapon has been added to your inventory...\n")
            break
        else:
            print("Provide an listed item value...")
    except ValueError:
        print("Provide an listed item value...")
        continue
    
# Pause
while menu_lock == 'x':
    menu_lock = input("Press [ENTER] to continue")

# Lists All in-Game Helms
print("\nPlease select a helm\n")
for num, item in enumerate(gearHelm, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Helm Selection
user_choice = int(input("\nSelect helm: "))
print('')
print(f"{'You have selected '}{gearHelm[user_choice].title()}")
print("\nHelm has been added to your inventory...\n")

# Pause
while menu_lock == 'x':
    menu_lock = input("Press [ENTER] to continue")

# Lists All in-Game Cuirass
print("\nPlease select a cuirass\n")
for num, item in enumerate(gearCuirass, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Cuirass Selection
user_choice = int(input("\nSelect a cuirass: "))
print('')
print(f"{'You have selected: '}{gearCuirass[user_choice].title()}")
print("\nCuirass has been added to your inventory.\n")

# Pause
while menu_lock == 'x':
    menu_lock = input("Press [ENTER] to continue")

# Lists All in-Game Greaves
print("\nPlease select a pair of greaves\n")
for num, item in enumerate(gearGreaves, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Greaves Selection
user_choice = int(input("\nSelect a pair of greaves: "))
print('')
print(f"{'You have selected: '}{gearGreaves[user_choice].title()}")
print("\nGreaves have been added to your inventory.\n")

# Pause
while menu_lock == 'x':
    menu_lock = input("Press [ENTER] to continue")

# Lists All in-Game Gauntlets
print("\nPlease select a pair of Gauntlets\n")
for num, item in enumerate(gearGauntlets, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Gauntlets Selection
user_choice = int(input("\nSelect a pair of gauntlets: "))
print('')
print(f"{'You have selected: '}{gearGauntlets[user_choice].title()}")
print("\nGauntlets have been added to your inventory.\n")

# Pause
while menu_lock == 'x':
    menu_lock = input("Press [ENTER] to continue")

# Lists All in-Game Boots
print("\nPlease select a boots\n")
for num, item in enumerate(gearBoots, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Gauntlets Selection
user_choice = int(input("\nSelect a pair of boots: "))
print('')
print(f"{'You have selected: '}{gearBoots[user_choice].title()}")
print("\nBoots have been added to your inventory.\n")

end = ()

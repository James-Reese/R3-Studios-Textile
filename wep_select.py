print("CONCEPT - Player Items Management Module")
print('Author: R3 Studios / OKNERD')
print('Version: 0.0.1')
print('Date: 2021')

# Internal Code Vars
menu_lock = 'x'

# Weapons List
weapons = ['longsword', 'shortsword', 'spiked gloves', 'mace', 'halberd', 'dagger', 'staff', 'claws', 'club',
           'war hammer', 'war axe', 'spear', 'longbow', 'bow', 'crossbow', 'none']
wep_len = len(weapons)

# Gear & Armor List
gearHelm = ['leather helm', 'iron helm', 'steal helm', 'none']
helm_len = len(gearHelm)

gearCuirass = ['leather cuirass', 'iron cuirass', 'steal cuirass', 'none']
cuirass_len = len(gearCuirass)

gearGreaves = ['leather greaves', 'iron greaves', 'steal greaves', 'none']
greaves_len = len(gearGreaves)

gearGauntlets = ['leather gauntlets', 'iron gauntlets', 'steal gauntlets', 'none']
gauntlets_len = len(gearGauntlets)

gearBoots = ['leather boots', 'iron boots', 'steal boots', 'none']
boots_len = len(gearBoots)

# Lists All in-Game Weapons
print("\nPlease select a weapon\n")
for num, item in enumerate(weapons, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - First Weapon Selection
while True:
    try:
        user_choice = int(input("Please choose a weapon:  "))
        if 0 <= user_choice <= wep_len:
            print('')
            print(f"{'You have selected: '}{weapons[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue

# PlayerInput - Second Weapon Selection
while True:
    try:
        user_choice = int(input("Please choose a secondary weapon: "))
        if 0 <= user_choice <= wep_len:
            print('')
            print(f"{'You have selected: '}{weapons[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue

# Lists All in-Game Helms
print("\nPlease select a helm\n")
for num, item in enumerate(gearHelm, 0):
    print(num, '. ' + item.title(), sep='')
    
# PlayerInput - Helm Selection
while True:
    try:
        user_choice = int(input("Please choose a helm: "))
        if 0 <= user_choice <= helm_len:
            print('')
            print(f"{'You have selected: '}{gearHelm[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue
        
# Lists All in-Game Cuirass
print("\nPlease select a cuirass\n")
for num, item in enumerate(gearCuirass, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Cuirass Selection
while True:
    try:
        user_choice = int(input("Please choose a cuirass: "))
        if 0 <= user_choice <= cuirass_len:            
            print('')
            print(f"{'You have selected: '}{gearCuirass[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue

# Lists All in-Game Greaves
print("\nPlease select a pair of greaves\n")
for num, item in enumerate(gearGreaves, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Greaves Selection
while True:
    try:
        user_choice = int(input("Please choose a pair of greaves: "))
        if 0 <= user_choice <= greaves_len:
            print('')
            print(f"{'You have selected: '}{gearGreaves[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue

# Lists All in-Game Gauntlets
print("\nPlease select a pair of gauntlets\n")
for num, item in enumerate(gearGauntlets, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Gauntlets Selection
while True:
    try:
        user_choice = int(input("Please choose a pair of gauntlets: "))
        if 0 <= user_choice <= gauntlets_len:
            print('')
            print(f"{'You have selected: '}{gearGauntlets[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue
        
# Lists All in-Game Boots
print("\nPlease select a pair of boots\n")
for num, item in enumerate(gearBoots, 0):
    print(num, '. ' + item.title(), sep='')

# PlayerInput - Gauntlets Selection
while True:
    try:
        user_choice = int(input("Please choose a pair of boots: "))
        if 0 <= user_choice <= boots_len:
            print('')
            print(f"{'You have selected: '}{gearBoots[user_choice].title()}")
            print("\nItem has been added to your inventory...\n")
            break
        else:
            print("Please select a valid option...")
    except ValueError:
        print("Please select a valid option...")
        continue

end = ()
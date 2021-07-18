import time
import os
print("Player Items Selection Management Module")
print('Author: OKNERD/R3 STUDIOS')
print('Version: Pre-Production v2')
print('Date: 2021')


class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Weapons List
weapons = ['none', 'longsword', 'shortsword', 'spiked gloves', 'mace', 'halberd', 'dagger',
           'staff', 'claws', 'club', 'war hammer', 'war axe', 'spear', 'longbow', 'bow', 'crossbow']
weapons_len = len(weapons)

# Equipment & Armor List
gearHelm = ['none', 'leather helm', 'iron helm', 'steal helm']
helm_len = len(gearHelm)
gearCuirass = ['none', 'iron cuirass', 'steal cuirass']
cuirass_len = len(gearCuirass)
gearGreaves = ['none', 'leather greaves', 'iron greaves', 'steal greaves']
greaves_len = len(gearGreaves)
gearGauntlets = ['none', 'leather gauntlets', 'iron gauntlets', 'steal gauntlets']
gauntlets_len = len(gearGauntlets)
gearBoots = ['none', 'leather boots', 'iron boots', 'steal boots']
boots_len = len(gearBoots)


# Item Selection Function
def item_select(item_type, item_len, output_trigger):
    loop_gate = 1
    while loop_gate == 1:
        try:
            print('\nItem Selection Menu\n')
            for num, item in enumerate(item_type, 0):
                print(num, '. ' + item.title(), sep='')
            if item_type == weapons:
                output_type = 'a weapon'
            else:
                output_type = 'an item'
            if output_trigger == 1:
                output_type = 'a second weapon'
            else:
                pass
            user_choice = int(input(f'\nSelect {output_type}: '))
            if 0 <= user_choice <= item_len - 1:
                print('')
                # PlayerInput - Starting Item Selections
                print(f'You have selected: {item_type[user_choice].title()}')
                print('\nItem has been added to your inventory...\n')
                time.sleep(.9)
                os.system('cls')
                loop_gate = 0
                continue
            else:
                loop_gate = 1
                os.system('cls')
            print(f'{TextColors.FAIL}\nPlease select a valid option...{TextColors.ENDC}')
        except ValueError:
            loop_gate = 1
            os.system('cls')
            print(f'{TextColors.FAIL}\nPlease select a valid option...{TextColors.ENDC}')


# Item Selection
item_select(item_type=weapons, item_len=weapons_len, output_trigger=0)
item_select(item_type=weapons, item_len=weapons_len, output_trigger=1)
item_select(item_type=gearHelm, item_len=helm_len, output_trigger=0)
item_select(item_type=gearCuirass, item_len=cuirass_len, output_trigger=0)
item_select(item_type=gearGreaves, item_len=greaves_len, output_trigger=0)
item_select(item_type=gearGauntlets, item_len=gauntlets_len, output_trigger=0)
item_select(item_type=gearBoots, item_len=boots_len, output_trigger=0)

exit()

from classes.game import Person
from classes.magic import Spell
from classes.inventory import Item

# Instance Attack Spells - Black Magic
fire = Spell('fire', 10, 100, 'black')
thunder = Spell('thunder', 10, 100, 'black')
blizzard = Spell('blizzard', 10, 100, 'black')
meteor = Spell('meteor', 30, 300, 'black')
quake = Spell('quake', 15, 150, 'black')

# Instance Heal Spells - White Magic
cure = Spell('cure', 10, 150, 'white')
cura = Spell('cura', 20, 250, 'white')

# Instance Items

potion = Item('Potion', 'potion', 'Heals 100 hp', 100)
superpotion = Item('Superpotion', 'potion', 'Heals 250 hp', 250)
xpotion = Item('Xpotion', 'potion', 'Heals max hp', 9999)
elixer = Item('Elixer', 'elixer', 'Fully restores HP/MP of one party member', 9999)
megaelixer = Item('Megaelixer', 'megaelixer', 'Fully restores HP/MP of all party members', 9999)
grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)


# Create arrays
player_spells = [fire, thunder, meteor, blizzard, cure, cura]
player_items = [{'item': potion, 'quantity': 15},
                {'item': superpotion, 'quantity': 10},
                {'item': xpotion, 'quantity': 5},
                {'item': elixer, 'quantity': 2},
                {'item': megaelixer, 'quantity': 1},
                {'item': grenade, 'quantity': 10}]

# Instanse players
player = Person('Valos',600, 100, 80, 40, player_spells, player_items)
enemy = Person(2000, 300, 150, 80, [], [])

running = True
i = 0

print('AN ENEMY ATTACKS!')

while running:
    print('=====================')
    player.choose_action()
    choise = int(input('Choose action: ')) - 1
    
    if choise == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(f'\nYou atacked for {dmg} points of damage')

    elif choise == 1:
        player.choose_magic()
        magic_choise = int(input('Choose magic: ')) - 1
        
        if magic_choise == -1:
            continue
        
        spell = player.magic[magic_choise]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print('Not enough MP')
            continue

        player.reduce_mp(spell.cost)
        if spell.type == 'white':
            player.heal(magic_dmg)
            print(f'\n{spell.name} heals for {magic_dmg} HP')

        elif spell.type == 'black':        
            enemy.take_damage(magic_dmg)
            print(f'\n{spell.name} deals {magic_dmg} points of damage ')

    elif choise == 2:

        player.choose_item()
        item_choise = int(input('Choose item: ')) - 1
        if item_choise == -1:
            continue

        item = player.items[item_choise]['item']
        if player.items[item_choise]['quantity'] == 0:
            print('\n None left..')
            continue
        
        player.items[item_choise]['quantity'] -= 1

        if item.type == 'potion':
            player.heal(item.value)
            print(f'\n{item.name} heals for {item.value} HP')
        elif item.type == 'elixer':
            player.hp = player.max_hp
            player.mp = player.max_mp
            print(f'\n{item.name} fully restores HP/MP')
        elif item.type == 'attack':
            enemy.take_damage(item.value)
            print(f'\n{item.name} deals {item.value} points of damage to the enemy.')


    enemy_choise = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f'Enemy attacks for {enemy_dmg}')
    print('-----------------------------------')
    print(f'Enemy HP: {enemy.get_hp()}/{enemy.get_max_hp()}')
    print(f'Player HP: {player.get_hp()}/{player.get_max_hp()}')
    print(f'Player MP: {player.get_mp()}/{player.get_max_mp()}')


    if player.get_hp() == 0:
        print('Your HP is 0, you are defeated.')
        running = False
    elif enemy.get_hp() == 0:
        print('Enemy HP is 0, you won!')
        running = False
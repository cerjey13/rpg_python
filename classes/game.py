import random
from .magic import Spell
from .inventory import Item


class Person:
    def __init__(self, name, hp, mp, atk, defe, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defe = defe
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.max_hp
    
    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    def get_spell_name(self):
        return self.magic['name']

    def choose_action(self):
        i = 1
        print('Actions')
        for item in self.actions:
            print(f'{i}: {item}')
            i += 1
    
    def choose_magic(self):
        i = 1
        print('Magic')
        for spell in self.magic:
            print(f'{i}: {spell.name} (cost:{spell.cost})')
            i += 1
    
    def choose_item(self):
        i = 1
        print('Items')
        for item in self.items:
            print(f'{i}: {item["item"].name} - {item["item"].description} (x{item["quantity"]})')
            i += 1
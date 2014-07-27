from scrpy import scr
from game import rpg
from tkinter import *

stats = [50,3,3,3,3]
stats2 = [15,2,4,5,2]

person = rpg.character

Si=person("Simon",100,stats)
guy=person("Guy",45,stats2)

weapon = rpg.weapon

BattleAxe = weapon("Battle Axe",35,1,0)

rpg.equip.weapon(Si,BattleAxe)

rpg.attack.weaponAtk(Si,guy)
print(guy.health)

rpg.attack.weaponAtk(Si,guy)
print(guy.health)

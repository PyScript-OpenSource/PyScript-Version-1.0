from PyScript import scr

class rpg():
    class magic():
        def __init__(self,name,damage,manaCost,text):
            self.name = name
            self.damage = damage
            self.manaCost = manaCost
            self.text = text
    class attack():
        def magicAttack(caster,magic,target):
            caster.mana-=magic.manaCost
            if caster.mana<0:
                caster.mana+=magic.manaCost

            else:
                target.health-=magic.damage
                print(magic.text)
                if target.health < 1:
                    print(caster+" killed "+target)
        def weaponAtk(character,target):
            target.health -= character.inventory[0].damage/(character.defe/2)
            if target.health < 1:
                    print(character.name+" killed "+target.name)
    class weapon():
        def __init__(self,name,damage,lvl,lvlR):
            self.name=name
            self.damage = damage
            self.lvl = lvl
            self.lvlR = lvlR
    class armor():
        def __init__(self,name,defe):
            self.name = name
            self.defe = defe
    class character():
        def __init__(self,name,health,stats):
            self.name = name
            self.mana = stats[0]
            self.defe = stats[1]
            self.spd = stats[2]
            self.dex = stats[3]
            self.atk = stats[4]
            self.health = health
            self.inventory = [None]
            self.level = 1
        def lvlUp(self,mod):
            self.level+=1
            self.mana+=mod
            self.defe+=mod
            self.spd+=mod
            self.dex+=mod
            self.atk+=mod
            self.health+=mod*3
        def armorEquip(self):
            self.defe += self.inventory[1].defe
    class equip():
        def weapon(character,weapon):
            if character.level > weapon.lvlR-1:
                character.inventory[0] = weapon
        def armor(character,armor):
            character.inventory[1] = armor
            

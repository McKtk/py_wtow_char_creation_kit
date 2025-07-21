class Characteristic: 
    def __init__(
    self, 
    name: str, 
    value: int
    ):
        self.name = name
        self.value = value

class Characteristics:
    def __init__(
    self, 
    weaponSkill: Characteristic,
    balisticSkill:Characteristic ,
    strength:Characteristic, 
    toughness:Characteristic, 
    initiative:Characteristic, 
    agility:Characteristic,
    reason:Characteristic,
    fellowship:Characteristic,
    fate:Characteristic
    ):
        self.weaponSkill = weaponSkill
        self.balisticSkill = balisticSkill
        self.strength = strength
        self.toughness = toughness
        self.initiative = initiative
        self.agility = agility
        self.reason = reason
        self.fellowship = fellowship
        self.fate = fate
    
class Skill:
    def __init__(
    self, 
    mainStat:Characteristic, 
    name: str,
    value:int
    ):
        self.mainStat = mainStat
        self.name = name
        self.value = value
    
class Lore: 
    def __init__(
    self, 
    name:str
    ):
        self.name = name
    
class Talent:
    def __init__(
    self, 
    name:str, 
    cost: int, 
    desc: str
    ):
        self.name = name
        self.cost = cost
        self.desc = desc
    
class Character:
    def __init__(
    self,
    name:str,
    origin:str,
    career:str,
    stats:Characteristics,
    exp:int,
    speed:str,
    lores:list[Lore],
    talents:list[Talent],
    ):
        self.name = name
        self.origin = origin
        self.career = career
        self.stats = stats
        self.exp = exp
        self.speed = speed
        self.lores = lores
        self.talents = talents
class Characteristic: 
    name = str
    value = int

class Characteristics:
    weaponSkill = Characteristic
    balisticSkill = Characteristic
    strength = Characteristic
    toughness = Characteristic
    initiative = Characteristic
    agility = Characteristic
    reason = Characteristic
    fellowship = Characteristic
    fate = Characteristic
    
class Skill:
    mainStat = Characteristic
    value = int
    
class Lore: 
    name = str
    
class Talent:
    name = str
    cost = int
    desc = str
    
class Character:
    name = str
    origin = str
    career = str
    stats = Characteristics
    exp = int
    speed = str
    lores = list[Lore]
    talents = list[Talent]
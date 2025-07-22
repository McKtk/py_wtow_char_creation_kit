from modules.classes import *
import pickle

table: list = [
    Talent("Accelerated Recovery",4, "Toughness 5+"),
    Talent("Acrobatic",3, "Agility 4+"),
    Talent("Allies in Arms",3, "Fellowship 4+"),
    Talent("Armour Bane",3, ""),
    Talent("Bash Attack",4, "Strength 5+"),
    Talent("Back in the Saddle",2,"Agility 4+"),
    Talent("Battlefield Musician",3,"Musician's Gear"),
    Talent("Blessings of the Lady",3,"Bretonnian Origin, High Society Lore, Honour Bound"),
    Talent("Careful Aim",3, "Reason 4+"),
    Talent("Cleaving Blow",4, "Strength 5+"),
    Talent("Combat Surgeon",3, "Anatomy Lore"),
    Talent("Deep Formation",2, ""),
    Talent("Defensive Stance",2,"Weapon Skill 3+"),
    Talent("Dispeller",3, "Wizard"),
    Talent("Exceptional Hearing",2, "Initiative 4+"),
    Talent("Faith",4, "Empire Origin"),
    Talent("Familiar",3, "Wizard"),
    Talent("Feigned Flight",2,""),
    Talent("Fight As One",3,""),
    Talent("Frightening",4, ""),
    Talent("Golden Voice",2,"Fellowship 4+"),
    Talent("The Grail Vow",4, "The Questing Vow"),
    Talent("Hardy",3, "Toughness 4+"),
    Talent("Hatred",3,""),
    Talent("Hold the Line",3,"Fellowship 4+"),
    Talent("Honour Bound",3,""),
    Talent("Intense Scrutiny",3, "Initiative 4+"),
    Talent("Interceptor",4, "Agility 5+"),
    Talent("Iron Gut",2, "Not a High Elf or Wood Elf"),
    Talent("Keen Eyed",2, "Initiative 4+"),
    Talent("Lightning Reflexes",3, "Initiative 5+"),
    Talent("Longbeard",3, "Dwarf Origin, only in character creation"),
    Talent("Lucky",4, ""),
    Talent("Magic Resistance",3, ""),
    Talent("Mighty Blow",3, "Strength 4+"),
    Talent("Night Dweller",2, ""),
    Talent("Polymath",2, "Reason 4+"),
    Talent("The Questing Vow",3, "Blessing of the Lady"),
    Talent("Quick Change",3, "Grooming Kit"),
    Talent("Quick Throw",4, "Weapon Skill 4+, Ballistic Skill 4+"),
    Talent("Rapid Reload",3, "Ballistic Skill 4+"),
    Talent("Resistance to Corruption",4, ""),
    Talent("Resolute",3, "Reason 4+"),
    Talent("Riposte",4, "Weapon Skill 5+"),
    Talent("Secret Bloodline",3, "only in character creation"),
    Talent("Short Size",2, "only in character creation"),
    Talent("Snake Charmer",3, ""),
    Talent("Spiteseer",3, "Wood Elf Origin"),
    Talent("Stand and Shoot",3,"Initiative 4+"),
    Talent("Steer Clear",3, ""),
    Talent("Taunter",4,""),
    Talent("Thirst for Knowledge",2, "Reason 4+"),
    Talent("Touched by the Winds",2,"Not a Dwarf or Halfling"),
    Talent("Unbreakable",3,"Resolute"),
    Talent("Valour of Ages",3,"High Elf Origin"),
    Talent("Vanguard",3, "Agility 4+"),
    Talent("Vouch For Them",3, "Silver or Gold status, Fellowship 4+"),
    Talent("Wild Attack",3, "Strength 4+"),
    Talent("Wizard",4, "Not a Dwarf or Halfling, Magic Lore (any)")
]

with open("./bin/talents.bin", "wb") as f:
    pickle.dump(table, f)
    
with open("./bin/talents.bin", "rb") as f:
    loaded_table = pickle.load(f)
    
print(loaded_table)
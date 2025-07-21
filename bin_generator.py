from modules.classes import Skill, Characteristic
import pickle

table: list = [
    "Brettonian",
    "Dwarf",
    "Empire",
    "Halfling",
    "High Elf",
    "Wood Elf"
]

with open("./bin/origin.bin", "wb") as f:
    pickle.dump(table, f)
    
with open("./bin/origin.bin", "rb") as f:
    loaded_table = pickle.load(f)
    
print(loaded_table)
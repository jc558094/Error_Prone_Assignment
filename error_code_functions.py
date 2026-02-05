import random

def combat(p1, p2):
    attack = random.randint(1,20)
    initiative = random.choice([p1["name"],p2["name"]])
    print(f"\n{initiative} acts!")
    if initiative == p1["name"]:
        if p1["attack"] + attack >= p2["defense"]:
            p2["health"] -= p1["damage"]  
            print(f"{p1['name']} lands a hit for {p1['damage']} damage!")
        else:
            print(f"{p1['name']} swings... and misses!")
    else:
        if p2["attack"] + attack >= p1["defense"]:
            p1["health"] -= p2["damage"] 
            print(f"The {p2['name']} strikes you for {p2['damage']} damage!")
        else:
            print(f"The {p2['name']} attacks... but you dodge it!")
    return p1,p2

def create_monster():
    stats = [25,50,75,100]
    health = random.choice(stats)
    stats.remove(health)
    attack = random.choice(stats)
    stats.remove(attack)
    defense = random.choice(stats)
    stats.remove(defense)
    damage = random.choice(stats)


    if damage == "100":
        name = "Dragon"
    elif damage == "75":
        name = "Manticore"
    elif damage == "50":
        name = "Ogre"
    else:
        name = "Goblin"

    return {
        "name":name,
        "health":health,
        "attack":attack,
        "defense":defense,
        "damage":damage
        }

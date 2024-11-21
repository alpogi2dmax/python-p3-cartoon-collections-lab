def roll_call_dwarves(dwarves_list):
    for i in range(len(dwarves_list)):
        print(f"{i+1}. {dwarves_list[i]}")

def summon_captain_planet(planeteers):
    new_planeteers = list()
    for planeteer in planeteers:
        new_planeteers.append(f"{planeteer.capitalize()}!")
    return new_planeteers


def long_planeteer_calls(words):
    return len(words) == 4

def find_the_cheese(foods):
    for food in foods:
        if food == 'cheddar':
            return 'cheddar'
        elif food == 'gouda':
            return 'gouda'
        elif food == 'camembert':
            return 'camembert'
        else:
            'None'

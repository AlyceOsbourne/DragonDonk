import random
from functools import partial
from typing import Callable

roll_d4 = partial(random.randint, 1, 4)
roll_d6 = partial(random.randint, 1, 6)
roll_d8 = partial(random.randint, 1, 8)
roll_d10 = partial(random.randint, 1, 10)
roll_d12 = partial(random.randint, 1, 12)
roll_d20 = partial(random.randint, 1, 20)
roll_d00 = partial(random.randint, 0, 99)

def advantage_check(roll: Callable, at_disadvantage):
    rolls = roll(), roll()
    return min(rolls) if at_disadvantage else max(rolls)

def ability_check(roll, modifier):
    return roll() + modifier

def perform_ability_check(to_pass, roll=roll_d20, modifier=0):
    return ability_check(roll, modifier) >= to_pass

def perform_contest(roll = roll_d20, 
            creature_a_modifier = 0, 
            creature_b_modifier = 0):
                creature_a = ability_check(roll, creature_a_modifier)
                creature_b = ability_check(roll, creature_b_modifier)
                return 0 if creature_a == creature_b else 1 if creature_a > creature_b else -1

def passive_check(modifier, at_advantage, to_pass):
    return 10 + modifier + 5 if at_advantage else -5 >= to_pass

def group_check(at_advantage, to_pass, *modifiers):
        passed = 0
        for mod in modifiers:
            if passive_check(mod, at_advantage, to_pass):
                passed +=1
                if passed > len(modifiers)//2:
                    return True
        return False

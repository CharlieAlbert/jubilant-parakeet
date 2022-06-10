import time
import random
import pyautogui

weight = []


# main assumption = (-ve carriage)
# variables: -overweight
#            -total population
#            -time duration
#            -luggage
# 1 boat only takes 2 people and the weight is k, how much boat is needed?
# step1: say the total population is X
# step2: say for example we have boat Y, takes in p1(w1) and p2(w2), definitely
# w1 + w2 = k
# step 3: what if there's an overweight of 1 person?, the k-Wo should be compensated by a child or luggage
# step4: the total boats needed is: X/2(minus the assumption of the overweight)
# step5: X/2 + c...where c is the added boat to save everyone
# sample =  [100, 150, 200, 300] max is 200...catch is that boat takes 2 people
# --each boat has its own maximum limit:i) if we have 2 people that meet the Sw, then the boat goes once
#                                        ii) if 1 person is enough ie [(Sw-w1) < w2] < Sw then the bought 
#                                        carries one but makes 2 trips
# 
# 

# function to return key for any value
def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def sort_weight_pop():
    total = int(input("Hello mayor :), what's your total population..."))
    default_boats_even = total / 2
    default_boats_odd = total % 2
    if default_boats_odd % 2 == 0:
        global full
        full = default_boats_odd / 2
    else:
        global _full
        _full = default_boats_odd + 1
    print(" ")
    print(f"So, by default we need a total of {default_boats_even} boats plus another {full}")
    # fill in the boats
    weights = dict(input("Two people per boat mayor....gimme the array of the top 5 names and weight....."))
    for x, y in weights.items():
        preferred_arr = random.choices((x, y), k=4)

    lst_max = [200, 350, 500, 650]
    max_boat = random.choice(lst_max)
    time.sleep(2)
    print(" ")
    print(f"The max weight chosen is {max_boat}...")
    for x, y in preferred_arr.items():
        ls = list(preferred_arr.keys())
        vs = list(preferred_arr.values())
        pos = vs.index(x)
        pose = random.choices(vs, k=2)
        if pose[0] + pose[1] == max_boat:
            print(" ")
            print(f"the people chosen are {ls[pos]} and ")


def checklugtime():
    print(" ")
    pass


def seaways():
    pass

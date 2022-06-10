import random
import time


# 1 boat only carries 2 people and their luggage. Their total weight is k.
# step1: total population is X. No. of boats = X/2.
# step2: boat Y takes in p1 and p2 with w1 and w2 respectively.
# w1 + w2 = k
# total weight for one boat is Sw.
# step3: if there is an overweight, Wo, it is compensated by a child
# step4: total boats needed is X/2, assuming there is no overweight, Wo.
# step5: each boat has its own maximum weight limit Sw: i) if 2 people meet maximum weight, Sw,
#                                                         the boat goes once.
#                                                       ii) if 1 person is close (+/-) to Sw ie (Sw - w1) < w2,
#                                                           then the boat goes 2 trips.
#


def seek_pass():
    total = int(input('Hello Captain, give us your population: '))
    if total % 2 == 0:
        global full
        full = total / 2
    else:
        full = (total / 2) + 1

    print(f'Generally the total number of boats needed is {full}')
    print('')
    weights = dict(input('Yow Captain, give us the top 5 guys on your list and their weights'))
    for x, y in weights.items():
        preferred_arr = random.choices((x, y), k=4)

    max_list = [300, 200, 450, 350]
    max_weight = random.choice(max_list)

    if max_weight in max_list:
        boat_number = max_list.index(max_weight)

    print('')
    print(f'The maximum weight chosen is {max_weight}')

    for x, y in preferred_arr.items():
        name = list(preferred_arr.keys())
        values = list(preferred_arr.values())
        pos = values.index(x)
        w = random.choices(values, k=2)

        if w[0] + w[1] <= max_weight:
            chosen_pass = w.name
            print(f'The chosen passengers are {chosen_pass}')
        else:
            chosen_pass = random.choice(w)
            print(f'Passenger {chosen_pass} will be on the first trip on boat number {boat_number}')











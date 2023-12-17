gold = 5
land = 1


def evaluate_budget():
    increase = land * 0.1
    random_modifier = random.randint(0, 5) * 0.1
    return increase / random_modifier

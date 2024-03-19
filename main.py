import random


def prime(goal):
    base_set = {1, 2, 3, 4}
    values_set = {-3, -2, -1, 0, 1, 2, 3}
    e = random.choice(list(base_set))
    goal[e - 1] = 0
    base_set.remove(e)
    e = random.choice(list(base_set))
    goal[e - 1] = random.choice(list(values_set))
    return goal


def others(goal):
    base_set = {1, 2, 3, 4}
    values_set = {-3, -2, -1, 0, 1, 2, 3}
    e = random.choice(list(base_set))
    goal[e - 1] = random.choice(list(values_set))
    base_set.remove(e)
    e = random.choice(list(base_set))
    goal[e - 1] = random.choice(list(values_set))
    return goal


buffK, buffP, buff1, buff2, buff3, buff4 = [None] * 4, [None] * 4, [None] * 4, [None] * 4, [None] * 4, [None] * 4
goals = {"king": buffK, "prime": buffP, "army": buff1, "economy": buff2, "religion": buff3, "society": buff4}
for goal in goals.keys():
    if goal == "king":
        goals[goal] = [0] * 4
        print(goal, "k")
    elif goal == "prime":
        goals[goal] = prime(goals[goal])
        print(goal, "p")
    else:
        goals[goal] = others(goals[goal])
        print(goal, "o")

print(goals)
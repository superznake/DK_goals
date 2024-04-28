import random
from enum import Enum


class Minister(Enum):
    ARMY = 1
    ECONOMY = 2
    RELIGION = 3
    SOCIETY = 4


def create():
    buffk, buffp, buff1, buff2, buff3, buff4 = [None] * 4, [None] * 4, [None] * 4, [None] * 4, [None] * 4, [None] * 4
    goals = {"king": buffk, "prime": buffp, Minister.ARMY: buff1, Minister.ECONOMY: buff2, Minister.RELIGION: buff3, Minister.SOCIETY: buff4}
    for goal in goals.keys():
        if goal == "king":
            goals[goal] = [0] * 4
            # print(goal, "k")
        elif goal == "prime":
            goals[goal] = prime(goals[goal])
            # print(goal, "p")
        else:
            goals[goal] = others(goals[goal], goal)
            # print(goal, "o")
    return goals


def prime(goal):
    base_set = {1, 2, 3, 4}
    values_set = {-3, -2, -1, 0, 1, 2, 3}
    e = random.choice(list(base_set))
    goal[e - 1] = 0
    base_set.remove(e)
    e = random.choice(list(base_set))
    goal[e - 1] = random.choice(list(values_set))
    return goal


def others(goal, name: Minister):
    base_set = {1, 2, 3, 4}
    base_set.remove(name.value)
    values_set = {-3, -2, -1, 0, 1, 2, 3}
    e = random.choice(list(base_set))
    goal[e - 1] = random.choice(list(values_set))
    base_set.remove(e)
    e = random.choice(list(base_set))
    goal[e - 1] = random.choice(list(values_set))
    return goal


print(create())

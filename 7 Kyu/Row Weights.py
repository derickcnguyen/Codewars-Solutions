Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

def row_weights(array):
    team1 = []
    team2 = []
    for i in range(len(array)):
        if i % 2 == 0:
            team1.append(array[i])
        if i % 2 != 0:
            team2.append(array[i])
    return (sum(team1),sum(team2))

or

def row_weights(array):
    return (sum(array[::2]),sum(array[1::2]))

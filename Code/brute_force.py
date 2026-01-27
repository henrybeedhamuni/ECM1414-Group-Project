from itertools import combinations

def brute_force_planner(activities,max_time,budget):

    # assign id's to each activity (integer 0-num of activities)
    ids = list()
    for i in range(len(activities)):
        ids.append(i)

    cheapest = activities[0]
    for activity in activities:
        if activity.cost < cheapest.cost:
            cheapest = activity

    max_length = budget // cheapest.cost
    if max_length > len(activities):
        max_length = len(activities)

    best_solution = [[0],[0],[0],[0]] # Combination, cost, time, enjoyment

    # run the combinations alorithm
    for length in range(max_length,1,-1):
        possible_solutions = combinations(ids,length)
        for solution in possible_solutions:
            cost = 0
            time = 0
            enjoyment = 0
            for activity in solution:
                cost += activities[activity].cost
                time += activities[activity].duration
            if cost <= budget and time <= max_time:
                enjoyment += activities[activity].enjoyment_level
                if enjoyment > best_solution[3][0]:
                    best_solution = [[solution],[cost],[time],[enjoyment]]

    return(best_solution)

    #itertools.combinations(iterable, r): It returns r-length tuples in sorted order with no repeated elements. For Example, combinations('ABCD', 2) ==> [AB, AC, AD, BC, BD, CD]. https://www.geeksforgeeks.org/python/itertools-combinations-module-python-print-possible-combinations/
    # process each comibination, if the cost > budget do not add to dictionary of possible soultions, enjoyment as key and the array [combination, time, cost, enjoyment]
    # sort the dictionary by key (higher is better, descending val), if the number of values assigned to 1 key is > 1 then we take the first solution
    # return the solution to main program
    
from itertools import combinations

def enhanced_brute_force_planner(activities,max_time,budget):

    # assign id's to each activity (integer 0-num of activities)
    ids = list() #create list for IDs
    for i in range(len(activities)):
        ids.append(i) #add each activity to the list of activityies

    cheapest = activities[0] #initial value for cheapest activity
    for activity in activities:
        if activity.cost < cheapest.cost: #if the next activity is cheaper then that is now the cheapest activity
            cheapest = activity 

    max_length = budget // cheapest.cost #ceiling for the max combination length to test to
    if max_length > len(activities): #if max length is longer than the number of activities reduce the ceiling to the number of activities
        max_length = len(activities)

    best_solution = [0,0,0,0] # Combination, cost, time, enjoyment

    # run the combinations alorithm
    for length in range(max_length,1,-1): #iterating from max length combinations to 1 length
        possible_solutions = combinations(ids,length) #tuple of all combinations of current length
        for solution in possible_solutions: #testing each solution in the tuple of combinations
            cost = 0
            time = 0
            enjoyment = 0
            for activity in solution: #adding up the cost, duration and enjoyment total for that combination
                cost += activities[activity].cost
                time += activities[activity].duration
                enjoyment += activities[activity].enjoyment_level
            if cost <= budget and time <= max_time and enjoyment >= best_solution[3]: #checking constraints if the new enjoyment is greater than the current best enjoyment overwrite it with the new solution
                    best_solution = [solution,cost,time,enjoyment]

    return(best_solution) #returning the best solution found

    #itertools.combinations(iterable, r): It returns r-length tuples in sorted order with no repeated elements. For Example, combinations('ABCD', 2) ==> [AB, AC, AD, BC, BD, CD]. https://www.geeksforgeeks.org/python/itertools-combinations-module-python-print-possible-combinations/
    # process each comibination, if the cost > budget do not add to dictionary of possible soultions, enjoyment as key and the array [combination, time, cost, enjoyment]
    # sort the dictionary by key (higher is better, descending val), if the number of values assigned to 1 key is > 1 then we take the first solution
    # return the solution to main program
    
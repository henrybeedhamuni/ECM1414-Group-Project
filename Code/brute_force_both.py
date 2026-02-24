def brute_force(activity_array,time,budget):
    # assign id's to each activity (integer 0-num of activities)
    # run the combinations alorithm
    #itertools.combinations(iterable, r): It returns r-length tuples in sorted order with no repeated elements. 
    #   For Example, combinations('ABCD', 2) ==> [AB, AC, AD, BC, BD, CD]. 
    #   https://www.geeksforgeeks.org/python/itertools-combinations-module-python-print-possible-combinations/
    # process each comibination, 
    #   if the cost > budget do not add to dictionary of possible soultions, 
    #   enjoyment as key and the array [combination, time, cost, enjoyment]
    # sort the dictionary by key (higher is better, descending val), 
    #   if the number of values assigned to 1 key is > 1 then we take the first solution
    # return the solution to main program

    #Activity name duration, cost, enjoyment level
    #Welcome-Dinner 2 40 75


    best_list = []
    highest_enjoyment = 0
    change_happened = False
    while change_happened == False:
        temp_list = []
        total_enjoyment = 0
        while time > 0 and budget > 0:
            for activity in activity_array:
                name = activity.name
                duration = activity.duration
                cost = activity.cost
                enjoyment = activity.enjoyment_level
                
                temp = temp.append((name, enjoyment))
                budget -= cost
                time -= duration
                total_enjoyment += enjoyment
        if total_enjoyment > highest_enjoyment:
            best_list = temp_list
            highest_enjoyment = total_enjoyment
            change_happened = True
        


    

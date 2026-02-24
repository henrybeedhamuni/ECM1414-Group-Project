def greedy_heuristic(activities, max_time, budget):

    # assign id's to each activity (integer 0-num of activities)
    ids = list() #create list for IDs
    for i in range(len(activities)):
        ids.append(i) #add each activity to the list of activityies

    cheapest = activities[0] #initial value for cheapest activity
    for activity in activities:
        if activity.cost < cheapest.cost: #if the next activity is cheaper then that is now the cheapest activity
            cheapest = activity 

    shortest = activities[0] #initial value for shortest activity
    for activity in activities:
        if activity.cost < shortest.duration: #if the next activity is shorter then that is now the shortest activity
            shortest = activity 

    if max_time // shortest.duration < budget // cheapest.cost: # Check which is smaler
        max_length = max_time // shortest.duration  #ceiling for the max combination length to test to
    else:
        max_length = budget // cheapest.cost #ceiling for the max combination length to test to

    if max_length > len(activities): #if max length is longer than the number of activities reduce the ceiling to the number of activities
        max_length = len(activities)

    calculated_activities_cost = []
    calculated_activities_duration = []
    best_solution = []

    # work out the enjoyment per hour and per cost and add them to a list 
    for activity in activities:
        enjoyment_per_hour = activity.enjoyment_level / activity.duration # calculate enjoyment per hour
        enjoyment_per_cost = activity.enjoyment_level / activity.cost # calculate enjoyment per cost
        calculated_activities_cost.append((activity, enjoyment_per_cost, activity.name)) # append cost enjoyment to it's list
        calculated_activities_duration.append((activity, enjoyment_per_hour, activity.name)) # append cost enjoyment to it's list
    
    # Sort them in reverse order
    calculated_activities_cost.sort(key=lambda tup: tup[1], reverse=True)  # sorts by enjoyment per cost
    calculated_activities_duration.sort(key=lambda tup: tup[1], reverse=True)  # sorts by enjoyment per duration

    # Reduce the list down to just the activites 
    cost_list = []
    index = 0
    while len(cost_list) < max_length:
        cost_list.append(calculated_activities_cost[index][0])
        index += 1

    # Same here reducing to just the activity
    duration_list = []
    index = 0
    while len(duration_list) < max_length:
        duration_list.append(calculated_activities_duration[index][0])
        index += 1

    # Work out the total for each list 
    duration_enjoyment = 0
    for x in range(len(duration_list)):
        duration_enjoyment += duration_list[x].enjoyment_level
    
    # Work out the total for the cost list 
    cost_enjoyment = 0
    for x in range(len(cost_list)):
        cost_enjoyment += cost_list[x].enjoyment_level
    
    best_solution = []

    # Make the best solution whichever list has the highest enjoyment
    if cost_enjoyment > duration_enjoyment:
        best_solution = cost_list
    else:
        best_solution = duration_list

    # Function to tally up each value
    def tally_up(best_solution):
        cost = 0
        time = 0
        enjoyment = 0
        for activity in best_solution: #adding up the cost, duration and enjoyment total for that combination
            cost += activity.cost
            time += activity.duration
            enjoyment += activity.enjoyment_level
        return cost, time, enjoyment

    # Tally each value
    cost, time, enjoyment = tally_up(best_solution)

    # Remove the lowest enjoyment activites until within budget and time constraints
    while cost > budget or time > max_time:
        lowest_enjoyment = best_solution[0]
        for activity in best_solution:
            if activity.enjoyment_level < lowest_enjoyment.enjoyment_level:
                lowest_enjoyment = activity
        best_solution.remove(lowest_enjoyment)
        cost, time, enjoyment = tally_up(best_solution)   

    # Convert list of activites to list of activity ids
    for x in range(0, len(activities)):
        for y in range(0, len(best_solution)):
            if type(best_solution[y])!= int:
                if activities[x].name == best_solution[y].name:
                    best_solution[y] = x

    best_solution = [tuple(sorted(best_solution)),cost,time,enjoyment] # Combination, cost, time, enjoyment

    return(best_solution) #returning the best solution found
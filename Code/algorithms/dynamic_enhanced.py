import copy

def dp_planner(activities, max_time, budget):

    n = len(activities)

    # dp[t][b] store the maximum enjoyment level that can be achieved with up to t hours and b budget
    dp = [[0] * (budget + 1) for _ in range(max_time + 1)]
    
    snapshots = []  # Save table state before adding each activity
    # to make it easier to figure out which activities were in the optimal solution
    
    
    # Add the activities to the table
    for i in range(n):
        # Save current state
        snapshots.append(copy.deepcopy(dp))
        
        activity = activities[i]
        
        # Go backwards to prevent using the same activity twice+ within one iteration
        for t in range(max_time, activity.duration - 1, -1):
            for b in range(budget, activity.cost - 1, -1):
                
                # If we include this activity,
                # calculate new enjoyment
                candidate = dp[t - activity.duration][b - activity.cost] + activity.enjoyment_level
                
                # If including it gives better enjoyment,
                # update the table
                if candidate > dp[t][b]:
                    dp[t][b] = candidate

    # Now find best enjoyment value
    best_enjoyment = 0
    best_t = 0
    best_b = 0
    for t in range(max_time + 1):
        for b in range(budget + 1):
            if dp[t][b] > best_enjoyment:
                best_enjoyment = dp[t][b]
                best_t = t
                best_b = b

    # Now we traceback through the activities using the snapshots to find which caused a change in the optimal solution.
    selected_ids = []
    t = best_t
    b = best_b
    for i in range(n - 1, -1, -1):
        activity = activities[i]
        prev = snapshots[i]  # table state before activity i was added
        if t >= activity.duration and b >= activity.cost:
            if dp[t][b] != prev[t][b]:  # activity i changed this cell => it was included
                selected_ids.append(i)
                t -= activity.duration
                b -= activity.cost
        dp = prev  # roll back for the next iteration

    selected_ids = tuple(reversed(selected_ids))  # restore ascending order

    # Calc totals
    total_cost = sum(activities[idx].cost for idx in selected_ids)
    total_time = sum(activities[idx].duration for idx in selected_ids)
    total_enjoyment = sum(activities[idx].enjoyment_level for idx in selected_ids)
    
    best_solution = [selected_ids, total_cost, total_time, total_enjoyment]

    return best_solution
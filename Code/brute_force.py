def brute_force(file_info,time,budget):
    # assign id's to each activity (integer 0-num of activities)
    # run the combinations alorithm
    #itertools.combinations(iterable, r): It returns r-length tuples in sorted order with no repeated elements. For Example, combinations('ABCD', 2) ==> [AB, AC, AD, BC, BD, CD]. https://www.geeksforgeeks.org/python/itertools-combinations-module-python-print-possible-combinations/
    # process each comibination, if the cost > budget do not add to dictionary of possible soultions, enjoyment as key and the array [combination, time, cost, enjoyment]
    # sort the dictionary by key (higher is better, descending val), if the number of values assigned to 1 key is > 1 then we take the first solution
    # return the solution to main program
    



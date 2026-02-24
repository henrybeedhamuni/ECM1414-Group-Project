from time import time
import matplotlib.pyplot as plt
import numpy as np
from algorithms.brute_force import brute_force_planner
from algorithms.enhanced_brute_force import enhanced_brute_force_planner
from algorithms.dynamic import dp_planner
from algorithms.greedy_heuristic import greedy_heuristic
from utils.read_input_file import read_input_file

def performance_analysis():
    brute_force_time = []
    dynamic_time = []
    files_list = np.array([
        "input_5.txt",
        "input_10.txt",
        "input_15.txt",
        "input_20.txt",
        "input_25.txt",
        "input_26.txt",
        "input_27.txt",])

    # Perform for each file 
    for filename in files_list:
        activities, max_duration, max_budget = read_input_file('../Input_Files/'+filename)

        # Time Brute force
        start_time = time.time()
        brute_force_planner(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        brute_force_time.append(time_taken)
        print(f"Regular brute force {filename} completed in {time_taken}")

        # Time dynamic
        start_time = time.time()
        dp_planner(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        dynamic_time.append(time_taken)
        print(f"Dynamic {filename} completed in {time_taken}")

    # Plot both
    fig, (lineplot, barplot) = plt.subplots(1, 2, figsize=(12, 5))
    lineplot.plot([5,10,15,20,25,26,27], dynamic_time)
    lineplot.plot([5,10,15,20,25,26,27], brute_force_time)
    lineplot.set_yscale('log')
    lineplot.set_title("Dynamic vs Brute force efficiency analysis")
    lineplot.set_ylabel("Time taken to execute (seconds)")
    lineplot.set_xlabel("Number of inputs")
    lineplot.legend(["Dynamic", "Brute Force"], loc="upper left")
    #Plot a bar chart for the speed up factor
    speed_factor = []
    for x in range(len(dynamic_time)):
        speed_factor.append(dynamic_time[x]/brute_force_time[x])

    barplot.bar([5,10,15,20,25,26,27], speed_factor)
    barplot.set_ylabel("Speedup factor (Dynamic type / Brute force time)")
    barplot.set_xlabel("Number of inputs")
    barplot.set_title("How the speedup factor changes at different numbers of inputs")

    plt.tight_layout()
    plt.show()

def performance_analysis_heuristic():

    brute_force_time = []
    dynamic_time = []
    heuristic_time = []
    files_list = np.array([
        "input_5.txt",
        "input_10.txt",
        "input_15.txt",
        "input_20.txt",
        "input_25.txt",
        "input_26.txt",
        "input_27.txt",])

    # Perform for each file 
    for filename in files_list:
        activities, max_duration, max_budget = read_input_file('../Input_Files/'+filename)

        # Time Brute force
        start_time = time.time()
        brute_force_planner(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        brute_force_time.append(time_taken)
        print(f"Regular brute force {filename} completed in {time_taken}")

        # Time dynamic
        start_time = time.time()
        dp_planner(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        dynamic_time.append(time_taken)
        print(f"Dynamic {filename} completed in {time_taken}")

        # Time Heuristic
        start_time = time.time()
        greedy_heuristic(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        heuristic_time.append(time_taken)
        print(f"Heuristic {filename} completed in {time_taken}")

    # Plot both
    fig, (plot1, plot2) = plt.subplots(1, 2, figsize=(12, 5))
    plot1.plot([5,10,15,20,25,26,27], dynamic_time)
    plot1.plot([5,10,15,20,25,26,27], brute_force_time)
    plot1.plot([5,10,15,20,25,26,27], heuristic_time)
    plot1.set_yscale('log')
    plot1.set_title("Dynamic vs Brute force vs Heuristic efficiency analysis")
    plot1.set_ylabel("Time taken to execute (seconds)")
    plot1.set_xlabel("Number of inputs")
    plot1.legend(["Dynamic", "Brute Force", "Heuristic"], loc="upper left")


    dynamic_time = []
    heuristic_time = []
    files_list = np.array([
        "input_5.txt",
        "input_10.txt",
        "input_15.txt",
        "input_20.txt",
        "input_25.txt",
        "input_26.txt",
        "input_27.txt",
        "input_28.txt",
        "input_29.txt",
        "input_100.txt",
        "input_200.txt",
        "input_500.txt",
        "input_1000.txt",])

    # Perform for each file 
    for filename in files_list:
        activities, max_duration, max_budget = read_input_file('Input_Files/'+filename)

        # Time dynamic
        start_time = time.time()
        dp_planner(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        dynamic_time.append(time_taken)
        print(f"Dynamic {filename} completed in {time_taken}")

        # Time Heuristic
        start_time = time.time()
        greedy_heuristic(activities,max_duration,max_budget)
        end_time = time.time()

        # Append to array
        time_taken = end_time - start_time
        heuristic_time.append(time_taken)
        print(f"Heuristic {filename} completed in {time_taken}")

    # Plot both
    plot2.plot([5,10,15,20,25,26,27,28,29,100,200,500,1000], dynamic_time)
    plot2.plot([5,10,15,20,25,26,27,28,29,100,200,500,1000], heuristic_time)
    plot2.set_yscale('log')
    plot2.set_title("Dynamic vs Heuristic efficiency analysis")
    plot2.set_ylabel("Time taken to execute (seconds)")
    plot2.set_xlabel("Number of inputs")
    plot2.legend(["Dynamic", "Heuristic"], loc="upper left")


    plt.show()

def performance_analysis_enjoyment():

    brute_force_values = []
    dynamic_values = []
    heuristic_values = []
    files_list = np.array([
        "input_5.txt",
        "input_10.txt",
        "input_15.txt",
        "input_20.txt",
        "input_25.txt",
        "input_26.txt",
        "input_27.txt",])

    # Perform for each file 
    for filename in files_list:
        activities, max_duration, max_budget = read_input_file('../Input_Files/'+filename)

        # Get total enjoyment
        value = brute_force_planner(activities,max_duration,max_budget)

        # Append to array
        brute_force_values.append(value[3])

        # Get total enjoyment
        value = dp_planner(activities,max_duration,max_budget)

        # Append to array
        dynamic_values.append(value[3])

        # Get total enjoyment
        value = greedy_heuristic(activities,max_duration,max_budget)

        # Append to array
        heuristic_values.append(value[3])

    # Plot both
    fig, (plot1, plot2) = plt.subplots(1, 2, figsize=(12, 5))
    plot1.plot([5,10,15,20,25,26,27], dynamic_values)
    plot1.plot([5,10,15,20,25,26,27], brute_force_values)
    plot1.plot([5,10,15,20,25,26,27], heuristic_values)
    plot1.set_title("Dynamic vs Brute force vs Heuristic efficiency analysis")
    plot1.set_ylabel("Total enjoyment")
    plot1.set_xlabel("Number of inputs")
    plot1.legend(["Dynamic", "Brute Force", "Heuristic"], loc="upper left")


    dynamic_values = []
    heuristic_values = []
    files_list = np.array([
        "input_5.txt",
        "input_10.txt",
        "input_15.txt",
        "input_20.txt",
        "input_25.txt",
        "input_26.txt",
        "input_27.txt",
        "input_28.txt",
        "input_29.txt",
        "input_100.txt",
        "input_200.txt",
        "input_500.txt",
        "input_1000.txt",])

    # Perform for each file 
    for filename in files_list:
        activities, max_duration, max_budget = read_input_file('Input_Files/'+filename)

        # Get total enjoyment
        value = dp_planner(activities,max_duration,max_budget)

        # Append to array
        dynamic_values.append(value[3])

        # Get total enjoyment
        value = greedy_heuristic(activities,max_duration,max_budget)

        # Append to array
        heuristic_values.append(value[3])

    # Plot both
    plot2.plot([5,10,15,20,25,26,27,28,29,100,200,500,1000], dynamic_values)
    plot2.plot([5,10,15,20,25,26,27,28,29,100,200,500,1000], heuristic_values)
    plot2.set_title("Dynamic vs Heuristic efficiency analysis")
    plot2.set_ylabel("Total enjoyment value")
    plot2.set_xlabel("Number of inputs")
    plot2.legend(["Dynamic", "Heuristic"], loc="upper left")


    plt.show()

performance_analysis_heuristic()
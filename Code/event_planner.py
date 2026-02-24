import os
import sys
import time
from typing import List, Tuple
import time

from read_input_file import read_input_file

# --- Import your brute_force and dynamic programming modules here when implemented. Uncomment the lines below:
from brute_force import brute_force_planner
from enhanced_brute_force import enhanced_brute_force_planner
# from dynamic import dp_planner
from dynamic import dp_planner

#Import Greedy Heuristic
from greedy_heuristic import greedy_heuristic

#Import Performance analysis:
# from performance_analysis import performance_analysis


class Activity:
  """Represents a single activity/event"""
  def __init__(self, name, duration, cost, enjoyment_level):
    self.name = name
    self.duration = duration  # in hours
    self.cost = cost  # in £ pounds
    self.enjoyment_level = enjoyment_level # positive integer

  def __str__(self):
    return f"Activity: {self.name}, Duration: {self.duration} hours, Cost: £{self.cost}, Enjoyment Level: {self.enjoyment_level}"

      
def main():
  # Read filename from command line argument (e.g. python Code/event_planner.py ./Input_Files/input_small.txt)
  filename = sys.argv[1] if len(sys.argv) > 1 else '../Input_Files/input_small.txt'
  activities, max_duration, max_budget = read_input_file(filename)
  
  # Use brute-force or dynamic programming planner here
  # --- Begin brute force usage
  start = time.time()
  bf_output = brute_force_planner(activities,max_duration,max_budget)
  end = time.time()
  bf_output.append("{:.6f}".format(end-start))

  start = time.time()
  bf_output_e = enhanced_brute_force_planner(activities,max_duration,max_budget)
  end = time.time()
  bf_output_e.append("{:.6f}".format(end-start))
  # --- End of brute force usage
  
  
  # --- Begin dynamic programming usage
  start = time.time()
  dp_output = dp_planner(activities, max_duration, max_budget)
  end = time.time()
  dp_output.append("{:.6f}".format(end-start))

  # --- End of dynamic programming usage

  # --- Begin Greedy Heuristic usage
  start = time.time()
  gh_output = greedy_heuristic(activities, max_duration, max_budget)
  end = time.time()
  gh_output.append("{:.6f}".format(end-start))

  # --- End of Greedy Heuristic  usage
  
  solutions = [bf_output,bf_output_e,dp_output,gh_output]
  # Print read activities and constraints
  # returns[[solution],[cost],[time],[enjoyment],[execution time]]
  print("========================================")
  print("EVENT PLANNER - RESULTS")
  print("========================================")
  print(f"Input File: {filename}")
  print(f"Available Time: {max_duration} Hours")
  print(f"Available Budget: £{max_budget}")

  print(" --- Standard Brute Force Algorithm --- ")
  print("Selected Activities: ")
  for index in solutions[0][0]:
      print(f"  {activities[index]}")
  print(f"Total Enjoyment: {solutions[0][3]}\nTotal Time Used: {solutions[0][2]} hours\nTotal Cost: £{solutions[0][1]}")
  print(f"\nExecution Time: {solutions[0][4]} Seconds")

  print("\n\n --- Enhanced Brute Force Algorithm --- ")
  print("Selected Activities: ")
  for index in solutions[1][0]:
      print(f"  {activities[index]}")
  print(f"Total Enjoyment: {solutions[1][3]}\nTotal Time Used: {solutions[1][2]} hours\nTotal Cost: £{solutions[1][1]}")
  print(f"\nExecution Time: {solutions[1][4]} Seconds")

  print("\n\n --- Standard Dynamic Programming Algorithm --- ")
  print("Selected Activities: ")
  for index in solutions[2][0]:
      print(f"  {activities[index]}")
  print(f"Total Enjoyment: {solutions[2][3]}\nTotal Time Used: {solutions[2][2]} hours\nTotal Cost: £{solutions[2][1]}")
  print(f"\nExecution Time: {solutions[2][4]} Seconds")

  print("\n\n --- Greedy Heuristic Algorithm --- ")
  print("Selected Activities: ")
  for index in solutions[3][0]:
      print(f"  {activities[index]}")
  print(f"Total Enjoyment: {solutions[3][3]}\nTotal Time Used: {solutions[3][2]} hours\nTotal Cost: £{solutions[3][1]}")
  print(f"\nExecution Time: {solutions[3][4]} Seconds")
if __name__ == "__main__":
  main()
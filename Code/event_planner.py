import sys
from typing import List, Tuple
# --- Import your brute_force and dynamic programming modules here when implemented. Uncomment the lines below:
from brute_force import brute_force_planner
# from dynamic import dp_planner

class Activity:
  """Represents a single activity/event"""
  def __init__(self, name, duration, cost, enjoyment_level):
    self.name = name
    self.duration = duration  # in hours
    self.cost = cost  # in £ pounds
    self.enjoyment_level = enjoyment_level # positive integer

  def __str__(self):
    return f"Activity: {self.name}, Duration: {self.duration} hours, Cost: £{self.cost}, Enjoyment Level: {self.enjoyment_level}"
  
def read_input_file(filename: str) -> Tuple[List[Activity], int, int]:
  """Read csv file of input activities and constraints"""
  try:
    with open(filename, 'r') as f:
      lines = f.readlines()
    
    n = int(lines[0].strip())
    max_duration, max_budget = map(int, lines[1].strip().split())
    
    activities = []
    for i in range(2, 2 + n):
      parts = lines[i].strip().split()
      name = parts[0]
      duration = int(parts[1])
      cost = int(parts[2])
      enjoyment_level = int(parts[3])
      activities.append(Activity(name, duration, cost, enjoyment_level))
    
    return activities, max_duration, max_budget
      
  except FileNotFoundError:
      print(f"Error: File '{filename}' not found.")
      sys.exit(1)
  except Exception as e:
      print(f"Error reading file: {e}")
      sys.exit(1)
      
def main():
  # Read filename from command line argument (e.g. python Code/event_planner.py ./Input_Files/input_small.txt)
  filename = sys.argv[1] if len(sys.argv) > 1 else '../Input_Files/input_small.txt'
  activities, max_duration, max_budget = read_input_file(filename)
  
  # Use brute-force or dynamic programming planner here
  # --- Begin brute force usage
  bf_output = brute_force_planner(activities,max_duration,max_budget)
  print(bf_output)
  
  # --- End of brute force usage
  
  
  # --- Begin dynamic programming usage
  
  
  
  # --- End of dynamic programming usage
  
  # Print read activities and constraints
  print(f"Max Duration: {max_duration} hours, Max Budget: £{max_budget}")
  for activity in activities:
    print(activity)

if __name__ == "__main__":
  main()
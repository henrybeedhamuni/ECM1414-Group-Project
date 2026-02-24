from typing import List, Tuple
import sys

from Classes.Activity import Activity

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
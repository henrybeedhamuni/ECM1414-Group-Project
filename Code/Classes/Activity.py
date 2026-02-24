class Activity:
  """Represents a single activity/event"""
  def __init__(self, name, duration, cost, enjoyment_level):
    self.name = name
    self.duration = duration  # in hours
    self.cost = cost  # in £ pounds
    self.enjoyment_level = enjoyment_level # positive integer

  def __str__(self):
    return f"Activity: {self.name}, Duration: {self.duration} hours, Cost: £{self.cost}, Enjoyment Level: {self.enjoyment_level}"
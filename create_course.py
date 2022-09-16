import random
import numpy as np

class Hole:

  def __init__(self,length,sand,water,width,difficulty):
    self.length = random.choice(length[difficulty])
    self.sand = random.choice(sand[difficulty])
    self.water = random.choice(water[difficulty])
    self.width = random.choice(width)
    self.map = []
    self.cells = []
    self.width_marker = []
    
  def create_hole(self):
    for x in range(0,self.sand):
      self.cells.append("B")
  
    for x in range(0,self.water):
      self.cells.append("W")
  
    for x in range(1,(self.length*self.width)-len(self.cells)+1):
      self.cells.append("F")

    for x in range(self.width):
      self.width_marker.append(x)

    self.cells = np.array(self.cells)
    random.shuffle(self.cells)    
    self.map = np.array_split(self.cells,len(self.cells)/self.width)
    self.map[-1][random.randrange(0,len(self.map[-1]))] = "T"
    self.map[0][random.randrange(0,len(self.map[-1]))] = "H"
    
    


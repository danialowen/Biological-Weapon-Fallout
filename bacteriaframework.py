import random

class Bacteria:
    
    def __init__ (self, bacteria, density):
        self.y = 150
        self.x = 50
        self.h = 75
        self.bacteria = bacteria
        self.density = density
    
    # Create a function controlling the height of the bacteria by probability.
    # If the bacteria >= height of the building, there is 20% chance of gaining a metre in height,
    # 10% chance of staying the same height and 70% of falling. When bacteria is lower than,
    # the building height, the bacteria falls one metre per second until reaching the ground    
    def turbulence(self):
        
        randomFall = random.random()
        
        if self.h >= 75:
            
            if randomFall <= 0.2:
                self.h = self.h + 1
                
            elif randomFall <= 0.3:
                self.h = self.h
                
            else:
                self.h = self.h - 1
                
        elif self.h > 0:
            self.h = self.h - 1
            
        elif self.h <= 0: 
            self.h =  0
            
     
    # Create a function which controls which direction (x and y) the bacteria moves.
    # When bacteria hasn't reached the ground, 5% of moving west,
    # 10% of moving either north or south and 75% chance of moving east.     
    def move_by_wind(self):
        
        randomWind = random.random()
        
        if self.h > 0:
            
            if randomWind <= 0.05:
                self.x = self.x - 1
                
            elif randomWind <= 0.15:
                self.y = self.y + 1
                
            elif randomWind <= 0.25:
                self.y = self.y - 1
                
            else:
                self.x = self.x + 1
                
        else:
            self.x = self.x
            self.y = self.y

    # A function which creates a density map by adding a value of 1 for each bacteria's
    # final positions (height equal to 0)                
    def dens_tot(self, density):
        if self.h == 0:
            self.density[self.y][self.x] += 1
            
            
            
        
        
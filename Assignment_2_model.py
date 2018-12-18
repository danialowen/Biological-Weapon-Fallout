# Leeds GOEG5995M Assignment 2 - Bacterial Bomb

# Import the necessary packages and frameworks
import matplotlib.pyplot 
import csv
import bacteriaframework   # Contains the Bacteria class (bacteriaframework.py in zip folder)

# Set the model conditions. Create a variable called "bacteria" ready to append values.
# Set the number of agents (individual bacteria), the height of the building (where the bomb is let off)
# and the number of iterations (time elapsed in seconds)
bacteria = []
num_of_bacteria = 5000
building_height = 75
num_of_iterations = 2000

# Create a density csv file and append with values of 0 in a 300x300 grid
f = open('wind.raster', newline='')
density = []
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist=[]
    for value in row:
        value = 0
        rowlist.append(value)
    density.append(rowlist)
f.close()

# Find the position of the bomb in the "wind.raster" file. Bomb is labelled with a value of 255
f1 = open('wind.raster', newline='') 
reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC)
for i, row in enumerate(reader):
    for j, bomb in enumerate(row):
        if bomb == 255:
            x0= j
            y0= i
                 
print('Bomb', x0,y0)


#Create a figure to display the final positions of the bacteria  
fig, ax = matplotlib.pyplot.subplots(figsize=(7, 7))

# For 5000 bacteria, append their position and density from the bacteriaframework
# Check to see if they have been appended in the variable explorer
for i in range(num_of_bacteria):
    bacteria.append(bacteriaframework.Bacteria(bacteria, density))


# Call on the functions from the Bacteria class in bacteriaframework and 
# make all agents loop for a set number of times, determined by the number of iterations        
for k in range(num_of_iterations):
    for i in range(num_of_bacteria):
        bacteria[i].turbulence()        #Probability of bacteria going higher/staying same height/falling
        bacteria[i].move_by_wind()      #Probability of the wind direction acting on movement of bacteria 
        
for i in range(num_of_bacteria):
    bacteria[i].dens_tot(density) #Give the environment a density value for where the bacteria fall


# Create a scatter plot with the final positions of all bacteria shown by points,
# Show the original position of the bomb shown by a black, star marker             
for i in range(num_of_bacteria):
    ax.scatter(x0, y0, marker="*", color="black")
    ax.scatter(bacteria[i].x,bacteria[i].y, marker=".", s=10)
    matplotlib.pyplot.xlabel('Longitude')
    matplotlib.pyplot.ylabel('Latitude')
    matplotlib.pyplot.title('Biological Weapon: Bacteria Spread')
    
#Set the axis limits and show/save the figure
ax.set_xlim(0,300)
ax.set_ylim(0,300)
matplotlib.pyplot.show()
#fig.savefig('5000_Bacteria.png') #if you wanted to save 

#Save the figure as another image file but zoomed in 
ax.set_xlim(0,200)
ax.set_ylim(100,200)
matplotlib.pyplot.show()
# fig.savefig('Zoomed_5000_Bacteria1.png') #if you wanted to save a zoomed in version        


#plot and show a density map of where the bacteria ends up (zoomed in) 
fig, ax1 = matplotlib.pyplot.subplots(figsize=(7, 7))
ax1.set_ylim(120,180)
ax1.set_xlim(70,130)
matplotlib.pyplot.imshow(density, cmap="Greens")
matplotlib.pyplot.colorbar(label='Bacteria Density')
matplotlib.pyplot.xlabel('Longitude')
matplotlib.pyplot.ylabel('Latitude')
matplotlib.pyplot.title('Biological Weapon: Bacteria Density')


#save the density map as a text file
file_out = open('density_out.txt', 'w', newline='') 
writer = csv.writer(file_out)
for row in density:		
	writer.writerow(row)		
file_out.close()        



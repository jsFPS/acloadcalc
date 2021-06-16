
#take in inputs
#ask for number of external walls
#ask for number of internal walls
#asks for teh room height
# asks if floor beneath is ground soil or unconditioned space
# asks if roof above is open to sky or unconditioned space

##goes to first external wall
# asks for its direction
#asks for its length
# asks for window lenght total window lengths

# asks for windhow height


#goes to next external wall and does the same



#then asks for length of internal wall

# works out infiltration and latent heat load
# asks for number of people in the room

# works out the total load and then tells yu a possible AC unit size

# asks for name of room to output to a json file

#added a comment here for github test .
# added a second comment now
import numpy as np
import extwall
import roof
import other

#coolload(RH, ISROOF, ISGROUND,WLDIR, WNDIR, WLLEN, WNA,TIN, TOUT, PPL, COMP)

#Room Configuration

#Room height in meters
room_height = 2

#Is the roof an exterior boundary? Is it exposed to the sun?
extroof = True # True if yes, False if not

#Is the room on ground floor? True or False?
groundfloor = False

#All wall lengths in meters both exterior and interior wall
wall_directions = {
        'north' : True,
        'west' : True,
        'south' : False,
        'east' : False
            }
#Exterior window directions
win_directions = {
        'north' : True,
        'west' : True,
        'south' : False,
        'east' : False
            }

#wall lengths in meters ( both exterior and interior walls)
wall_lengths = {
        'north' : 10,
        'west' : 10,
        'south' : 10,
        'east' : 10 
            }

#window areas in sq. meters
win_areas = {
        'north' : 1,
        'west' : 1,
        'south' : 0,
        'east' : 0
            }


#Temperatures in degrees Celcius
Tin = 22
Tout = 40

#Number of people in the room
people = 3

#Number of computers in the room
computers = 3




partition_length = 0
floor_area = wall_lengths[max(wall_lengths)]*wall_lengths[min(wall_lengths)]
room_volume = floor_area*room_height


walls = np.zeros((12, 24))
matrix = np.zeros((12, 24))
roofmatrix = np.zeros((12,24))

for direc, extr in wall_directions.items():
        if extr == True:
            matrix = extwall.extwallcalc(direc, wall_lengths[direc], room_height, win_areas[direc], Tin, Tout)
            walls = walls + matrix
            
        if extr == False:
            partition_length = partition_length + wall_lengths[direc]

if extroof == True:
    roofmatrix = roof.roofcalc(floor_area, Tin, Tout)
    
total = roofmatrix + walls

max_sensible = np.max(total)
partition_size = room_height*partition_length


other_loads = other.othercalc(Tin, Tout, room_volume, computers, people, partition_size, floor_area, groundfloor)

total_sensible = other_loads[0] + max_sensible
total_latent = other_loads[1]
total_cooling_load = total_sensible + total_latent

SHR = total_sensible / total_cooling_load 

print('Total Cooling Load is : ', (str("%.2f" % (total_cooling_load/10))), 'kW.')
print('Total Sensible Load is: ', (str("%.2f" % (total_sensible/10))), 'kW.')
print('Total Latent Load is: ' , (str("%.2f" % (total_latent/10))), 'kW.')
print('Sensible heat ratio is: ', (str("%.2f" % SHR)))

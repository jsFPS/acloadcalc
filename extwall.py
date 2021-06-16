def extwallcalc(direction, wall_length, room_height, win_area, Tin, Tout):
    
    #import pandas as pd
    import numpy as np
    
    #inputs
    #Tin = 22 #inside temperature in degC
    #Tout = 40 #outside temperature in degC
    K = 0.83 #unknown factor
    U_wall = 1.57 #U value for walls
    U_win = 2.8 #U value for windows
    T1 = 25.5
    T2 = 29.4
    wall_area = wall_length*room_height - win_area# - win_area 
    SC = 0.7
    
    if direction == 'north':
        select = 0
    elif direction == 'east':
        select = 4
    elif direction == 'south':
        select  = 8
    else:
        select = 12
    
    
    table1 = np.loadtxt('table1.txt')
    table2 = np.loadtxt('table2.txt')
    table3 = np.loadtxt('table3.txt')
    table4 = np.loadtxt('table4.txt')
    table5 = np.loadtxt('table5.txt')
    table6 = np.loadtxt('table6.txt')
    
    a = np.array(table1[select,:])
    d = np.transpose([a])
    d = np.transpose(d)
    b = np.array(table2[:, select])
    
    f = np.array(table3[:,select])
    g = np.array(table6[select])
    
    
    x = np.shape(a)
    e = np.zeros((1, x[0]))
    
    sunlitwalls = np.zeros((1, x[0]))
    sunlitwins = np.zeros((1, x[0]))
    sunwincond = np.zeros((1, x[0]))
    e = np.zeros((1, x[0]))
    h = np.zeros((1, x[0]))
    k = np.zeros((1, x[0]))
    
    h[0,:] = U_win*win_area*(table5[:] + T1 - T2 + Tout - Tin)
    sunwincond = h
    
    for j in range(0,np.shape(f)[0]):
        for i in range(0,np.shape(e)[1]):
            e[0,i] = U_wall*wall_area*((d[0,i] + b[j])*K + T1 - T2 + Tout - Tin)
            k[0,i] = g[i]*f[j]*SC
            
        sunlitwalls = np.append(sunlitwalls, e, axis=0)
        sunlitwins = np.append(sunlitwins, k, axis=0)
        sunwincond = np.append(sunwincond, h , axis=0)
    
    sunlitwalls = np.delete(sunlitwalls, 0, 0)
    sunlitwins = np.delete(sunlitwins, 0, 0)
    sunwincond = np.delete(sunwincond, 0,0)    
    
   
    
    total = sunlitwalls + sunlitwins + sunwincond
  
    return total
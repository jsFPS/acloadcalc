def roofcalc(floor_area, Tin, Tout):  
    
    import numpy as np
        
    table2 = np.loadtxt('table2.txt')
    a = np.array(table2[:, 16])
        
    T1 = 25.5
    T2 = 29.4
    K = 0.83
    U_ceiling = 0.7
        
    #Tin = 22
    #Tout = 40
    #floor_area = 100
    
        
    r = a - a
    roofmatrix = r
        
    for j in range(0,12):
        r[j] = U_ceiling*floor_area*((23 + a[j])*K + T1 - T2 + Tout - Tin)
          #  print(r[j])
        
    for i in range(0,23):
        roofmatrix = np.vstack((roofmatrix, r))
            
    roofmatrix = np.transpose(roofmatrix)    
   
    return roofmatrix
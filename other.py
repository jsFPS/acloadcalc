def othercalc(Tin, Tout, room_volume, computers, people, partition_size, floor_area, groundfloor):
    
    #ventilation and infiltration load
    sensible_vent_infilt = room_volume*4.5*1.19*15/3.6
    latent_vent_infilt = room_volume*4.5*1.19*42/3.6
    
    #power equipment load
    sensible_equipment_load = computers*500
    
    #people in room
    sensible_people = people*75
    latent_people = people*55
    
    #lighting load
    sensible_lighting = 1.2*35*floor_area
    
    
    sensible_groundfloor = 0
    #unconditioned space 
    if groundfloor == False:
        sensible_groundfloor = 1.97*floor_area*(Tout - 0.5*(Tout + Tin))
    
    sensible_partition = 2.8*partition_size*(Tout - 0.5*(Tout + Tin))
    
    
    
    
    #total load
    sensible_other_total = sensible_vent_infilt + sensible_equipment_load \
                            + sensible_people + sensible_lighting \
                            + sensible_groundfloor \
                            + sensible_partition
    
    latent_other_total = latent_vent_infilt + latent_people
    
    
    return sensible_other_total, latent_other_total
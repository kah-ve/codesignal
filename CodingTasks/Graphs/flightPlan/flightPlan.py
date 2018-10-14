def flightPlan(time, sour, des): #dynamic program
    
    def toMinutes(t):
        t = t.split(':')
        hours = t[0]
        minutes = t[1]
        return int(hours) * 60 + int(minutes)
    
    path = {}
    # initialize the beginning node
    path[sour] = -60 # initialize at -60 since the 1 hour delay does not matter for first flight
    k = float("inf") # key to use to check if value exists in dictionary
    
    # sort according to the times of the flights so that we start considering all nodes that are
    # possible after the source has been reached
    time = sorted(time, key=lambda x: x[-2]) 
    
    for dep_loc, arr_loc, dep_time, arr_time in time:
        if path.get(dep_loc, k) + 60 <= toMinutes(dep_time): 
        # if the current flights departure time is even reachable from the path we can take
            path[arr_loc] = min(path.get(arr_loc, k), toMinutes(arr_time))
            # the destination time's earliest reachable value is now either its the previous value
            # or this new value
    
    # ran through times, picked earliest times possible to reach each location
    def convertBack(t):
        h, t = divmod(t, 60)
        return "{:02}:{:02}".format(h, t)
    
    if path.get(des):
        return convertBack(path[des])
    else:
        return "-1"
    
        

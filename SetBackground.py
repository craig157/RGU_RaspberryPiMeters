#Function For setting LED Display background depending on the Temp passed into argument
def BackColour_func(x):
    if x < 5:
        return (0,0,153) #darkBlue
    elif 5.1 <= x <= 10:
        return (0,0,255) #blue
    elif 10.1 <= x <=15:
        return (0,255,255) #lightBlue
    elif 15.1 <= x <=20:
        return (0,255,0) #green
    elif 20.1 <= x <=25:
        return (191,255,0) #paleGreen
    elif 25.1 <= x <=30:
        return (255,191,0) #orange
    elif 30.1 <= x <=35:    
        return (255,102,0) #darkOrange
    elif x >= 35.1:
        return (255,0,0) #red
    else:
        return (255, 255, 255) #white
     
                                    
                                    
                                    
                                    
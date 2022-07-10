def add_time(start, duration,day=None):

    #Split the string from start into 2 parts: time and am/pm
    str_start = start.split(" ")    #str_start[0]=11:06     str_start[1]=PM
    
    #Split the first string into 2 parts again: hour and minutes
    num_start = str_start[0].split(":")
    
    #split the duration into 2 parts: hour and minutes
    num_duration = duration.split(":")
    
    #Total sum of the minutes
    new_minutes = int(num_start[1]) + int(num_duration[1])
    new_day = 0
    i=0
    list_days = ("Monday","tuesday","Wednesday","Thursday","Friday","saturDay","Sunday")
    
    #Check the total minutes. If more than 60, +1 to add_hour.
    if new_minutes > 60:
    
        new_minutes_1 = new_minutes - 60
        add_hour = 1
        
        #If minutes are less than 10, add a string of "0" in front.
        if len(str(new_minutes_1)) == 1:
        
            new_minutes_2 = "0" + str(new_minutes_1)
        
        else:
        
            new_minutes_2 = str(new_minutes_1)
        
    else:
    
        new_minutes_1 = new_minutes
        add_hour = 0
        
        if new_minutes_1 <10:
        
            new_minutes_2 = "0" + str(new_minutes_1)
            
        else:
        
            new_minutes_2 = str(new_minutes_1)
    
    #Total sum of the hour including add_hour by round up from minutes.
    new_hour = int(num_start[0]) + int(num_duration[0]) + add_hour
    
    #In case day is not given.
    try:
    
        day_position = list_days.index(day)
        
    except:
    
        pass
    
    #If start starts from AM,
    if str_start[1] == "AM":
        
        if new_hour < 12:
            
            new_hour_1 = new_hour
            new_ampm = str_start[1]
            new_day_1 = ""
            
            if day is None:
            
                update_day = ""
            
            else:
            
                update_day = ", "+day
            
        elif 12 <= new_hour < 24:
        
            new_hour_1 = new_hour - 12
            
            if new_hour_1 == 0:
                
                new_hour_1 = 12
            
            else:
            
                pass
                
            new_ampm = "PM"
            new_day_1 = ""
            
            if day is None:
            
                update_day = ""
            
            else:
            
                update_day = ", "+day
            
        elif 24 <= new_hour < 36:
            
            new_hour_1 = new_hour - 24
            
            if new_hour_1 == 0:
                
                new_hour_1 = 12
            
            else:
            
                pass
                
            new_ampm = "AM"
            new_day_1 = " (next day)"
            
            if day is None:
            
                update_day = ""
            
            else:
            
                update_day = ", "+list_days[day_position+1]
        
        elif 36 <= new_hour < 48:
            
            new_hour_1 = new_hour - 36
            
            if new_hour_1 == 0:
                
                new_hour_1 = 12
            
            else:
            
                pass
                
            new_ampm = "PM"
            new_day_1 = " (next day)"
            
            if day is None:
            
                update_day = ""
            
            else:
            
                update_day = ", "+list_days[day_position+1]
        
        else:
            
            total_days = new_hour / 24
            str_total_days = str(total_days).split(".")
            
            if round(total_days) < total_days:
                
                new_hour_1 = new_hour - int(str_total_days[0])*24
                
                if new_hour_1 == 0:
                
                    new_hour_1 = 12
            
                else:
                
                    pass
                
                new_ampm = "AM"
                new_day_1 = " (" + str_total_days[0] + " days later)"
                
                if day is None:
                
                    update_day = ""
            
                else:
                
                    update_day = ", "+list_days[day_position+int(str_total_days[0])]
                
            elif round(total_days) > total_days:
                
                new_hour_1 = new_hour - int(str_total_days[0])*24 - 12
                
                if new_hour_1 == 0:
                
                    new_hour_1 = 12
            
                else:
                
                    pass
                
                new_ampm = "PM"
                new_day_1 = " (" + str_total_days[0] + " days later)"
                
                #Check if day is None.
                if day is None:
                
                    update_day = ""
            
                else:
                
                    update_day = ", "+list_days[day_position+int(str_total_days[0])]
    
    #If start starts from PM:
    else:
        
        if new_hour < 12:
        
            new_hour_1 = new_hour
            new_ampm = str_start[1]
            new_day_1 = ""
            
            if day is None:
            
                update_day = ""
            
            else:
                update_day = ", "+day
            
        elif 12 <= new_hour < 24:
            
            new_hour_1 = new_hour - 12
            
            if new_hour_1 == 0:
                
                new_hour_1 = 12
            
            else:
            
                pass
                
            new_ampm = "AM"
            new_day_1 = " (next day)"
            
            if day is None:
            
                update_day = ""
            
            else:
            
                update_day = ", "+list_days[day_position+1]
            
        elif 24 <= new_hour < 36:
        
            new_hour_1 = new_hour - 24
            
            if new_hour_1 == 0:
                
                new_hour_1 = 12
            
            else:
            
                pass
                
            new_ampm = "PM"
            new_day_1 = " (next day)"
            
            if day is None:
            
                update_day = ""
            
            else:
            
                update_day = ", "+list_days[day_position+1]
            
        elif new_hour >= 36:
            
            total_days = new_hour / 24
            str_total_days = str(total_days).split(".")
            
            if round(total_days) < total_days:
                
                new_hour_1 = new_hour - int(str_total_days[0])*24
                
                if new_hour_1 == 0:
                
                    new_hour_1 = 12
            
                else:
                
                    pass
                
                new_ampm = "PM"
                new_day_1 = " (" + str(round(total_days)) + " days later)"
                
                if day is None:
                
                    update_day = ""
            
                else:
                
                    update_day = ", "+list_days[day_position+int(str_total_days[0])]
                
            elif round(total_days) > total_days:
                
                new_hour_1 = new_hour - int(str_total_days[0])*24 - 12
                
                if new_hour_1 == 0:
                
                    new_hour_1 = 12
            
                else:
                    pass
                
                new_ampm = "AM"
                new_day_1 = " (" + str(round(total_days)) + " days later)"
                
                #Check if day is None.
                if day is None:
                
                    update_day = ""
            
                else:
                    
                    find_day = day_position+int(str_total_days[0])+1
                    
                    if find_day<7:
                    
                        update_day = ", "+list_days[day_position+int(str_total_days[0])+1]
                    
                    else:
                    
                        find_day = find_day - (7*int((find_day/7)))
                        update_day = ", "+list_days[find_day]
                        
    #Join all the strings for the new_time.
    new_time = str(new_hour_1)+":"+new_minutes_2+" "+str(new_ampm)+update_day+new_day_1

    return new_time
    
print(add_time("11:55 AM", "3:12"))
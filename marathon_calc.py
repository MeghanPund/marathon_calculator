from math import *

def completion_time(pace_mins, pace_secs, distance_in_miles):
    total_secs = (((pace_mins * 60) + pace_secs) * distance_in_miles)
    seconds = int(total_secs % 60)
    minutes = floor((total_secs / 60) % 60)
    hours = floor((total_secs / 60) / 60)
         
    if distance_in_miles == 13.1:
        print(f"Your projected half marathon time is {hours} hours, {minutes} minutes, and {seconds} seconds!")
    elif distance_in_miles == 26.2:
        print(f"Your projected marathon time is {hours} hours, {minutes} minutes, and {seconds} seconds!")
    elif distance_in_miles >= 26.2:
        print(f"Your projected ultramarathon time is {hours} hours, {minutes} minutes, and {seconds} seconds!")
    else:
        print(f"Your projected finish time is {hours} hours, {minutes} minutes, and {seconds} seconds!")

completion_time(9, 20, 13.1)

def pace(race_hours, race_minutes, race_seconds, distance_in_miles):
    total_secs = (race_hours * 3600) + (race_minutes * 60) + race_seconds
    pace_mins = floor(total_secs / 60 / distance_in_miles)
    pace_secs = floor((total_secs % (pace_mins * 60 * distance_in_miles)) / distance_in_miles)
    if distance_in_miles == 13.1:
        print(f"To run a {race_hours}:{race_minutes}:{race_seconds} half marathon, you need to clock {pace_mins}-minute, {pace_secs}-second miles!")    
    elif distance_in_miles == 26.2:
        print(f"To run a {race_hours}:{race_minutes}:{race_seconds} marathon, you need to clock {pace_mins}-minute, {pace_secs}-second miles!")
    elif distance_in_miles >= 26.2:
        print(f"To run a {race_hours}:{race_minutes}:{race_seconds} ultramarathon, you need to clock {pace_mins}-minute, {pace_secs}-second miles!")
    else:
        print(f"To run a {race_hours}:{race_minutes}:{race_seconds} race, you need to clock {pace_mins}-minute, {pace_secs}-second miles!")
    

pace(2, 0, 0, 13.1)
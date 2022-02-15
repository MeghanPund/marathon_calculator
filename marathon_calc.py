from math import *


def completion_time(pace_mins, pace_secs, distance_in_miles):
    '''
    Takes 3 arguments, pace in minutes, pace in seconds, and distance in miles.
    Performs calculations that give the completion time for a race.
    '''
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


def pace(race_hours, race_minutes, race_seconds, distance_in_miles):
    '''
    Takes 4 arguments, race hours, race minutes, race seconds,
    and distance in miles.
    Performs calculations that give the pace needed to complete
    a race within the given time.
    '''
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


def run_program():
    '''Runs the program.'''
    print("Welcome to the Marathon Calculator.\n Would you like to calculate your pace based on finish time, or your finish time based on pace?\n")
    choice = input("Enter 'pace' to determine your pace, or 'finish time' to find your finish time: ")
    if choice.lower() == 'pace':
        distance_in_miles = float(input("How far (in miles) will you be running? i.e. 13.1: "))
        race_time = input("How many hours:minutes:seconds will it take you? i.e. 3:30:00 : ").split(":")
        race_time = [int(nums) for nums in race_time]
        race_hours, race_minutes, race_seconds = race_time
        pace(race_hours, race_minutes, race_seconds, distance_in_miles)
    elif choice.lower() == 'finish time':
        distance_in_miles = float(input("How far (in miles) will you be running? i.e. 13.1 : "))
        pace_mins_secs = input("How many minutes:seconds will it take you per mile? i.e. 9:30 : ").split(":")
        pace_mins_secs = [int(nums) for nums in pace_mins_secs]
        pace_mins, pace_secs = pace_mins_secs
        completion_time(pace_mins, pace_secs, distance_in_miles)
    else:
        print("Oops. Try that again.")
        run_program()


if __name__=='__main__':
    run_program()

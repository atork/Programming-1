import random
import time

#Function to generate a random number between 1 and 60 for the countdown
def get_countdown():
    return random.randint(1, 60)

#Function to print the current state of the timer
def print_timer(tim):
    minutes = int(tim / 60)
    seconds = tim % 60
    print('Time remaining: {:02d}:{:02d}'.format(minutes, seconds))

#Function to check if the countdown is finished
def check_finished():
    return time == 0

#Function to start the timer and decrease it by one second each second
def start_timer(tim):
    while True:
        print_timer(tim)
        tim -= 1
        if check_finished():
            break
        time.sleep(1)

#Start the function and call it with a random countdown number
start_timer(get_countdown())
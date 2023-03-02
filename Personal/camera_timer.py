## This code takes three parameters: delay, interval, and num_photos. 
# The camera_timer function takes these parameters and simulates a camera timer. 
# The sleep function from the time module is used to pause the code for a specified number of seconds. 
# The user inputs the values for delay, interval, and num_photos and the code takes the specified number
# of photos with the specified interval between each photo, after the specified delay. ##

import time

def camera_timer(delay, interval, num_photos):
    print(f"Starting camera timer with a delay of {delay} seconds, taking {num_photos} photos with an interval of {interval} seconds between each photo.")
    time.sleep(delay)
    for i in range(num_photos):
        print(f"Taking photo {i+1}")
        time.sleep(interval)
    print("Camera timer finished.")

delay = int(input("Enter delay time in seconds: "))
interval = int(input("Enter interval time in seconds: "))
num_photos = int(input("Enter number of photos: "))

camera_timer(delay, interval, num_photos)
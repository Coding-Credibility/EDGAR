# This code runs the new_index script on a 24 hour basis

# Importing the file and time keeping
import new_index, time

# While loop to run the new_index code every 24 hours
while True:

    # Run new_index
    new_index
    
    # Just to keep user aware
    print ("I will check for a new file in 24 hours")
    
    # 24 hours = 86400 seconds
    time.sleep(86400)

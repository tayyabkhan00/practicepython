import os
import time
REPEAT_INTERVAL = 5
# sets the variable "REPEAT INTERVAL"to 3600 seconds(1 hour).
while True:
# creates an infinite loop
    command = "osascript -e 'say \"drink water\";osascript -e\"display alert\\\"drink water\\\"\"'"
# this line constructs a string that represent a command to be executed.
# osascript is a command line tool on macos that allows you to interact with the os scripting capabilities
# the -e flag allows you to specify a script to be executed.
# the script here uses say to speak phrase "drinkwater" and display alert to show a pop-up alert with the same message. 
    os.system(command)
# executes the command stored in the command variable.this will trigger the "drink water" reminders 
    time.sleep(REPEAT_INTERVAL)
# pauses the program for the duration specified in "REPEAT INTERVAL"(1 hour),before the loop starts again

import machine
from machine import Pin
import time

# Define the up and down button pins
up_button = Pin(12, Pin.IN, Pin.PULL_UP)
down_button = Pin(13, Pin.IN, Pin.PULL_UP)

# Define the menu options
menu_options = ["Option 1", "Option 2"]

# Set the initial menu index
current_option = 0

while True:
    # Print the menu options with a cursor indicating the current option
    for i, option in enumerate(menu_options):
        if i == current_option:
            print("> " + option)
        else:
            print("  " + option)

    # Check if the up button is pressed
    if not up_button.value():
        # Decrement the menu index
        current_option -= 1
        # Wrap around to the last option if necessary
        current_option = max(0, current_option)
        time.sleep(0.3)

    # Check if the down button is pressed
    if not down_button.value():
        # Increment the menu index
        current_option += 1
        # Wrap around to the first option if necessary
        current_option = min(len(menu_options)-1, current_option)
        time.sleep(0.3)

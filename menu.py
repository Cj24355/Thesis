# Import the necessary libraries
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD class
lcd = characterlcd.Character_LCD_Mono(board.D4, board.D5, board.D6, board.D7, lcd_columns, lcd_rows)

# Initialize the menu options
menu_options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Initialize the menu buttons
button_up = digitalio.DigitalInOut(board.D12)
button_up.direction = digitalio.Direction.INPUT
button_up.pull = digitalio.Pull.UP

button_down = digitalio.DigitalInOut(board.D13)
button_down.direction = digitalio.Direction.INPUT
button_down.pull = digitalio.Pull.UP

button_select = digitalio.DigitalInOut(board.D14)
button_select.direction = digitalio.Direction.INPUT
button_select.pull = digitalio.Pull.UP

# Initialize the menu index
menu_index = 0

# Initialize the LCD screen
def initialize_lcd():
    lcd.clear()
    lcd.message = menu_options[menu_index]

# Handle input from the menu buttons
def handle_input():
    global menu_index
    if not button_up.value:
        menu_index = (menu_index - 1) % len(menu_options)
    elif not button_down.value:
        menu_index = (menu_index + 1) % len(menu_options)
    elif not button_select.value:
        print("Selected: " + menu_options[menu_index])

# Handle output to the LCD screen
def handle_output():
    lcd.clear()
    lcd.message = menu_options[menu_index]

# Main loop
initialize_lcd()
while True:
    handle_input()
    handle_output()
    time.sleep(0.1)
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from ds3231 import DS3231
from time import sleep

# Initiate The Size and the Address of the LCD

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

# initializing the I2C method for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Initiation RealTime Clock Module

ds = DS3231(i2c)

# Initializing The Time and Date

time = ds.get_time()
print("Year: " + str(time[0]))
print("Month: " + str(time[1]))
print("Day: " + str(time[2]))
print("Hour: " + str(time[3]))
print("Minute: " + str(time[4]))
print("Second: " + str(time[5]))

# Initializing the Buttons
button_up = Pin(12, Pin.IN)
button_down = Pin(14, Pin.IN)
button_select = Pin(27, Pin.IN)


# Creating Array for Menu
menu = ["TIME OF FEEDING", "KILOGRAM/GRAMS", "START OPERATION"]
options_menu = 0  # Menu State


def RealTime():
    # This Section Is for the Time and Date Section
    date_time = ds.get_time()
    year = str(date_time[0])
    month = str(date_time[1])
    day = str(date_time[2])
    hour = str(date_time[3])
    minute = str(date_time[4])

    lcd.clear()
    lcd.putstr("Time: " + hour + ":" + minute)
    lcd.move_to(1, 0)
    sleep(10)
    lcd.clear()
    lcd.putstr("Date: " + year + "/" + month + "/" + day)

RealTime()
while True:

    if button_up.value() == True:
        lcd.clear()
        options_menu = max(options_menu - 1, 0)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")
    if button_down.value() == True:
        lcd.clear()
        options_menu = min(options_menu + 1, len(menu) - 1)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")

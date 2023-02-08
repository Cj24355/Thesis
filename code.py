# Create A program for Automated Feeding Machine
# 1st Create A menu. In The Menu There is TIME OF FEEDING, KILOGRAMS/GRAMS, and START OPERATIONS
# 2nd Create A Configuration For TIME OF FEEDING and KILOGRAMS/GRAMS
# Create A function of START OPERATION Where TIME OF FEEDING and KILOGRAMS/GRAMS Configuration WILL save
# In the Configuration for TIME OF FEEDING is We use the DS3231 RTC Module that control the Time(HRS) of the FEEDING
#
# In the Configuration of KILOGRAMS/GRAMS we used the LOADCELL.
#

from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from ds3231 import DS3231
from time import sleep

# Initializing The Buttons
button_Scroll = Pin(12, Pin.IN)
button_select = Pin(14, Pin.IN)

# Initiate The Size and the Address of the LCD

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

# Iniitalizing the I2C method for ESP32

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
# i2c = I2C(scl=Pin(5), sda=Pin(4), Freq=10000)
# Initializing the I2C method forz ESP8266
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
# Initialization RealTime Clock Module

ds = DS3231(i2c)
# Printing The Time and Date
time = ds.get_time()
print("Year " + str(time[0]))
print("Month " + str(time[1]))
print(" Day " + str(time[2]))
print("Hour " + str(time[3]))
print("Minute " + str(time[4]))
print("Second " + str(time[5]))


# Creating Array for Menu

menu = ["TIME AND DATE",
        "TIME OF FEEDING",
        "KILOGRAM/GRAMS",
        "START OPERATION"
        ]

TimeAndDate = [" YEAR:",
               " MONTH:",
               "  DAY:",
               " HOURS:",
               "MINUTES:",
               "SECONDS:"
               ]
TimeFeeding = [" HOURS:",
               "MINUTES:",
               "SECONDS:",
               ]
KiloGrams = ["KILOGRAMS:",
             "  GRAMS:"
             ]

options_menu = 0  # Main Menu State
TimeDate = 0  # Time and Date State
TimeFeed = 0  # Time of Feeding State
KiLos = 0  # KILOGRAMS/GRAMS State

# Creating Functions For RealTime Clock


def RealTime():
    date_time = ds.get_time()
    year = str(date_time[0])
    month = str(date_time[1])
    day = str(date_time[2])
    hour = str(date_time[3])
    minute = str(date_time[4])
    second = str(date_time[5])

# this Section is for displaying the Time, Date, Year, Month, and day to the LCD Screen
    lcd.clear()
    lcd.putstr("TIME: " + hour + ":" + minute + ":" + second)
    lcd.move_to(1, 0)
    sleep(10)
    lcd.clear()
    lcd.putstr("Date: " + year + "/" + month + "/" + day)
    sleep(10)


# RealTime()

# Time and Date Configuration


# def Time_Date():
    # DateTime = ds.get_time()
   # year = 0
    # month = 0
    # day = 0
    # hour = 0
    # minute = 0
    # second = 0

    # if options_menu == 0:
    # if button_select == True:
    # print("The button was pressed")
# Time_Date()

while True:
    if button_Scroll.value() == True:
        lcd.clear()
        options_menu = (options_menu + 1) % len(menu)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")

    if button_select.value() == True and options_menu == 0:
        print("The button was pressed")
        lcd.clear()
        TimeDate = (TimeDate + 1) % len(TimeAndDate)
        lcd.move_to(4, 0)
        lcd.putstr(f"{TimeAndDate[TimeDate]}")

    elif button_select.value() == True and options_menu == 1:
        print("Array 1 has been Pressed")
        lcd.clear()
        TimeFeed = (TimeFeed + 1) % len(TimeFeeding)
        lcd.move_to(4, 0)
        lcd.putstr(f"{TimeFeeding[TimeFeed]}")
    elif button_select.value() == True and options_menu == 2:
        print("Array 2 has been Pressed")
        lcd.clear()
        KiLos = (KiLos + 1) % len(KiloGrams)
        lcd.move_to(3, 0)
        lcd.putstr(f"{KiloGrams[KiLos]}")

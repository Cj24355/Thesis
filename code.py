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
#button_set = Button(Pin(27, Pin.IN)) #Useless For Now

# Initiate The Size and the Address of the LCD

I2C_ADDR = 0x27 #LCD Address
totalRows = 2 #LCD Total Rows
totalColumns = 16 #LCD total Columns

# Iniitalizing the I2C method for ESP32

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  #i2c pin and Frequency
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

# menu is the main manu
menu = ["TIME AND DATE",
        "TIME OF FEEDING",
        "KILOGRAM/GRAMS",
        "START OPERATION"
        ]
# TimeAnddate is the submenu of TIME AND DATE IN THE MENU
TimeAndDate = [" YEAR:",
               " MONTH:",
               "  DAY:",
               " HOURS:",
               "MINUTES:",
               "SECONDS:"
               ]
# TimeFeeding is the submenu of TIME OF FEEDING IN THE MENU
TimeFeeding = [" HOURS:",
               "MINUTES:",
               "SECONDS:",
               ]
#KiloGrams is the submenu of KILOGRAMS/GRAMS IN THE MENU
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


#Main Lopp
while True:
    if button_Scroll.value() == True: #If the button_scroll was pressed. The menu will start Incrementing 
        lcd.clear()
        options_menu = (options_menu + 1) % len(menu)
        lcd.move_to(0, 0)
        lcd.putstr(f"{menu[options_menu]}")
      
    if button_select.value() == True and options_menu == 0: #if the button select the Time and date menu the submenu will appear 
        lcd.clear()
        lcd.move_to(4, 0)
        lcd.putstr(f"{TimeAndDate[TimeDate]}")
        button_select.value() == False
        print("blyat")
        while True:
            if button_Scroll.value() == True: 
                lcd.clear()
                TimeDate = (TimeDate + 1) % len(TimeAndDate)
                lcd.move_to(4, 0)
                lcd.putstr(f"{TimeAndDate[TimeDate]}")
                if button_set.is_pressed() == True:
                    print("Set Year:")
       
    elif button_select.value() == True and options_menu == 1: #if the button select the Time of Feeding menu the submenu will appear 
        print("Array 1 has been Pressed")
        lcd.clear()
        TimeFeed = (TimeFeed + 1) % len(TimeFeeding)
        lcd.move_to(4, 0)
        lcd.putstr(f"{TimeFeeding[TimeFeed]}")
        button_select.value() == False
        while True:
            if button_Scroll.value() == True:
                lcd.clear()
                TimeFeed = (TimeFeed + 1) % len(TimeFeeding)
                lcd.move_to(4,0)
                lcd.putstr(f"{TimeFeeding[TimeFeed]}")
        
    elif button_select.value() == True and options_menu == 2:  #if the button select the Kilogram/Grams menu the submenu will appear 
        print("Array 2 has been Pressed")
        lcd.clear()
        KiLos = (KiLos + 1) % len(KiloGrams)
        lcd.move_to(3, 0)
        lcd.putstr(f"{KiloGrams[KiLos]}")
        button_select.value() == False
        while True:
            if button_Scroll.value() == True:
                lcd.clear()
                KiLos = (KiLos + 1) % len(KiloGrams)
                lcd.move_to(3, 0)
                lcd.putstr(f"{KiloGrams[KiLos]}")
 
 #################### GOALS ######################################              
# Create a function for back button. kong naa ta sa submenu kong i click ang back button kay mo balik siya sa main menu
# Create a function that can configure the TIME AND DATE, TIME OF FEEDING, KILOGRAMS/GRAMS
# Create a function for back button para sa configuration ba after ma configure ang setting kong i click ang back kay mo exit siya sa configuration mode

#Anonther Goals#
# Create a function na mo display ang TIME AND DATE(USING RTC MODULE) and KILOGRAMS(USING LOADCELL) sa LCD
        #If the button was Pressed, The menu will shown in the Screen
        #If the button is not Pressed. ang TIME AND DATE and KILOGRAMS kay mo display sa LCD after 5 seconds

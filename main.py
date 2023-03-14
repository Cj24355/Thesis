import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import ntptime
import time
from machine import SoftI2C 
from ds3231 import DS3231
import network

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
networks = wlan.scan()
wlan.connect('ALHN-72AD', 'nCHLL2XrRN')

while not wlan.isconnected():
    pass

print('network config:', wlan.ifconfig())

# Initialize the I2C method for ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

# Initialize the DS3231 RTC module
ds = DS3231(i2c)

# Update the time from the network
ntptime.settime()

t = time.localtime()
ds.set_time(t[0], t[1], t[2], t[3], t[4], t[5], t[6]+1, t[7])


lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
Motor = Pin(2, Pin.OUT)
scheduled_times = [(7, 00), (12, 00), (17, 00)]

# Define the weekdays as strings
weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRDIAY", "SATURDAY", "SUNDAY"]

while True:
    # Get the current time from the RTC module
    t = ds.get_time()
    
    # Add 8 hours to the UTC time to get Philippine time
    ph_time = (t[3] + 8) % 24
    
    # Format the time as a string
    time_str = "{:02d}:{:02d}:{:02d}".format(ph_time, t[4], t[5])
    date_str = "{:02d}-{:02d}-{:04d}".format(t[2], t[1], t[0])
    
    time_spaces = (totalColumns - len(time_str)) // 2
    date_spaces = (totalColumns - len(date_str)) // 2
    
    # Combine the time/date strings with the calculated spaces
    time_str = " " * time_spaces + time_str + " " * time_spaces
    date_str = " " * date_spaces + date_str + " " * date_spaces
    
    # Get the day of the week
    day_idx = time.localtime()[6]
    day_str = weekdays[day_idx]
    
    # Display the time, day, and date on the LCD screen
    lcd.clear()
    lcd.move_to((totalColumns - len(time_str)) // 2, 0)
    lcd.putstr(time_str)
    lcd.move_to((totalColumns - len(day_str)) // 2, 1)
    lcd.putstr(day_str)
    #lcd.move_to((totalColumns - len(date_str)) // 2, 1)
    #lcd.putstr(date_str[len(day_str):])  # Remove the day of the week from the date string
    
    # Wait for one second
    
    
    if (ph_time, t[4]) in scheduled_times:
        Motor.on()
        print("Led is On")
        print(time_str)
        time.sleep(30)
        Motor.off()
        time.sleep(30)
    else:
        Motor.off()
    
    # Wait for one sec
    time.sleep(1)

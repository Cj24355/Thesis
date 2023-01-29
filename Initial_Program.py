import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Define the up and down button pins
up_button = Pin(12, Pin.IN, Pin.PULL_UP)
down_button = Pin(13, Pin.IN, Pin.PULL_UP)


while True:
    
    if up_button.value() == True:
        lcd.putstr("The Button was pressed")
        sleep(5)
        lcd.clear()
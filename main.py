import machine
from machine import Pin, SoftI2C, Timer
import ntptime
import time
from ds3231 import DS3231
import network
import lcd_2004
from hx711 import HX711

# Initialize the HX711 load cell object
hx = HX711(dout=(16), pd_sck=4)
hx.set_scale(86053.4)
hx.tare()

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


#lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
lcd = lcd_2004.lcd(0x27, 22, 21)  # Change to match your device (Address, SCL Pin, SDA Pin)

Motor = Pin(2, Pin.OUT)

# Define the scheduled times
scheduled_times = [(7, 0), (12, 0), (17, 0)]

# Define the scheduled time index
scheduled_time_idx = 0

# Define the push buttons for setting the scheduled times
button_hour = Pin(15, Pin.IN, Pin.PULL_UP)
button_minute = Pin(14, Pin.IN, Pin.PULL_UP)
button_next = Pin(13, Pin.IN, Pin.PULL_UP)

button_hour_last = 0
button_minute_last = 0
button_next_last = 0
debounce_delay = 200  # debounce delay in milliseconds

def button_hour_handler(pin):
    global scheduled_times, scheduled_time_idx, button_hour_last
    now = time.ticks_ms()
    if (now - button_hour_last) < debounce_delay:
        return
    button_hour_last = now

    # Increment the hour of the current scheduled time
    hour, minute = scheduled_times[scheduled_time_idx]
    hour = (hour + 1) % 24
    scheduled_times[scheduled_time_idx] = (hour, minute)
    print("Hour button pressed. New scheduled time:", scheduled_times[scheduled_time_idx])
    lcd.lcd_clear()
    lcd.lcd_print("New SchedTime:", 1, 0)
    lcd.lcd_print("{:02d}:{:02d}".format(hour, minute), 2, 0)

def button_minute_handler(pin):
    global scheduled_times, scheduled_time_idx, button_minute_last
    now = time.ticks_ms()
    if (now - button_minute_last) < debounce_delay:
        return
    button_minute_last = now

    # Increment the minute of the current scheduled time
    hour, minute = scheduled_times[scheduled_time_idx]
    minute = (minute + 1) % 60
    scheduled_times[scheduled_time_idx] = (hour, minute)
    print("Minute button pressed. New scheduled time:", scheduled_times[scheduled_time_idx])
    lcd.lcd_clear()
    lcd.lcd_print("New SchedTime:", 1, 0)
    lcd.lcd_print("{:02d}:{:02d}".format(hour, minute), 2, 0)


def button_next_handler(pin):
    global scheduled_time_idx, button_next_last
    now = time.ticks_ms()
    if (now - button_next_last) < debounce_delay:
        return
    button_next_last = now

    # Go to the next scheduled time
    scheduled_time_idx = (scheduled_time_idx + 1) % len(scheduled_times)
    print("Next button pressed. New scheduled time index:", scheduled_time_idx)
    lcd.lcd_clear()
    lcd.lcd_print("SchedTimeIdx:", 1, 0)
    lcd.lcd_print(str(scheduled_time_idx), 2, 0)
    
button_hour.irq(trigger=Pin.IRQ_FALLING, handler=button_hour_handler)
button_minute.irq(trigger=Pin.IRQ_FALLING, handler=button_minute_handler)
button_next.irq(trigger=Pin.IRQ_FALLING, handler=button_next_handler)
# Define the weekdays as strings

weekdays = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

while True:

    # Get the current time from the RTC module
    t = ds.get_time()

    # Add 8 hours to the UTC time to get Philippine time
    ph_time = (t[3] + 8) % 24

    # Format the time as a string
    time_str = "{:02d}:{:02d}:{:02d}".format(ph_time, t[4], t[5])
    date_str = "{:02d}-{:02d}-{:04d}".format(t[2], t[1], t[0])


    # Get the day of the week
    day_idx = time.localtime()[6]
    day_str = weekdays[day_idx]

    # Display the time, day, and date on the LCD screen
    #lcd.clear()
    lcd.lcd_clear()
    
    lcd.lcd_print("Time/Date: " + time_str + " "*20, 1, 0)
    time.sleep(1)
    lcd.lcd_print("DAY: " + day_str + " "*20, 2, 0)
    lcd.lcd_print("Max-capacity: 100kg", 3, 0)
    # Display the weight load on the LCD screen
    weight = hx.get_units()
    formatted_weight = "{:.2f}".format(weight)
    lcd.lcd_print("Weight: {} kg".format(formatted_weight) + " "*20, 4, 0)
   
    if (ph_time, t[4]) in scheduled_times:
        Motor.on()
        print("Led is On")
        print(time_str)
        time.sleep(30)
        Motor.off()
        time.sleep(30)
    else:
        Motor.off()
       
    time.sleep(5)

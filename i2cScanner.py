import machine

sdaPin = machine.Pin(21)
sclPin = machine.Pin(22)

i2c = machine.I2C(sda = sdaPin, scl = sclPin, freq = 10000)

devices = i2c.scan()

if len (devices) == 0:
    print("No Devices !")
else:
    print("i2c devices found: ", len(devices))
for device in devices:
    print("At address: ", hex(device))
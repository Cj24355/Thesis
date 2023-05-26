from hx711 import HX711
import time

hx = HX711(dout=16, pd_sck=4)
hx.set_scale(1)
hx.set_time_constant(0.1)

print("Put the weight on the scale and press enter...")
input()
calibration_factor = hx.get_units(10)
print("Calibration factor: ", calibration_factor)

xvar = 0

while True:
    hx.tare()
    read = hx.read()
    average = hx.read_average(5)
    value = average / calibration_factor

    if xvar == 0:
        xvar = value

    output = float(value) - float(xvar)

    print('Raw value: ', read)
    print('Average value: ', average)
    print('Weight: ', value, 'kg -> ', output, 'kg')
    print('----------------')
    time.sleep(1)



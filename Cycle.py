import datetime

# Initialize current_weight_threshold to 0.4 grams
current_weight_threshold = 0.4

# Define the date when the weight threshold should increase
next_increase_date = datetime.date.today().replace(day=1, month=datetime.date.today().month+1)

while True:
    # Check if it's time to increase the weight threshold
    if datetime.date.today() >= next_increase_date:
        current_weight_threshold += 0.1  # Increase weight threshold by 0.1 grams
        next_increase_date = datetime.date.today().replace(day=1, month=datetime.date.today().month+1)

    # Get the weight and check if it's below the current weight threshold
    weight = hx.get_units()
    if weight >= current_weight_threshold:
        Motor.on()
        print("Led is On")
        print(time_str)

        while weight >= current_weight_threshold:
            weight = hx.get_units()
            time.sleep(0.1)

        Motor.off()
        print("Motor Stopped")
    else:
        Motor.off()

    time.sleep(2)

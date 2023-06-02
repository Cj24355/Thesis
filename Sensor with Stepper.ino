#include <Stepper.h>
#include <Servo.h>

// Stepper motor configuration
const int stepsPerRevolution = 2048;
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

// Servo motor configuration
Servo tap_servo;
int tap_servo_pin = 5;

// Sensor configuration
int sensor_pin = 4;
int val;

void setup() {
  // Stepper motor setup
  myStepper.setSpeed(10);

  // Servo motor setup
  tap_servo.attach(tap_servo_pin);
  Serial.begin(9600);

  // Sensor setup
  pinMode(sensor_pin, INPUT_PULLUP);
}

void loop() {
   //Perform stepper motor actions
  performStepperMotorActions();
  val = digitalRead(sensor_pin);
  Serial.println(val);

  if (val == 0) {
    Serial.println("Sensor detected!");
    

    // Perform servo motor actions
    tap_servo.write(0);
    unsigned long start_time = millis();
    while (millis() - start_time < 500) {
      // Wait for 500ms before moving the servo to 90 degrees
      delay(3000);
    }
    tap_servo.write(90);
  }
}

void performStepperMotorActions() {
  // Rotate 1024 steps clockwise
  myStepper.step(2048);
  delay(1000);

  // Rotate 1024 steps counterclockwise
  myStepper.step(-2048);
  delay(1000);
}

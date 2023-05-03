#include <Servo.h>

Servo tap_servo;

int sensor_pin = 4;
int tap_servo_pin =5;
int val;

void setup(){
  pinMode(sensor_pin,INPUT_PULLUP);
  tap_servo.attach(tap_servo_pin);
   Serial.begin(9600);
}

void loop(){
  val = digitalRead(sensor_pin);
  Serial.println(val);
  if (val==0)
  {
    Serial.println("Sensor detected!");
    tap_servo.write(0);
    unsigned long start_time = millis();
    while (millis() - start_time < 500) {
      // Wait for 500ms before moving the servo to 180 degrees
      delay(3000);
    }
    tap_servo.write(90);
  }
}

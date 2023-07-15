#include <Servo.h>

// Constants
const int ultrasonicTriggerPin = 2;      // Ultrasonic sensor trigger pin
const int ultrasonicEchoPin = 3;         // Ultrasonic sensor echo pin
const int conveyorMotorPin = 4;          // Conveyor motor control pin
const int proximitySensorPin = 10;        // Proximity sensor input pin
const int servoMotorPin = 6;             // Servo motor control pin
const int InfraRedSensor = 11;            // Infrared Sensor pin

// Variables
Servo servoMotor;

void setup() {
  pinMode(ultrasonicTriggerPin, OUTPUT);
  pinMode(ultrasonicEchoPin, INPUT_PULLUP);
  pinMode(conveyorMotorPin, OUTPUT);
  pinMode(proximitySensorPin, INPUT_PULLUP);
  pinMode(InfraRedSensor, INPUT);
  servoMotor.attach(servoMotorPin);
  unsigned long motorStartTime = 0;
  const unsigned long motorDuration = 30000; // Motor duration in milliseconds (30 seconds)
  
  // Start the conveyor motor initially
  digitalWrite(conveyorMotorPin, HIGH);
  Serial.begin(9600);
}

void loop() {
  // Read distance from ultrasonic sensor
  long duration, distance;
  int sensorstatus = digitalRead(InfraRedSensor); 
  
  digitalWrite(ultrasonicTriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonicTriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonicTriggerPin, LOW);
  
  duration = pulseIn(ultrasonicEchoPin, HIGH);
  distance = duration * 0.034 / 2;
  
  if (distance < 10) {
    // Waste detected, stop the conveyor motor
    digitalWrite(conveyorMotorPin, LOW);
    Serial.println("Ultrasonic Sensor: Waste Detected!");
    Serial.println(distance);
  } else {
    // No waste detected, restart the conveyor motor
    digitalWrite(conveyorMotorPin, HIGH);
  }
  
  // Check for metal waste using proximity sensor
  if (digitalRead(proximitySensorPin) == HIGH) {
    //digitalWrite(conveyorMotorPin, LOW);
    Serial.println("Detected");
    servoMotor.write(0);  // Rotate the servo motor to separate the metal waste
    delay(2000);
    servoMotor.write(90); // Reset the servo motor position
     // Add a 2-second delay before restarting the conveyor motor
    
    Serial.println("Proximity Sensor: Metal Waste Detected!");
  }

  if sensorstatus == 1{
    
  }
}

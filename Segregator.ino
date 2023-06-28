// Pin definitions for inductive sensors
const int sensor1Pin = 2;  // Sensor 1 connected to digital pin 2
const int sensor2Pin = 3;  // Sensor 2 connected to digital pin 3

// Pin definitions for motors
const int motor1Pin = 4;  // Motor 1 connected to digital pin 4
const int motor2Pin = 5;  // Motor 2 connected to digital pin 5

// Variables to store the sensor states
int sensor1State = 0;
int sensor2State = 0;

void setup() {
  // Initialize the inductive sensor pins as input
  pinMode(sensor1Pin, INPUT);
  pinMode(sensor2Pin, INPUT);

  // Initialize the motor pins as output
  pinMode(motor1Pin, OUTPUT);
  pinMode(motor2Pin, OUTPUT);
}

void loop() {
  // Read the sensor states
  sensor1State = digitalRead(sensor1Pin);
  sensor2State = digitalRead(sensor2Pin);

  // If sensor 1 detects metal, rotate motor 1 for 2 seconds
  if (sensor1State == HIGH) {
    Serial.println("Sensor1 Detected");
    rotateMotor(motor1Pin);
    delay(2000);  // Delay for 2 seconds
    stopMotor(motor1Pin);
  }

  // If sensor 2 detects metal, rotate motor 2 for 2 seconds
  if (sensor2State == HIGH) {
    rotateMotor(motor2Pin);
    delay(2000);  // Delay for 2 seconds
    stopMotor(motor2Pin);
  }
}

// Function to rotate a motor
void rotateMotor(int motorPin) {
  digitalWrite(motorPin, HIGH);  // Set motor pin to HIGH (ON)
}

// Function to stop a motor
void stopMotor(int motorPin) {
  digitalWrite(motorPin, LOW);  // Set motor pin to LOW (OFF)
}

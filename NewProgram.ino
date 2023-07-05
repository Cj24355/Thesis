// Pin definitions for inductive sensors
const int sensor1Pin = 7;  // Sensor 1 connected to digital pin 2
const int sensor2Pin = 8;  // Sensor 2 connected to digital pin 3

// Pin definitions for motors
const int motor1Pin = 4;  // Motor 1 connected to digital pin 4
const int motor2Pin = 5;  // Motor 2 connected to digital pin 5
const int motor3Pin = 6;  // Motor 3 connected to digital pin 6

// Pin definitions for Conveyor
const int conveyor = 9; // Motor 9 connected to digital pin 9

// Pin definitions for ultrasonic sensor
const int trigPin = 1;    // Ultrasonic sensor trig pin connected to digital pin 7
const int echoPin = 3;    // Ultrasonic sensor echo pin connected to digital pin 8

// Variables to store the sensor states
int sensor1State = 0;
int sensor2State = 0;


void setup() {
  // Initialize the inductive sensor pins as input
  pinMode(sensor1Pin, INPUT_PULLUP);
  pinMode(sensor2Pin, INPUT_PULLUP);

  // Initialize the motor pins as output
  pinMode(motor1Pin, OUTPUT);
  pinMode(motor2Pin, OUTPUT);
  pinMode(motor3Pin, OUTPUT);
  // Initialize the ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // Initialize Serial communication
  Serial.begin(9600);
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
    Serial.println("Sensor2 Detected");
    rotateMotor(motor2Pin);
    delay(2000);  // Delay for 2 seconds
    stopMotor(motor2Pin);
  }
  
  // Check the distance detected by the ultrasonic sensor
  int distance = getUltrasonicDistance();
  if (distance <= 3) {
    Serial.println("Ultrasonic Sensor Detected 3cm");
    rotateMotor(motor3Pin);
    delay(30000);  // Delay for 30 seconds
    stopMotor(motor3Pin);
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

// Function to get the distance from the ultrasonic sensor
int getUltrasonicDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2;

  return distance;
}

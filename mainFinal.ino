#include <Servo.h>

// Constants
const int ultrasonicTriggerPin = 2;      // Ultrasonic sensor trigger pin
const int ultrasonicEchoPin = 3;         // Ultrasonic sensor echo pin
const int conveyorMotorPin = 4;          // Conveyor motor control pin
const int proximitySensorPin = 10;        // Proximity sensor input pin
const int servoMotorPin = 6;             // Servo motor control pin
const int InfraRedSensor = 11;            // Infrared Sensor pin
const unsigned long interval = 1000;  // Timer interval in milliseconds
unsigned long previousMillis = 0;     // Stores the previous time
unsigned int countdownSeconds = 0;

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
  //digitalWrite(conveyorMotorPin, HIGH);
  Serial.begin(9600);
}


void Conveyor (){

  if (digitalRead( proximitySensorPin) == LOW){   
    Serial.println("Metal Detected");
    delay(500);
    digitalWrite(conveyorMotorPin, HIGH);
    delay(1000);
    servoMotor.write(90);  // Rotate the servo motor to separate the metal waste
    delay(1000);
    servoMotor.write(0); // Reset the servo motor position
     // Add a 2-second delay before restarting the conveyor motor
    }
    else{
      //delay(1000);
      digitalWrite(conveyorMotorPin, LOW);

    }
}


void loop () {

  digitalWrite(ultrasonicTriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonicTriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonicTriggerPin, LOW);
   long duration, distance; 
  duration = pulseIn(ultrasonicEchoPin, HIGH);
  distance = duration * 0.034 / 2;

  unsigned long currentMillis = millis();  // Get the current time

  if (currentMillis - previousMillis >= interval) {
    
    previousMillis = currentMillis; 

    if(distance < 7){
      countdownSeconds = 15;
    }
    
  delay(1000);
  Conveyor();
  
    if (countdownSeconds > 0 ) {
      
      Serial.println(countdownSeconds);
     
      countdownSeconds--;
    } else {
      // Countdown has reached zero
      Serial.println("Countdown complete!");
      digitalWrite(conveyorMotorPin, HIGH);
    }
  }

  
  
}

//program by: Orencio

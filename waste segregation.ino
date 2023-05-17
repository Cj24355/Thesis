#include <Servo.h>



Servo servo;
Servo servo1;


int ledPin1 = 11;
int ledPin2 = 8;
int ledPin3 = 4;

int trigPin1 = 9;
int echoPin1 = 10;

int trigPin2 = 12;
int echoPin2 = 13;

int trigPin3 = 2;
int echoPin3 = 3;




void setup(){
  servo.attach(6); // attach the servo to pin 6
  servo1.attach(7); // attach the servo to pin 7
  
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT_PULLUP);
 
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT_PULLUP);


  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT_PULLUP);
  
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);


  
  Serial.begin(9600); // Starts the serial communication
  }

void firstsensor(){ // This function is for first sensor.
  int duration1, distance1;
  digitalWrite (trigPin1, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin1, LOW);
  duration1 = pulseIn (echoPin1, HIGH);
  distance1 = (duration1/2) / 29.1;

      Serial.print("1st Sensor: ");
      Serial.print(distance1); 
      Serial.print("cm    ");

  if (distance1 < 30) {  // Change the number for long or short distances.
    digitalWrite (ledPin1, HIGH);
  } else {
    digitalWrite (ledPin1, LOW);
  }   
}
void secondsensor(){ // This function is for second sensor.
    int duration2, distance2;
    digitalWrite (trigPin2, HIGH);
    delayMicroseconds (20);
    digitalWrite (trigPin2, LOW);
    duration2 = pulseIn (echoPin2, HIGH);
    distance2 = (duration2/2) / 29.1;
 
      Serial.print("2nd Sensor: ");
      Serial.print(distance2); 
      Serial.print("cm    ");
  
    if (distance2 < 20) {  // Change the number for long or short distances.
      digitalWrite (ledPin2, HIGH);
    }
 else {
      digitalWrite (ledPin2, LOW);
    }


 }
void thirdsensor(){ // This function is for third sensor.
    int duration3, distance3;
    digitalWrite (trigPin3, HIGH);
    delayMicroseconds (10);
    digitalWrite (trigPin3, LOW);
    duration3 = pulseIn (echoPin3, HIGH);
    distance3 = (duration3/2) / 29.1;

      Serial.print("3rd Sensor: ");  
      Serial.print(distance3); 
      Serial.print("cm");
  
    if (distance3 < 10) {  // Change the number for long or short distances.
      digitalWrite (ledPin3, HIGH);
    }
 else {
      digitalWrite (ledPin3, LOW);
}
}


void loop(){

  servo.write(0);
  servo1.write(30);
  delay(2000);

  
  servo.write(180);
  servo1.write(0);
  delay(2000);

  
  // Code to detect when someone approaches the door
  
  Serial.println("\n");
  firstsensor();
  secondsensor();
  thirdsensor();
  delay(100);
 
  
  
}

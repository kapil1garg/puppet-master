#include <Servo.h>

Servo servoArm;          // Define arm servo
Servo servoTorso;        // Define torso servo

int armDownAngle;
int armUpAngle;
int torsoDownAngle;
int torsoUpAngle;

bool isArmUp = false;
bool isArmDown = true; 
bool isTorsoUp = true; 
bool isTorsoDown = false; 

void setup() {
  // initializers for servo and connection
  servoArm.attach(9);  // Set left servo to digital pin 10
  servoTorso.attach(10);  // Set right servo to digital pin 9
  Serial.begin(9600);

  // initializers for variables
  armDownAngle = 25;
  armUpAngle = 115;
  torsoDownAngle = 25;
  torsoUpAngle = 115;

  // set initial angles for servos
  servoArm.write(armDownAngle);
  servoTorso.write(torsoUpAngle); 
} 

void loop() {
//  armUp();
//  armDown(); 
}

void serialEvent() {
  if (Serial.available() > 0) {
    String sentValue = Serial.readString();
    sentValue.trim();
    
    if (sentValue.equals("armUp")) {
      if (!isArmUp) {
        isArmUp = true;
        isArmDown = false;
        armUp();
      }
    } else if (sentValue.equals("armDown")) {
      if (!isArmDown) {
        isArmUp = false;
        isArmDown = true; 
        armDown();
      }
    } else if (sentValue.equals("bowDown")) {
      if (!isTorsoDown) {
        isTorsoUp = false; 
        isTorsoDown = true;
        bowDown();
      }
    } else if (sentValue.equals("bowUp")) {
      if (!isTorsoUp) {
        isTorsoUp = true; 
        isTorsoDown = false;
        bowUp(); 
      }
    }
  }
}

// Motion routines for arm up, arm down, bow up, and bow down
void armUp() {
  for(int pos = armDownAngle; pos < armUpAngle; pos++)
  {                                 
    servoArm.write(pos);            
    delay(15);                      
  }  
}

void armDown() {
  for(int pos = armUpAngle; pos > armDownAngle; pos--)
  {                                 
    servoArm.write(pos);            
    delay(15);                      
  } 
}

void bowUp() {
  for(int pos = torsoDownAngle; pos < torsoUpAngle; pos++)
  {                                 
    servoTorso.write(pos);            
    delay(15);                      
  } 
}

void bowDown() {
  for(int pos = torsoUpAngle; pos > torsoDownAngle; pos--)
  {                                 
    servoTorso.write(pos);            
    delay(15);                      
  } 
}


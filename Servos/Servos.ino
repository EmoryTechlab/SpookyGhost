#include <Servo.h> 

Servo base;  // create servo object to control a servo 
Servo head;  // create servo object to control a servo 
// a maximum of eight servo objects can be created 

int pos1 = 0;    // variable to store the servo position 
int pos2 = 0;    // variable to store the servo position 
int currentPos1 = 0;
int currentPos2 = 0;
int vel = 1;
int threshold = 10;

const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;


void setup()  { 
  base.attach(9);  // attaches the servo on pin 9 to the servo object 
  head.attach(8);
  Serial.begin(9600);
  base.write(0);
  head.write(0);
} 


void loop() { 
  recvWithEndMarker();
  showNewData();
  currentPos1 += vel * signum(pos1-currentPos1);
  currentPos2 += vel * signum(pos2-currentPos2);
  base.write(currentPos1);
  head.write(currentPos2);

}

void recvWithEndMarker() {
  static byte ndx = 0;
  char endMarker = '\n';
  char rc;

  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();
    if (rc != endMarker) {
      receivedChars[ndx] = rc;
      ndx++;
      if (ndx >= numChars) {
        ndx = numChars - 1;
      }
    }
    else {
      receivedChars[ndx] = '\0'; // terminate the string
      ndx = 0;
      newData = true;
    }
  }
}

void showNewData() {
  if (newData == true) {
    String in = String(receivedChars);
    pos1 = in.substring(0, 3).toInt();
    pos2 = in.substring(4, 7).toInt();
    newData = false;
  }
}

int signum(int num) {
  if (num >= 0) return 1;
  return -1;
}


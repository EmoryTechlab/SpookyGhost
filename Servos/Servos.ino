#include <Servo.h> 

Servo myservo;  // create servo object to control a servo 
// a maximum of eight servo objects can be created 

int pos = 0;    // variable to store the servo position 
int currentPos = 0;
int speed = 5;
int threshold = 10;

const byte numChars = 32;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;


void setup()  { 
	myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
	Serial.begin(9600)
	myservo.write(0);
} 


void loop() { 
	recvWithEndMarker();
	showNewData();
	while(abs(pos - currentPos) < 10) {
		currentPos += speed * signum(pos-currentPos);
		myservo.write(currentPos);
	}
	
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
		pos = atoi(&receivedChars);
        newData = false;
    }
}

int signum(int num) {
	if (num >= 0) return 1;
	return -1;
}

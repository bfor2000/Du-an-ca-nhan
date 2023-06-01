
#include <Servo.h>
#include <Wire.h> 
int servo1 = 5;
int servo2 = 6;
int servo3 = 9;
int servo4 = 10;

Servo kep;
Servo keo;
Servo gocquay;
Servo gockep;
int a[4]={90,0,0,0};
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  kep.attach(servo1);
  keo.attach(servo2);
  gocquay.attach(servo3);
  gockep.attach(servo4);
}
 
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
        String str = Serial.readString();
        for(int i=0;i<4;i++)
          {
          char kitu=str.charAt(i);
          if(kitu=='1') a[i]=a[i]+5;
          else if(kitu=='2') a[i]=a[i]-5;
          else a[i]=a[i];
          if(a[i]>180) a[i]=180;
          if(a[i]<0) a[i]=0;
          }
        
       
        Serial.println((String)a[0]);
        Serial.println((String)a[1]);
        Serial.println((String)a[2]);
        Serial.println((String)a[3]);
      
    }
        gockep.write(a[0]);
        gocquay.write(a[1]);
        keo.write(a[2]);
        kep.write(a[3]);
  delay(50);
}
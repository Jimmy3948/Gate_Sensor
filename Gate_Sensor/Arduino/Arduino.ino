#include<Servo.h>
int d=0;
Servo servo1; //Horizontal Servo
int x =0;
void setup()
{
  Serial.begin(9600);
  servo1.attach(9); 
  servo1.write(0);
}
void loop()
{
  x = Serial.read();
  
  if (x == '1')
   servo1.write(90);
  else if (x == '0')
  {
  servo1.write(0);
  
  }
}

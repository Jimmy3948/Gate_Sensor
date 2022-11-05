#include<Servo.h>
int d=0;
Servo servo1; //Horizontal Servo
int x =0; 
unsigned long int t = 0 ; 
int flag = 0 ;
void setup()
{
  Serial.begin(9600);
  servo1.attach(9); 
  servo1.write(0);
  pinMode(13,OUTPUT);
  
}
void loop()
{

 
  
  x = Serial.read();
  
   if (x == '1' && flag == 0){
    t = millis()/1000;
    flag = 1 ;
    //servo1.write(90);
    //digitalWrite(13,HIGH);
   }
   if (x == '1' && (millis()/1000)>t+3){
     servo1.write(90);
   }
   
   if (x == '0' && flag == 1){
    t = millis()/1000;
    flag = 0 ;
   }

   if (x == '0' && (millis()/1000)>t+3){
    servo1.write(0);
    //digitalWrite(13,LOW);
   }

}

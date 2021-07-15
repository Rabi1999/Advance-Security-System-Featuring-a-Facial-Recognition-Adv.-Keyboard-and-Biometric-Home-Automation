#include<Servo.h>
#include<SoftwareSerial.h>
SoftwareSerial HC05(10,11);
Servo myservo;
int pos;
int a2=3;
int s1=0;
char input;
int sensorPin = A0;
int Value,i=0;
float volt;
char d;
void setup() {
  Serial.begin(9600);
  HC05.begin(9600);
  // put your setup code here, to run once:
pinMode(a2,OUTPUT);
myservo.attach(9); 
  myservo.write(0);
}

void loop() {
  if(Serial.available())
{// put your main code here, to run repeatedly:
 d=Serial.read();
  //receive from pyhton and ard2 both

if(d=='s')
{
  for(pos=0;pos<=90;pos+=5)
   { myservo.write(pos);
   delay(20);
   }
  delay(200);
  digitalWrite(a2,HIGH);
  delay(200);
  digitalWrite(a2,LOW);
  delay(14000);
  for(pos=90;pos>=0;pos-=5)
   { myservo.write(pos);
   delay(20);
   }
  delay(200);
  Serial.println('y');
}
if(d=='e'||d=='f'||d=='g'||d=='d')
HC05.println(d);
d="";
}
}

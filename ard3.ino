#include<SoftwareSerial.h>
SoftwareSerial hc05(10,11);
char d;
int a5=2;
int a6=3;
void setup() {
Serial.begin(9600);
pinMode(a5,OUTPUT);
pinMode(a6,OUTPUT);
}

void loop() {
if(Serial.available()>0)
{
  d=Serial.read();
  Serial.println(d);
  if(d=='d')
  digitalWrite(a5,LOW);
  else if(d=='e')
  digitalWrite(a5,HIGH);
  else if(d=='f')
  digitalWrite(a6,LOW);
else if(d=='g')
  digitalWrite(a6,HIGH);
  d="";
  }
  
}

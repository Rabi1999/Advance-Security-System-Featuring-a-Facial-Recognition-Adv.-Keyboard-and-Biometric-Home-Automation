#include<SoftwareSerial.h>
SoftwareSerial HC05(10,11);
char input;
int s=0,t,p=0;
int f=0;
long int nu=0;
int i=0,ti=400;
unsigned prev=0;
unsigned curr=millis();
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
 
HC05.begin(9600);
}
void loop() 
{
if(Serial.available()>0)
input=Serial.read();
if(input=='m')
{ 
  digitalWrite(8,HIGH);
 delay(500);
digitalWrite(8,LOW);
input="";
 digitalWrite(7,HIGH);
    delay(200);
  digitalWrite(7,LOW);
  delay(200);
  while(p<=10)
  {
 digitalWrite(2,HIGH);
  int sensor1 = analogRead(A1);
  digitalWrite(3,HIGH);
  int sensor2 = analogRead(A2);
  digitalWrite(4,HIGH);
  int sensor3 = analogRead(A3);
  digitalWrite(5,HIGH);
  int sensor4 = analogRead(A4);
  digitalWrite(6,HIGH);
   int sensor5 = analogRead(A5);
  if(analogRead(A1)>=216&&analogRead(A1)<=400)
  {
    nu=nu*10+1;
    digitalWrite(7,HIGH);
    delay(ti);
    digitalWrite(7,LOW);
  }
  if(analogRead(A2)>=110&&analogRead(A2)<=130)
  {
    nu=nu*10+2;
    digitalWrite(7,HIGH);
    delay(ti);
    digitalWrite(7,LOW);
  }
   if(analogRead(A3)>=125&&analogRead(A3)<=150)
  {
   nu=nu*10+3;
    digitalWrite(7,HIGH);
    delay(ti);
    digitalWrite(7,LOW);
  
  }
   if(analogRead(A4)>=115&&analogRead(A4)<=130)
  {
    nu=nu*10+4;
    digitalWrite(7,HIGH);
    delay(ti);
    digitalWrite(7,LOW);
     
  }
   if(analogRead(A5)>=155&&analogRead(A5)<=190)
  {
    nu=nu*10+5;
    digitalWrite(7,HIGH);
    delay(ti);
    digitalWrite(7,LOW);
     
  }
    if(nu==231)
    {
    p=11;
    f=1;
    break;
    }
    else if(nu>231)
    {
    p=11;
    f=4;
    break;
    }
    else if(nu>0)
    {
    continue;
    p++;
    }
    
    else
    f=3;
  delay(500);
  
  p++;
  }
if(f==1)
{
  digitalWrite(8,HIGH);
delay(1000);
digitalWrite(8,LOW);
delay(500);
 while(s<10)
 {
if(HC05.available()>0)
{
  input=HC05.read();
  if(input=='a')
  {
 Serial.println('o');
 digitalWrite(8,HIGH);
 delay(500);
 digitalWrite(8,LOW);
 t=5;
 s=10;
  }
  input="";
}
delay(1000);
s++;
}
if(s>=10&&t==0)
{
Serial.println('f');
s=0;
}
input="";
}
else if(f==3||f==4)
{
Serial.println('p');
p=0;
nu=0;
}
}
}
  

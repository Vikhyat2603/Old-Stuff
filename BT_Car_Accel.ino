#include<AFMotor.h>

// 0 : Brake ; 1 : Forward ; 2 : Backward ; 3 : Right ; 4 : Left

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

char data;
int i;  

void setup() 
{
  motor1.setSpeed(255);
  motor2.setSpeed(255);
  motor3.setSpeed(255);
  motor4.setSpeed(255);
  Serial.begin(9600);
}

void loop() 
{
  if(Serial.available()>0)
  {
    data=Serial.read();
    Serial.println(data);
//    for(i=0;data[i]!='.';i++)
//      { r=(r*10)+(data[i]-'0');  }
//    i++;
//    for(;data[i]!='\0';i++)
//      { b=(b*10)+(data[i]-'0');  }
  }
}

void brake()
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

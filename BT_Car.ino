#include<AFMotor.h>

// 0 : Brake ; 1 : Forward ; 2 : Backward ; 3 : Right ; 4 : Left

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

char data;

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
    switch(data)
    {
      case '0': brake()     ; break;
      case '1': forward()   ; break;
      case '2': backward()  ; break;
      case '3': right()     ; break;
      case '4': left()      ; break;
      default :               break;
    }
  }
}

void brake()
{
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void forward()
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

void backward()
{
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void right()
{
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);  
}

void left()
{
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD); 
}

char data ;
void setup()
{
    Serial.begin(9600);                             
    pinMode(13, OUTPUT);  
}
void loop()
{
   if(Serial.available() > 0)      
   {
      data = Serial.read();        
      Serial.print("\n");        
      if(data == '1')     
      {         
         digitalWrite(13, HIGH);
         Serial.print("on");
      }
      else if(data == '0')         
      {
        digitalWrite(13, LOW);  
        Serial.print("off");
      }
   }
}

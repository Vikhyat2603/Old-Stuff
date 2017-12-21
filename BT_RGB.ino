
String data;
int i,r,g,b;
void setup()
{
    Serial.begin(9600);                             
    pinMode(9, OUTPUT);  
    pinMode(10, OUTPUT);  
    pinMode(11, OUTPUT);  
}
void loop()
{
   if(Serial.available() > 0)      
   {
      data = Serial.readString();       
      Serial.println(data);
      r=0;g=0;b=0;        
      for(i=0;data[i]!='.';i++)
      { r=(r*10)+(data[i]-'0');  }
      i++;
      for(;data[i]!='.';i++)
      { g=(g*10)+(data[i]-'0');  }
      i++;
      for(;data[i]!='\0';i++)
      { b=(b*10)+(data[i]-'0');  }
      Serial.println(r);
      Serial.println(g);
      Serial.println(b);
      analogWrite(11,r);
      analogWrite(10,g);
      analogWrite(9,b);        
   }
}

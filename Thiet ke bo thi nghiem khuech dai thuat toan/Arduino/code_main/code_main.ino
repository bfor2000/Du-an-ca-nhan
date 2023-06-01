String data="";
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(5);
  for(int i=22;i<37;i++)
    pinMode(i, OUTPUT); 
  digitalWrite(22, HIGH);
  digitalWrite(27, HIGH);
  digitalWrite(34, HIGH);
}

void loop() {
  if(Serial.available()){
    data = Serial.readString();
    if(data.startsWith("output:")){
      set_relay(data);
    }
    Serial.println("Ch1:"+(String)map(analogRead(A0),0,1023,-12000,12000)+" "+"Ch2:"+(String)map(analogRead(A1),0,1023,-10000,10000)+" "+"timer:"+(String)((unsigned long) millis()));
  }
}
void set_relay(String text){
  if((text.charAt(7)=='0'||text.charAt(7)=='1'||text.charAt(7)=='4')){
    digitalWrite(28,LOW);
    digitalWrite(27,LOW);
    digitalWrite(33,LOW);  
     digitalWrite(27+(int)text.charAt(7), text.charAt(8)=='0'?HIGH:LOW);
     for(int i=29;i<33;i++)
      digitalWrite(i,LOW);   
     }
  else{
    digitalWrite(28,LOW);
    digitalWrite(27,LOW);
    digitalWrite(33,LOW);    
    for(int i=29;i<31;i++)
     digitalWrite(i+text.charAt(7)-48-2,text.charAt(8)-48!=3&&(text.charAt(8)-48==i-29||text.charAt(8)-48==2)?HIGH:LOW);      
  }
  for(int i=22;i<27;i++)
    digitalWrite(i,text.charAt(7)-48==i-22?HIGH:LOW);
  for(int i=34;i<37;i++)
     digitalWrite(i,text.charAt(9)-48==i-34?HIGH:LOW);
}

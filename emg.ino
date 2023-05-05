/*
RECORDS VOLTAGE AT PIN A0 AT ~100HZ
AUTHOR: Enrico Persico
*/
int data;

void setup() {
  Serial.begin(9600);
} 

void loop(){
  data = analogRead(A0);
  Serial.println(data1);
  delay(10);
}

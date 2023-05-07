/*
RECORDS VOLTAGE AT PIN A0 AT ~100HZ
AUTHOR: Enrico Persico
*/
int data;

void setup() {
  Serial.begin(50000);
} 

void loop(){
  data = analogRead(A0);
  Serial.println(data);
  delay(1);
}

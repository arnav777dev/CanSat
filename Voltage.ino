void Voltage() {

  float sensorValue = analogRead(23);
  float voltage = (sensorValue * 3.3) / 1024.0;
//  float Battery_Voltage= voltage*44.7/39;   //for single cell
  float Battery_Voltage= voltage*13.3/3.3;//for 2S cells
  
  packet+=String(Battery_Voltage,2) + ",";
  
//  Serial.println(String(sensorValue,2));
//  Serial.println(Battery_Voltage);

//  float Battery_Voltage= voltage*(13.3/3.3);
//  int sensorValue = analogRead(A13);
//  float voltage = sensorValue * (3.3 / 1023.0);
//  float Battery_Voltage= voltage*(3.7/3.3);
//  Serial.println(String(Battery_Voltage,2));
}

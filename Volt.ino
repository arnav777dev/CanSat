void Voltage() {

  float sensorValue = analogRead(23);
  float voltage = (sensorValue * 3.3) / 1024.0;
  float Battery_Voltage= voltage*13.3/3.3;//for 2S cells
  
  packet+=String(Battery_Voltage,2) + ",";

}

void sim_bmp() {
  while(1){
  char c= XBee.read();
  if(c == '<'){
    
    String receivedString = XBee.readStringUntil('>');  // Read the incoming string until '>'
//    receivedString.remove(0);
    simulated_pressure = receivedString.toInt();
    new_pressure=1; 
    break;
  }
  else if(c == 'd'){
    XBee.write("disable kro sim");
    simulation=0;
    return;
  }
  }
   
  float sim_alt = bmp.readAltitude(simulated_pressure/100);
  packet += String(sim_alt, 1);
  packet += ",";

  packet += simulated_pressure;
  packet += ",";

  float sim_temp = bmp.readTemperature();
  packet += String(sim_temp, 1);
  packet += ",";


  
}

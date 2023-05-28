// void sim_bmp() {
//   char c = XBee.read();
//   if (c == '<') {
//     sim_pr = "";
//     c = XBee.read();
//     while (c != '>') {
//       sim_pr += c;
//       c = XBee.read();
//     }
//   }

  int simulated_pressure = sim_pr.toInt();
   
  float sim_alt = bmp.readAltitude(simulated_pressure/100);
  packet += String(sim_alt, 1);
  packet += ",";

  packet += sim_pr;
  packet += ",";

  float sim_temp = bmp.readTemperature();
  packet += String(sim_temp, 1);
  packet += ",";
}

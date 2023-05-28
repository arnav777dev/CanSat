void Quectel_L89() {
  //while (mySerial.available()) {
  String sentence = mySerial.readStringUntil('\n');
  while (!sentence.startsWith("$GNGGA")) {
    sentence = "";
    sentence += mySerial.readStringUntil('\n');
  }
  String parts[15];
  int i = 0;
  char * pch = strtok (sentence.c_str(), ",");
  while (pch != NULL) {
    parts[i++] = pch;
    pch = strtok (NULL, ",");
  }

  String Satellites = parts[7];

  String altitude = parts[9];

  String latitude_full = parts[2];
  float latitude_float = latitude_full.toFloat();
  int latitude_degrees = int((int)(latitude_float) / 100);
  float latitude_minutes = ((latitude_float - (latitude_degrees * 100.0)) / 60.0);
  float latitude_converted = latitude_degrees + latitude_minutes;


  String longitude_full = parts[4];
  float longitude_float = longitude_full.toFloat();
  int longitude_degrees = int((int)(longitude_float) / 100);
  float longitude_minutes = ((longitude_float - (longitude_degrees * 100.0)) / 60.0);
  float longitude_converted = longitude_degrees + longitude_minutes;

  String time = parts[1];

  packet += time.substring(0, 2);
  packet += ":";
  packet += time.substring(2, 4);
  packet += ":";
  packet += time.substring(4, 6) + ",";

  packet += String(latitude_converted, 4);
  packet += ",";

  packet += String(longitude_converted, 4);
  packet += ",";

 //will print altitude with 2 decimal places once it is available else, empty (when yet to find fix)
    float altitude_float = altitude.toFloat();
    packet += String(altitude_float,1);
    packet += ",";

  packet += Satellites;
  packet += ",";
  //}
}

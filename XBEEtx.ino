void Xbeetx(){
  char dataPacket[packet.length() + 1];
  packet.toCharArray(dataPacket, packet.length() + 1);
  XBee.write(dataPacket);
}
//
//#include <SoftwareSerial.h>
//SoftwareSerial XBee(0,1);
//
//void setup()
//{
//  XBee.begin(9600);
//  Serial.begin(9600);
//}
//
//void loop(){
//  while (XBee.available()) {
//    String sentence = XBee.readStringUntil('\r');
//    Serial.write(sentence);
//    delay(1000);
//}
  

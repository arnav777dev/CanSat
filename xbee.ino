void Xbeetx(){
  char dataPacket[packet.length() + 1];
  packet.toCharArray(dataPacket, packet.length() + 1);
  XBee.write(dataPacket);
}

  

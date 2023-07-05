void BMP_280(){  
    float alt=bmp.readAltitude(calibration);  
    packet+=String(alt,1);
    packet+=",";

    altitudes[0]=altitudes[1]; // queue operation for altitude readings
    altitudes[1]=altitudes[2];
    altitudes[2]=alt;
    
    int h=bmp.readPressure();
    packet+=String(h);
    packet+=",";
    
    pressure[0]=pressure[1]; // queue operation for pressure readings
    pressure[1]=pressure[2];
    pressure[2]=h;
   
    float temp=bmp.readTemperature();
    packet+=String(temp,1);
    packet+=",";
    
}

void BMX(){
  sBmx160SensorData_t Omagn, Ogyro, Oaccel;
  bmx160.getAllData(&Omagn, &Ogyro, &Oaccel);
  
  packet+=String(Oaccel.x); 
  packet+=",";
  
  packet+=String(Oaccel.y); 
  packet+=",";
  
  packet+=String(Oaccel.z); 
  packet+=",";

  packet+=String(Ogyro.x); 
  packet+=",";
  
  packet+=String(Ogyro.y);
  packet+=",";

  packet+=String(Ogyro.z); 
  packet+=",";
  
//  d=(atan2(Oaccel.x,Oaccel.z)*4068)/71;
//  s_cam.write(-1*d);

}

void SW_state(){
   //0-boot mode 
   //1-test mode don't know

      if (cnt==40) {
      SWstate=3; //Ascent
      }
      
      if (cnt==100){
        //camera should start recording here
      ON_camera();
      BLDC.write(80);
      SWstate=4; //Deployment
    }
    
     if (cnt==160){
      SWstate=5; //Descent
     }
     
      if (cnt==220){
      s.write(180); //servo turns to deploy second parachute
      SWstate=6; //Aerobreak Release
      }

      if (cnt==280){
        BLDC.write(0);
        OFF_camera(); //camera stops recording here
        //buzzer should switch on here
        SWstate=7;//Impact
      }

   packet+=String(SWstate);
   packet+=">\r";

}

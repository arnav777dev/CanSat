//void SW_state(){
//   0-boot mode 
//   1-test mode don't know
//
//    int p1=pressure[0]/100;
//    int p2=pressure[1]/100;
//    int p3=pressure[2]/100;
//
//    float a1=altitudes[0];
//    float a2=altitudes[1];
//    float a3=altitudes[2];
//
//    if (p1==p2 && p2==p3 && a1==a2 && a2==a3)
//
//   else if (a1<=5.0 && a2<=5.0 && a3<=5.0){
//   if (a1<=5.0 && a2<=5.0 && a3<=5.0){
//      SWstate=2;//launch pad
//    }
//
//    else if (p2<p1 && p3<p2 && a2>a1 && a3>a2 && a1>5.0 && a2>5.0 && a3>5.0) {
//      SWstate=3; //Ascent
//      
//      if (millis()-start_BLDC>=7210 || a1>800.0 && a1<=900.0 && a3<a1 && p3>p1){
//        //camera should start recording here
//      ON_camera();
//      s.write(180);
//      BLDC.write(80);
//      SWstate=4; //Deployment
//    }
//    }
//    
//     else if (p2>p1 && p3>p2 && a2<a1 && a3<a2 && a1<800.0 && a2<800.0 && a3<800.0 ){
//      SWstate=5; //Descent
//      if (a3<=500.0){
//      s.write(180); //servo turns to deploy second parachute
//      SWstate=6; //Aerobreak Release
//      if (p1==p2 && p2==p3 && a1==a2 && a2==a3)
//      if (a1<5.0 && a2<5.0 && a3<5.0){
//        BLDC.write(0);
//        SWstate=7;//Impact
//        OFF_camera(); //camera stops recording here
//        //buzzer should switch on here
//      }
//    }
//    }
//
//    else{
//      SWstate=1;
//    }
//
//   packet+=String(SWstate);
//   packet+=">\r";
//
//}


void SW_state() {
  int p1 = pressure[0] / 100;
  int p2 = pressure[1] / 100;
  int p3 = pressure[2] / 100;

  float a1 = altitudes[0];
  float a2 = altitudes[1];
  float a3 = altitudes[2];

  if (a1 <= 5.0 && a2 <= 5.0 && a3 <= 5.0) {
    SWstate = 2; // Launch Pad
  }
  else if (a1 <= 500.0 && a2 <= 500.0 && a3 <= 500.0) {
    SWstate = 3; // Descent
    if (a3 <= 5.0) {
      s.write(180); // Deploy second parachute
      SWstate = 4; // Aerobrake Release
      if (p1 == p2 && p2 == p3 && a1 == a2 && a2 == a3) {
        SWstate = 7; // Impact
        OFF_camera(); // Stop recording here
        // Buzzer activation code can be added here
      }
    }
  }
  else if (a1 > 500.0 && a2 > 500.0 && a3 > 500.0) {
    SWstate = 5; // Ascent
    if (millis() - start_BLDC >= 7210 || (a1 > 800.0 && a1 <= 900.0 && a3 < a1 && p3 > p1)) {
      ON_camera(); // Start recording here
      BLDC.write(80);
      SWstate = 6; // Deployment
    }
  }
  else {
    SWstate = 1; // Test Mode or default state
  }

  packet += String(SWstate);
  packet += ">\r";
}

//
//void SW_state(){
//   //0-boot mode 
//   //1-test mode don't know
//      if(cnt<10) SWstate=2;
//      if (cnt==10) {
//      SWstate=3; //Ascent
//      }
//      
//      if (cnt==25){
//        //camera should start recording here
//      ON_camera();
//      BLDC.write(80);
//      SWstate=4; //Deployment
//    }
//    
//     if (cnt==40){
//      SWstate=5; //Descent
//     }
//     
//      if (cnt==50){
//      s.write(90); //servo turns to deploy second parachute
//      SWstate=6; //Aerobreak Release
//      }
//
//      if (cnt==60){
//        BLDC.write(0);
//        OFF_camera(); //camera stops recording here
//        //buzzer should switch on here
//        SWstate=7;//Impact
//      }
//
//   packet+=String(SWstate);
//   packet+=">\r";
//
//}

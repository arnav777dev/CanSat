void ON_camera(){ 
  if(vid==0){
  digitalWrite(cam,LOW);
  delay(500);
  digitalWrite(cam,HIGH);
  vid=1;
    }
  digitalWrite(cam,LOW);
  delay(150);
  digitalWrite(cam,HIGH);
}
//
void OFF_camera(){ 
   digitalWrite(cam,LOW);
   delay(600);
   digitalWrite(cam,HIGH);
}

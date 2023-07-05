void Timestamp(){
   packet+=String(hour());
   printDigits(minute());
   printDigits(second());
   packet+=",";
}

void printDigits(int digits) {
   packet+=":";
   if(digits < 10)
      packet+='0';
      packet+=String(digits);
}

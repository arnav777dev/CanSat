#include <Wire.h>              //importing libraries for all sensors
#include <Adafruit_BMP280.h>
#include <DFRobot_BMX160.h>
#include <SoftwareSerial.h>

SoftwareSerial XBee(34, 35);

#include <Servo.h>

#include <TimeLib.h>

#include <SD.h>

#define BMP280_ADDRESS 0x76
Adafruit_BMP280 bmp;
DFRobot_BMX160 bmx160;

char command;
bool telemetry = 1;
bool simulation = 0;
String sim_pr;
bool timeset = 0;
bool new_pressure=0;

Servo s;
float d;
int countn = 0;
float dR;
float dP;

Servo BLDC;
float start_BLDC;

int pressure[3] = {0, 0, 0}; //will be used as queue to determine S/W states acc. to pressure and altitude readings each second
float altitudes[3] = {0, 0, 0}; //new value pushed each second (with each data packet)

int cam = 32; //mini spy cam
bool vid = 0;

const int buzzer = 9;

File Kalpana_Test;
bool logged = 0;

String packet = "";
String prev_packet = "";
int simulated_pressure;
float calibration = 1013.25; //calibration for BMP altitude

int SWstate = 0;

SoftwareSerial mySerial(16, 17); //GNSS Tx and Rx, mySerial is GNSS object

int cnt = 0; // packet count

void setup() {

  BLDC.attach(6); //ESC activation
  delay(1);
  BLDC.write(10);
  delay(5000);

  Serial.begin(9600);

  XBee.begin(9600);

  mySerial.begin(9600);
  mySerial.println("$PMTK220,1000*5F");

  pinMode(cam, OUTPUT);
  digitalWrite(cam, HIGH);

  //  setTime(0, 0, 0, 24, 5, 2023);

  unsigned status;
  status = bmp.begin(BMP280_ADDRESS);
  bmx160.begin();

  //Serial.println("TEAM_ID,TIME_STAMPING,PACKET_COUNT,ALTITUDE,PRESSURE,TEMP,VOLTAGE,GNSS_TIME,GNSS_LATITUDE,GNSS_LONGITUDE,GNSS_ALTITUDE,GNSS_SATS,ACC_R,ACC_P,ACC_Y,GYRO_R,GYRO_P,GYRO_Y,FLIGHT_SOFTWARE_STATE");

  //  if (!status) {
  //    while (1);
  //    delay(10);
  //  }
  //
  //  if (!bmx160.begin()) {
  //    Serial.println("NO BMX found");
  //    while (1);
  //  }

  SD.begin(BUILTIN_SDCARD);

  //  for (int j = 0; j < 10; j++) { //calibration by taking mean of 10 BMP pressure readings
  //    calibration += bmp.readPressure();
  //    delay(50);
  //  }
  //  calibration /= 1000;
  //  calibration/=10;

  //  calibration=bmp.readPressure();

  //  calibration=bmp.readPressure();
  //  calibration/=100;

  //  for (int j = 0; j < 300; j++) { //calibration of bmx
  //    sBmx160SensorData_t Omagn, Ogyro, Oaccel;
  //    bmx160.getAllData(&Omagn, &Ogyro, &Oaccel);
  //    delay(50);
  //  }

  s.attach(33); //servo pwm pin

  pinMode(buzzer, OUTPUT);

  Kalpana_Test = SD.open("Flight_2022ASI049.csv", FILE_WRITE);

  if (Kalpana_Test && logged == 0) {
    Kalpana_Test.println("TEAM_ID,TIME_STAMPING,PACKET_COUNT,ALTITUDE,PRESSURE,TEMP,VOLTAGE,GNSS_TIME,GNSS_LATITUDE,GNSS_LONGITUDE,GNSS_ALTITUDE,GNSS_SATS,ACC_R,ACC_P,ACC_Y,GYRO_R,GYRO_P,GYRO_Y,FLIGHT_SOFTWARE_STATE");
    logged = 1;
  }
  Kalpana_Test.close();
}

// with GCS commands


void loop() {
  if (XBee.available()) {
    command = XBee.read();
    if(command=='x'){
      telemetry = 1;
    }
  }

  if (command == 'c') {      //calibrate
    calibration = 0.00;
    for (int j = 0; j < 10; j++) { //calibration by taking mean of 10 BMP pressure readings
      calibration += bmp.readPressure();
      delay(50);
    }

    calibration /= 1000;

//      for (int j = 0; j < 10; j++) { //calibration of bmx
//        sBmx160SensorData_t Omagn, Ogyro, Oaccel;
//        bmx160.getAllData(&Omagn, &Ogyro, &Oaccel);
//        delay(50);
//      }

  }

  else if (command == 'x') { // telemetry on/off
//    telemetry = 1;
    setTime(0, 0, 0, 24, 5, 2023);
    start_BLDC = millis();

    while (telemetry == 1) {
      data_packet();
      delay(10); 
    }
  }

  else if (command == 'e') { // sim enable
    SWstate = 1;
    simulation = 1;
  }

  else if (command == 'a') { // sim activate
    
    setTime(0, 0, 0, 24, 5, 2023);
    packet = "";
    cnt=-1;
    
    while(simulation==1){
    packet = "";
    cnt++;
    
    packet += "<2022ASI-049";
    packet += ",";
    Timestamp();
    packet += String(cnt) + ",";
    sim_bmp();
    Voltage();
    Quectel_L89();
        BMX();
    for(int i=0;i<6;i++){
      packet += 0.0;
      packet += ",";
    }
    packet+="1>\r";

if (new_pressure){
  new_pressure=0;
    Data_Log(); // logging packet to sd card for backup
    Xbeetx();
}
    
      if (XBee.available()) {
        command = XBee.read();
        if (command == 'd') { // sim disable
          simulation = 0;
        }
      }
    }
  }
}

void data_packet() { //data_packet function name with GCS commands
  telemetry = 1;
  cnt=-1;
  
  while (telemetry && SWstate != 7 ) { // until the CanSat makes impact, telemetry is sent


    if (timeset == 0) {
      setTime(0, 0, 0, 24, 5, 2023);
      timeset = 1;
    }

    packet = "";
    cnt++;

    if (cnt == 7380) { //breadboard testing camera, ON at 2 hr 3 mins ..7380
      s.write(180);
      ON_camera();
      BLDC.write(80);
    }

    if (cnt == 7980) { //breadboard testing camera, OFF after 10  mins reccording..7860+120
      OFF_camera();
      BLDC.write(0);
      while (cnt < 11580) { //bb test..buzzer should play upto 3 mins only...11460
        cnt++;
        analogWrite(buzzer, 10000);
        delay(500);
        analogWrite(buzzer, 0);
        delay(500);
      }
    }

    packet += "<2022ASI-049";
    packet += ",";
    Timestamp();
    packet += String(cnt) + ",";
    BMP_280();
    Voltage();
    Quectel_L89();
    //    BMX();
    for(int i=0;i<6;i++){
      packet += 0.0;
      packet +=",";
    }
    SW_state();

    Data_Log(); // logging packet to sd card for backup 
    Xbeetx();
    if (XBee.available()) {
      command = XBee.read();
      if (command == 'x') {
        telemetry = 0 ;
      }
    }
    //    Serial.println(packet); // printing packet to serial monitor
  }
}

#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_ADS1X15.h>

SoftwareSerial BTSerial(10,11);
Adafruit_ADS1015 ads;
bool start = false;
byte btRead;
unsigned int anaIn;
int16_t adc[4];

void setup() {
  BTSerial.begin(38400);
  Serial.begin(9600);
  ads.begin();
  
}

void BTPrint(unsigned int);

void loop() {
  if(BTSerial.available()) {
    btRead = BTSerial.read();
    if(!start) {
      start = true;
    }
    else if(btRead == 255) {
      while(1){}
    }
    else {
      for(byte j = 0; j < btRead; ++j) {
        for(byte i = 0; i < 20; ++i) {
          for(byte k = 0; k < 4; ++k) {
            adc[k] = ads.readADC(k);
            adc[k] = ads.readADC_SingleEnded(k);
            BTPrint(adc[k]);
//            Serial.print(float(adc[k])*300/(5000-float(adc[k])*3));
//            Serial.print(' ');
//            Serial.print(adc[k]);
//            Serial.print("  ");
          }
          Serial.println();
        }
      }
      BTSerial.flush();
    }
  }
}

void BTPrint(unsigned int output) {
  BTSerial.write(output >> 8);
  BTSerial.write(output);
}

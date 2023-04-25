// SDI 3 -> MOSI arduino 11
// SDO 13 -> MISO arduino 12
// SCK 2 -> CLK arduino 13
// CS 1 -> CS arduino 10

#include <SPI.h>

void setup() {
  // put your setup code here, to run once:

  SPI.begin();
  Serial.begin(9600);

  SPI.transfer(0x12);
  SPI.transfer(0xFF);



}

void loop() {
  // put your main code here, to run repeatedly:
  

  

}

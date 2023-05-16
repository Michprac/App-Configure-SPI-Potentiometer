// SDI 3 -> MOSI arduino 11
// SDO 13 -> MISO arduino 12
// SCK 2 -> CLK arduino 13
// CS 1 -> CS arduino 10


#include <SPI.h>

byte message_byte;
int configure_byte;
char element[4];
char operation;
int i=0;
String a;



void setup() {
  SPI.begin();
  Serial.begin(9600);
  pinMode(10, OUTPUT);
  digitalWrite(10, LOW);

}

void loop() {


  while (Serial.available() > 0){

    a =  Serial.readString();

    if (a[0] == '1' && a[1] == '1'){
      operation = 'a';
    }

    if (a[0] == '1' && a[1] == '2'){
      operation = 'b';
    }

    if (a[0] == '1' && a[1] == '3'){
      operation = 'c';
    }


    if (a[0] == 'A'){
      Serial.println(a.length());
      for (int k = 1; k < a.length()+1; k++) {
        element[k-1] = a[k];
      }
      message_byte = (byte)atoi(element);
      element[0]='\0';
    }

    if (a[0] == 'B'){
      for (int k = 1; k < a.length()+1; k++) {
        element[k-1] = a[k];
      }
      message_byte = (byte)atoi(element);
      element[0]='\0';
    }

    switch (operation) {
      case 'a':
        SPI.transfer(0x11);
        SPI.transfer(message_byte);
      case 'b':
        SPI.transfer(0x12);
        SPI.transfer(message_byte);
      case 'c':
        SPI.transfer(0x13);
        SPI.transfer(message_byte);
    }

  }

}
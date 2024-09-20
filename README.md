# Aplication for controlling digital potentiometer by spi interface

The aim of this project was creating an application with which you can control an integrated circuit, which consists of two potentiometers.
This solution helps to change the parameter of an electronic element remotely.

<p align="center">
  <img src ="View_of_the_app.png" width="500" >
</p>

The tested system consisted of a PCB containing an integrated circuit with a double potentiometer. The PCB was connected to an Arduino microcontroller, which in turn connected to a laptop running an application. The microcontroller acted as an intermediary, receiving commands via a USB/UART port, to which a double potentiometer was connected via an SPI interface. Using a simple C program, depending on the actions in the application, the microcontroller set the appropriate values ​​on the potentiometer.

To start working with this app you need to choose COM-port and element control option (first potentiometer, second potentiometer, two potentiometers at once). 
Also you need to upload the program (from the project directory) to the Arduino microcontroller.

Of course, you also need to make the appropriate wire connections, connect the appropriate pins of the integrated circuit with the pins of the Arduino microcontroller.

# Installation

To start using this app, the user can simply use the installer which is called main.exe. This file allows you to use the application without routine installations of additional environments and other things.

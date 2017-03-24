# PiTrude1.0
A Plastic Recycler controlled by a GUI on a Raspberry Pi to be used within Schools

Loughborough University Finalist (Product Design & Technology BSc Hons. Final Year Project)

Product Design, Embedded Design, OpenSource, Sustianability, Education,

Inspired by/Contributors:

David Hakkens (Shredder & Extruder designs & Precious Plastics Community) - https://davehakkens.nl/tag/preciousplastic/
Matt Richardson (mrichardson23) - https://github.com/mrichardson23/rpi-kivy-screen
Tony DiCola (tdicola) - https://github.com/adafruit/Adafruit_Python_MAX31855
Raspberry Pi Community - https://www.raspberrypi.org/community/

Hardware:

AC Adapter (Mains to mini USB)
 -  INPUT (AC): 100-240V - 50/60Hz  0.5A MAX
 - OUTPUT (DC): 5.0V 2.0A
 

Raspberry Pi 3 Model B
 - Powered by (x2) Dupont Jumper Cables
      +5V to +5V Display Module
      GND to GND Display Module

7" Official Raspberry Pi Touch Display (referred to as Display Module)
 - Powered by AC Adapter (mini USB)

 - Connections on Display Module:

    Connection 1: 15 Pin Ribbon Cable
      DSI to RPi DSI

    Connection 2: Dupont Jumper cables (x2)
      +5V - +5V RPi GPIO
      INT - N/A
      SDA - N/A
      SCL - N/A
      GND - GND on RPi GPIO

      (INT, SDA, SCL are not required when using 15 Pin DSI connection)

52Pi - Triple GPIO Multiplexing Expansion Board (reffered to as Rpi GPIO)
  - attached to Raspberry Pi 3 Model B 40 GPIO pins
  - 120 Pin Headers


Haiworld Wide Angle Camera 5 MP Omnivision 5647 Camera Module (referred to as Camera Module)
  - connected with 15 Pin Ribbon Cable
  - Camera Module CSI to Rpi CSI

Thermocouple Amplifier (K-Type) 1

- connected with Dupont Jumper Cables
  Vin - 3.3V RPi GPIO
  3Vo - N/A
  GND - GND RPi GPIO
  DO - IO16 RPi GPIO
  CS - IO20 RPi GPIO
  CLK - IO21 RPi GPIO

- connected to K Type Thermocouple Type-K (Glass Braid Insulated)
  Red (-) & Yellow (+) connection


Thermocouple Amplifier (K Type) 2

- connected with Dupont Jumper Cables
  Vin - 3.3V RPi GPIO
  3Vo - N/A
  GND - GND RPi GPIO
  DO - IO18 RPi GPIO
  CS - IO24 RPi GPIO
  CLK - IO25 RPi GPIO

 - connected to K Type Thermocouple Type-K (Glass Braid Insulated)
  Red (-) & Yellow (+) connection

#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

########################################################
#### M A X 3 1 8 5 5 K   C O N F I G U R A T I O N ####
########################################################


# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

# Raspberry Pi software SPI configuration.
CLK_1 = 25
CS_1 = 24
DO_1 = 18
sensor1 = MAX31855.MAX31855(CLK_1, CS_1, DO_1)

CLK_2 = 21
CS_2 = 20
DO_2 = 16
sensor2 = MAX31855.MAX31855(CLK_2, CS_2, DO_2)



print('Press Ctrl-C to quit.')
while True:
    temp1 = sensor1.readTempC()
    temp2 = sensor2.readTempC()
    internal1 = sensor1.readInternalC()
    internal2 = sensor2.readInternalC()
    print('Thermocouple1 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp1, c_to_f(temp1)))
    # print('    Internal1 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal1, c_to_f(internal1)))
    print('Thermocouple2 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp2, c_to_f(temp2)))
    #print('    Internal2 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal2, c_to_f(internal2)))
    time.sleep(0.25)     # Loop printing measurements every second.

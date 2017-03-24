from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
import time
from threading import Thread
from glob import glob

from kivy.uix.label import Label
from kivy.core.window import Window

        # Raspberry Pi software SPI configuration.
        #CLK_1 = 25
        #CS_1 = 24
        #DO_1 = 18
        #sensor1 = MAX31855.MAX31855(CLK_1, CS_1, DO_1)

        #CLK_2 = 21
        #CS_2 = 20
        #DO_2 = 16
        #sensor2 = MAX31855.MAX31855(CLK_2, CS_2, DO_2)


    #def c_to_f(c):
        #return c * 9.0 / 5.0 + 32.0

                    #temp1 = sensor1.readTempC()
                    #temp2 = sensor2.readTempC()
                    #internal1 = sensor1.readInternalC()
                    #internal2 = sensor2.readInternalC()
                    #print('Thermocouple1 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp1, c_to_f(temp1)))
                    # print('    Internal1 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal1, c_to_f(internal1)))
                    #print('Thermocouple2 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(temp2, c_to_f(temp2)))
                    #print('    Internal2 Temperature: {0:0.3F}*C / {1:0.3F}*F'.format(internal2, c_to_f(internal2)))
                    #time.sleep(0.25)     # Loop printing measurements every second.

            # Sleep for 100ms
            #sleep(0.1)

class ControlCentre(Screen):
    pass

class Learn(Screen):
    pass

class Tools(Screen):
    pass

class Manager(ScreenManager):

    screen_controlc = ObjectProperty(None)
    screen_learn = ObjectProperty(None)
    screen_tools = ObjectProperty(None)


class RecyclerApp(App):

    def build(self):
        m = Manager(transition=FadeTransition())
        return m



if __name__ == "__main__":
    RecyclerApp().run()

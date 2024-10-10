
import os
import sys 

class Pin:
    __registry = []
    OUT = "out"
    IN = "in"
    def __init__(self, gpio: int, mode: str) -> None:
        self.gpio = gpio
        self.mode = mode
        Pin.__registry.append(self)
        os.write('echo "{}" > /sys/class/gpio/export'.format(self.gpio))
        os.write('echo "{}" > /sys/class/gpio/gpio{}/direction'.format(self.mode, self.gpio))
    
    def writePin(self, val: int):
        '''
        This function writes the value of a specific pin. This functions requires a class member of the "Pin" class
        as an argument.
        
        >> ex_pin = Pin(19, "out")
        >> ex_pin.writePin(1) will write a 1/HIGH to the pin that was initialized
        >> ex_pin.writePin(0) will write a 0/LOW to the pin that was initialized
        '''
        if val == 1:
            os.write('echo "1" > /sys/class/gpio/gpio{}/value'.format(self.gpio))
            return 0
        elif val == 0:
            os.write('echo "0" > /sys/class/gpio/gpio{}/value'.format(self.gpio))
            return 0
        else:
            return None 
    
    def readPin(self):
        '''
        This function reads the value of a specific pin. This functions requires a class member of the "Pin" class
        as an argument.

        >> ex_pin = Pin(19, "in")
        >> ex_pin.readPin() will read the value of the pin that was initialized

        '''
        os.read('cat /sys/class/gpio/gpio{}/value'.format(self.gpio))
        return 0

    def unexportPinObject(self):
        '''
        This function unexports a specific pin. This functions requires a class member of the "Pin" class
        as an argument.

        >> ex_pin = Pin(19, "out")
        >> ex_pin.unexportPin() will unexport pin 19
        '''
        os.write('echo "{}" > /sys/class/gpio/unexport'.format(self.gpio))
        return 0


    @staticmethod
    def unexportPin(gpio: int):
        '''
        This function unexports a specific pin. This function does not require the intialization of a "Pin" object/class member
        beforehand.

        >> Pin.unexportPin(19) will unexport pin 19
        '''
        os.write('echo "{}" > /sys/class/gpio/unexport'.format(gpio))
        return 0
    
    @staticmethod
    def writeDigital(gpio: int, val: int):
        '''
        This function writes the value of a specific pin. This function does not require the intialization of a "Pin" object/class member
        beforehand.


        >> Pin.writeDigital(19, 1) will write a 1/HIGH to pin 19
        >> Pin.writeDigital(19, 0) will write a 0/LOW to pin 19

        DO BE WARNED: This function DOES write to the operating system, so it does export the pin's gpio number as a member of the /gpio/ directory. Meaning you would
        have to call the unexportPin() function to unexport the pin. 
        '''
        os.write('echo "{}" > /sys/class/gpio/export)'.format(gpio))
        os.write('echo "out" > /sys/class/gpio/gpio{}/direction'.format(gpio))
        if val == 1:
            os.write('echo "1" > /sys/class/gpio/gpio{}/value'.format(gpio))
            return 0
        elif val == 0:
            os.write('echo "0" > /sys/class/gpio/gpio{}/value'.format(gpio))
            return 0
        else:
            return None
    
    @staticmethod
    def readDigital(gpio: int):
        '''
        This function reads the value of a specific pin. This function does not require the intialization of a "Pin" object/class member
        beforehand.

        >> Pin.readDigital(19) will read the value of pin 19

        DO BE WARNED: This function DOES write to the operating system, so you it does export the pin's gpio number as a member of the /gpio/ directory. Meaning you would
        have to call the unexportPin() function to unexport the pin.

        '''
        os.write('echo "{}" > /sys/class/gpio/export'.format(gpio))
        os.write('echo "in" > /sys/class/gpio/gpio{}/direction'.format(gpio))
        os.read('cat /sys/class/gpio/gpio{}/value'.format(gpio))
        return 0
    


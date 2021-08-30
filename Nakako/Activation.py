#!/usr/bin/python
###########################################################################
#Filename      :Activation.py
#Description   :Activated-> LED ON / Not activated-> LED OFF
#Author        :Yuya
#Update        :2021/07/24
############################################################################

import RPi.GPIO as GPIO
import time


#set BCM_GPIO 17(GPIO0) as button pin
ButtonPin = 17
#set BCM_GPIO 18(GPIO1) as LED pin
LedPin = 18

#set activation mode and led status to True(OFF/OFF)
Activation_mode = True


#setup function for some setup---custom function
def setup():
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set all LedPin's mode to output,and initial level to HIGH(3.3V)
    GPIO.setup(LedPin,GPIO.OUT,initial=GPIO.HIGH)
    #set ButtonPin's mode to input,and pull up to high(3.3v)
    GPIO.setup(ButtonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    #set up a falling detect on ButtonPin,and callback function to ButtonLed
    GPIO.add_event_detect(ButtonPin,GPIO.FALLING,callback = Activation_change)
    pass


#define a callback function for button callback
def Activation_change(ev=None):
    global Activation_mode
    # Switch led status(on-->off; off-->on)
    Activation_mode = not Activation_mode
    GPIO.output(LedPin, Activation_mode)
    
    if Activation_mode:
        print('|**************************|')
        print('|Alarm is not activated... |')
        print('|**************************|')
        print(Activation_mode)
        print('\n')
    else:
        print('|*********************|')
        print('|Alarm is activated...|')
        print('|*********************|')
        print(Activation_mode)
        print('\n')
    time.sleep(1)


# Define a main function for main process
def main():
    # Print messages
#    print_message()
    while True:
        # Don't do anything.
        time.sleep(1)
        
        

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
    # Turn off LED
    GPIO.output(LedPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()
    pass


setup()
"""
try:
    main()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
except KeyboardInterrupt:
    destroy()
"""


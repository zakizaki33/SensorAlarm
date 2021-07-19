

import RPi.GPIO as GPIO
import smbus
import time
import datetime

address = 0x48
bus=smbus.SMBus(1)
# 10進数ならば６４になる
cmd_Cds=0x40
cmd_Thermista=0x41
cmd_Potential=0x43

ledPin = 11

# ic2set -y 1 0x48 0x03
# ic2get -y 1 0x48
# Cds 0x00
# thermista 0x01
# potential meter 0x03

# valueを読むのに１回でよめないから２回書く
value = bus.read_byte_data(address, 0x43)
value = bus.read_byte_data(address, 0x43)
print("value of potential meter is =",value,"(DEC)")

value = bus.read_byte_data(address, 0x40)
value = bus.read_byte_data(address, 0x40)
print("value of Cds is =",value,"(DEC)")


import pygame.mixer

alarm_music="004_canon543_Koisuru.mp3"
play_volume=100

pygame.mixer.init()
pygame.mixer.music.load(alarm_music)
pygame.mixer.music.set_volume(play_volume/100)

def loop():
    while True:
        value = bus.read_byte_data(address, 0x40)
        value = bus.read_byte_data(address, 0x40)
        print("value of Cds is =",value,"(DEC)")
        
        value2 = bus.read_byte_data(address, 0x43)
        value2 = bus.read_byte_data(address, 0x43)
        print("value of potential meter is =",value2,"(DEC)")
        print(datetime.datetime.now())
        hour = datetime.datetime.now().hour
        # print(hour)
        
        
        if value < 245 and value2<10 and hour >= 5 and hour <=7:
            # 220 during day time 
            pygame.mixer.music.play(1)
            time.sleep(100) # maybe 100sec
            # pygame.mixer.music.stop()
        else:
            destroy()
        time.sleep(180)
        
def destroy():
    print("program ended !!!")
    pygame.mixer.music.stop()

if __name__ == '__main__':
    print("Program has started !!!")
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
    




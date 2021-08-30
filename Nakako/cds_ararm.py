#!/usr/bin/python
###########################################################################
#Filename      :cds_ararm.py
#Description   :
#Author        :yuya
#Website       :
#Update        :2021/07/25
############################################################################

import time, signal, sys
import smbus
import pygame.mixer
import Activation

alarm_on_level = 200

alarm_music = "030406.WAV"

play_time = 10

play_volume = 100

reset_flag = 1

pygame.mixer.init()

pygame.mixer.music.load(alarm_music)

pygame.mixer.music.set_volume(play_volume/100)

def get_CDS():
    address = 0x48

    #indivisual adress of CDS(AIN0)
    A0 = 0x40

    bus = smbus.SMBus(1)

    bus.write_byte(address,A0)
    return bus.read_byte(address)
    time.sleep(1.0)


while True:
    print("Activation mode =",Activation.Activation_mode)
    CDS_level = get_CDS()
    print("CDS_level =",CDS_level)
    if Activation.Activation_mode == False:
        level = CDS_level
        if (level < alarm_on_level) and (reset_flag == 1):
            reset_flag = 0
            pygame.mixer.music.play(-1)
            
            st = time.time()
            
            while st + play_time > time.time():
                if Activation.Activation_mode == True:
                    break
                time.sleep(0.2)
                
        else:
            pygame.mixer.music.stop()
    else:
        reset_flag = 1
        
    time.sleep(1.0)
    




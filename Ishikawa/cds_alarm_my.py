#! /usr/bin/env python

import time, signal, sys
import RPi.GPIO as GPIO
import pygame.mixer
import smbus

alarm_on_volt = 0xf0
alarm_music = "music.mp3"
play_time = 120
play_volume = 100
switch_pin = 9

GAIN = 1
#adc = Adafruit_ADS1x15.ADS1015()
i2c = smbus.SMBus(1)
addr = 0x48

reset_flag = 1

GPIO.setmode( GPIO.BCM )
GPIO.setup( switch_pin, GPIO.IN )

pygame.mixer.init(frequency = 44100)    # 初期設定
pygame.mixer.music.load("music.mp3")     # 音楽ファイルの読み込み
#pygame.mixer.music.play(1)              # 音楽の再生回数(1回)

while True:
    i2c.write_byte_data(addr,0x40,0x00)
    data = i2c.read_byte_data(addr, 0x40)

    if ( data < alarm_on_volt ) and ( reset_flag == 1 ):
        reset_flag = 0
        pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
        print("ON")
        break;
    else:
        pygame.mixer.music.stop()
    
    print(hex(data))
    #ime.sleep( 0.1 )

#stop music condtion
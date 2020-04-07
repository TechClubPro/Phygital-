# -*- coding: utf-8 -*-
"""
Program to blink an LED connected at pin 32 (Dout 1)
"""

import Phygital as Bot
import time

Bot.init('COM3')

for i in range(10):
    Bot.dwrite(1,1)
    time.sleep(1)
    Bot.dwrite(1,0)
    time.sleep(1)
    
    
"""

//Digital Outputs
#define DOut1 18
#define DOut2 5
#define DOut3 17
#define DOut4 23

//Servo Pins

#define ServoPin2 25
#define ServoPin3 26
#define ServoPin4 27

//Digital Inputs
#define DIn1 32
#define DIn2 33
#define DIn3 4
#define DIn4 15

//Analog Inputs
#define AIn1 36
#define AIn2 39
#define AIn3 34
#define AIn4 35

#define RGBPin 14


#define EnChannel1 13
#define EnChannel2 12
#define RGBChannel3 14
"""
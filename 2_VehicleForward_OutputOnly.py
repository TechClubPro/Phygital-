# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:45:05 2020

@author: Toshiba
"""

import Phygital as PyBot
import time

import PhygitalVehicleClass as x



PyBot.init('COM3')
Vehicle=x.Vehicle


Vehicle.forward(Vehicle,170,1)
time.sleep(2)
PyBot.close()
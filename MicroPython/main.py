"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *

# our variable for the temperature
temperature_of_microbit = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        temperature_of_microbit = input.temperature()
        display.show(str(temperature_of_microbit))

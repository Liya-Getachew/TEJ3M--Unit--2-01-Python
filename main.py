"""
Created by: Liya Getachew
Created on: February 12 2025
This 
"""

# Example for Pico. Blinks the built-in LED.
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# loop forever
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)

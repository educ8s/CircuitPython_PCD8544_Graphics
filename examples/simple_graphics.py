import adafruit_pcd8544
import board
import busio
import digitalio
from time import sleep
from pcd8544_graphics import *

mosi_pin = board.GP11
clk_pin = board.GP10

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
dc = digitalio.DigitalInOut(board.GP16) # data/command
cs = digitalio.DigitalInOut(board.GP18) # Chip select
reset = digitalio.DigitalInOut(board.GP17) # reset

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)
display.bias = 5
display.contrast = 45

clearScreen(display)

for counter in range(48):
    drawLine(0,0,84,counter,display)
    
for counter in range(48):
    drawLine(0,counter,84,counter,display)
    
clearScreen(display)

for counter in range(48):
    drawLine(0,counter,84,counter,display)
    
clearScreen(display)

for counter in range(48):
    drawLine(0,counter,84,counter,display)

import adafruit_pcd8544
import board
import busio
import digitalio
from time import sleep
from pcd8544_graphics import *
from image import *
import math
import microcontroller

mosi_pin = board.GP11
clk_pin = board.GP10

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
dc = digitalio.DigitalInOut(board.GP16) # data/command
cs = digitalio.DigitalInOut(board.GP18) # Chip select
reset = digitalio.DigitalInOut(board.GP17) # reset

lcd = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)
lcd.bias = 5
lcd.contrast = 45

clearScreen(lcd)
    
drawFullScreenBitmap(lcd,image)

while True:
    temperature = round(microcontroller.cpu.temperature,1)
    draw_number(temperature,23,10,lcd)
    sleep(0.3)
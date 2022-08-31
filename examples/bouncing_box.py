import adafruit_pcd8544
import board
import busio
import digitalio
from time import sleep, monotonic

def clear_screen():
    display.fill(0)
    display.show()

def tick():
    global last_tick
    last_tick += 1/10
    wait = max(0, last_tick - monotonic())
    if wait:
         sleep(wait)
    else:
         last_tick = monotonic()
    
ball_x = 0
ball_y = 0
ball_speed_x = 1
ball_speed_y = 1
last_tick = monotonic()

mosi_pin = board.GP11
clk_pin = board.GP10

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
dc = digitalio.DigitalInOut(board.GP16) # data/command
cs = digitalio.DigitalInOut(board.GP18) # Chip select
reset = digitalio.DigitalInOut(board.GP17) # reset

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)
display.bias = 5
display.contrast = 45

clear_screen()

while True:
    display.fill(0)
    display.rect(0,0,84,48,1)
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if ball_y >= 43 or ball_y <= 0:
        ball_speed_y *= -1
    if ball_x >= 79 or ball_x <= 0:
        ball_speed_x *= -1
    
    display.fill_rect(ball_x, ball_y, 5, 5, 1)

    display.show()
    tick()
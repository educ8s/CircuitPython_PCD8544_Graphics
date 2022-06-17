def drawFullScreenBitmap(display,image):
    for row in range(48):
        for column in range(84):
            display.pixel(column,row, image[row][column])
    display.show()
    
def clearScreen(display):
    display.fill(0)
    display.show()
    
def dot(x,y,display):
    display.hline(x + 5,y + 26,3,1)
    display.hline(x + 4,y + 25,5,1)
    display.hline(x + 5,y + 24,3,1)
    
def zero(x,y,display):
    topSegment(x,y,display)
    bottomSegment(x,y,display)
    topRightSegment(x,y,display)
    bottomRightSegment(x,y,display)
    topLeftSegment(x,y,display)
    bottomLeftSegment(x,y,display)

def one(x,y,display):
    topRightSegment(x,y,display)
    bottomRightSegment(x,y,display)
    
def two(x,y,display):
    topSegment(x,y,display)
    bottomSegment(x,y,display)
    topRightSegment(x,y,display)
    bottomLeftSegment(x,y,display)
    middleSegment(x,y,display)
    
def three(x,y,display):
    topSegment(x,y,display)
    bottomSegment(x,y,display)
    topRightSegment(x,y,display)
    bottomRightSegment(x,y,display)
    middleSegment(x,y,display)
    
def four(x,y,display):
    topLeftSegment(x,y,display)
    topRightSegment(x,y,display)
    bottomRightSegment(x,y,display)
    middleSegment(x,y,display)

def five(x,y,display):
    topSegment(x,y,display)
    topLeftSegment(x,y,display)
    middleSegment(x,y,display)
    bottomRightSegment(x,y,display)
    bottomSegment(x,y,display)
    
def six(x,y,display):
    topSegment(x,y,display)
    topLeftSegment(x,y,display)
    middleSegment(x,y,display)
    bottomRightSegment(x,y,display)
    bottomSegment(x,y,display)
    bottomLeftSegment(x,y,display)

def seven(x,y,display):
    topSegment(x,y,display)
    bottomRightSegment(x,y,display)
    topRightSegment(x,y,display)

def eight(x,y,display):
    topSegment(x,y,display)
    bottomSegment(x,y,display)
    topRightSegment(x,y,display)
    bottomRightSegment(x,y,display)
    topLeftSegment(x,y,display)
    bottomLeftSegment(x,y,display)
    middleSegment(x,y,display)
    
def nine(x,y,display):
    topSegment(x,y,display)
    bottomSegment(x,y,display)
    topRightSegment(x,y,display)
    bottomRightSegment(x,y,display)
    topLeftSegment(x,y,display)
    middleSegment(x,y,display)
    
def clear(x,y,display):
    for number in range(y+27):
        display.hline(x,number,13,0)
        
def middleSegment(x,y,display):
    x = x + 1
    y = y + 13
    display.hline(x,y,11,1)
    display.hline(x+1,y-1,9,1)
    display.hline(x+1,y+1,9,1)
    
def topSegment(x,y,display):
    x = x + 1
    display.hline(x,y,11,1)
    x = x + 1
    y = y + 1
    display.hline(x,y,9,1)
    x = x + 1
    y = y + 1
    display.hline(x,y,7,1)

def topRightSegment(x,y,display):
    y=y+1
    x = x + 12
    display.vline(x,y,12,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,8,1)

def bottomLeftSegment(x,y,display):
    y = y + 14
    display.vline(x,y,12,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,8,1)
    
def topLeftSegment(x,y,display):
    y=y+1
    display.vline(x,y,12,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,8,1)
    
def bottomRightSegment(x,y,display):
    x = x + 12
    y = y + 14
    display.vline(x,y,12,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,8,1)

def bottomSegment(x,y,display):
    x = x + 1
    y = y + 26
    display.hline(x,y,11,1)
    x = x + 1
    y = y - 1
    display.hline(x,y,9,1)
    x = x + 1
    y = y - 1
    display.hline(x,y,7,1)
    
def draw_number(number, x, y, display):
    zeros = '.1f'
    number_string = f"{number:,{zeros}}"
    if len(number_string) > 1:
        for digit in range(len(number_string)):
            draw_single_number(number_string[digit],x,y,display)
            x = x + 16
    else:
        draw_single_number(number,x,y,display)

def draw_single_number(number,x,y,display):
    clear(x,y,display)
    numbers = {"0" : zero,
           "1" : one,
           "2" : two,
           "3" : three,
           "4" : four,
           "5" : five,
           "6" : six,
           "7" : seven,
           "8" : eight,
           "9" : nine,
           "." : dot}
    
    numbers[number](x,y,display)
    display.show()
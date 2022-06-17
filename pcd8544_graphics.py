def draw_full_screen_bitmap(display,image):
    for row in range(48):
        for column in range(84):
            display.pixel(column,row, image[row][column])
    display.show()
    
def clear_screen(display):
    display.fill(0)
    display.show()
    
def _dot(x,y,display):
    display.hline(x + 5,y + 26,3,1)
    display.hline(x + 4,y + 25,5,1)
    display.hline(x + 5,y + 24,3,1)
    
def _zero(x,y,display):
    _topSegment(x,y,display)
    _bottomSegment(x,y,display)
    _topRightSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _topLeftSegment(x,y,display)
    _bottomLeftSegment(x,y,display)

def _one(x,y,display):
    _topRightSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    
def _two(x,y,display):
    _topSegment(x,y,display)
    _bottomSegment(x,y,display)
    _topRightSegment(x,y,display)
    _bottomLeftSegment(x,y,display)
    _middleSegment(x,y,display)
    
def _three(x,y,display):
    _topSegment(x,y,display)
    _bottomSegment(x,y,display)
    _topRightSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _middleSegment(x,y,display)
    
def _four(x,y,display):
    _topLeftSegment(x,y,display)
    _topRightSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _middleSegment(x,y,display)

def _five(x,y,display):
    _topSegment(x,y,display)
    _topLeftSegment(x,y,display)
    _middleSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _bottomSegment(x,y,display)
    
def _six(x,y,display):
    _topSegment(x,y,display)
    _topLeftSegment(x,y,display)
    _middleSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _bottomSegment(x,y,display)
    _bottomLeftSegment(x,y,display)

def _seven(x,y,display):
    _topSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _topRightSegment(x,y,display)

def _eight(x,y,display):
    _topSegment(x,y,display)
    _bottomSegment(x,y,display)
    _topRightSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _topLeftSegment(x,y,display)
    _bottomLeftSegment(x,y,display)
    _middleSegment(x,y,display)
    
def _nine(x,y,display):
    _topSegment(x,y,display)
    _bottomSegment(x,y,display)
    _topRightSegment(x,y,display)
    _bottomRightSegment(x,y,display)
    _topLeftSegment(x,y,display)
    _middleSegment(x,y,display)
    
def _clear(x,y,display):
    for number in range(y+27):
        display.hline(x,number,13,0)
        
def _middleSegment(x,y,display):
    x = x + 1
    y = y + 13
    display.hline(x,y,11,1)
    display.hline(x+1,y-1,9,1)
    display.hline(x+1,y+1,9,1)
    
def _topSegment(x,y,display):
    x = x + 1
    display.hline(x,y,11,1)
    x = x + 1
    y = y + 1
    display.hline(x,y,9,1)
    x = x + 1
    y = y + 1
    display.hline(x,y,7,1)

def _topRightSegment(x,y,display):
    y=y+1
    x = x + 12
    display.vline(x,y,12,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,8,1)

def _bottomLeftSegment(x,y,display):
    y = y + 14
    display.vline(x,y,12,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,8,1)
    
def _topLeftSegment(x,y,display):
    y=y+1
    display.vline(x,y,12,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x + 1
    y = y + 1
    display.vline(x,y,8,1)
    
def _bottomRightSegment(x,y,display):
    x = x + 12
    y = y + 14
    display.vline(x,y,12,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,10,1)
    x = x - 1
    y = y + 1
    display.vline(x,y,8,1)

def _bottomSegment(x,y,display):
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
    zeros = '.2f'
    if type(number) == float:
        number_string = f"{number:,{zeros}}"
    else:
        number_string = str(number)
    if len(number_string) > 1:
        for digit in range(len(number_string)):
            _draw_single_number(number_string[digit],x,y,display)
            x = x + 16
    else:
        _draw_single_number(number,x,y,display)

def _draw_single_number(number,x,y,display):
    _clear(x,y,display)
    numbers = {"0" : _zero,
           "1" : _one,
           "2" : _two,
           "3" : _three,
           "4" : _four,
           "5" : _five,
           "6" : _six,
           "7" : _seven,
           "8" : _eight,
           "9" : _nine,
           "." : _dot}
    
    numbers[number](x,y,display)
    display.show()
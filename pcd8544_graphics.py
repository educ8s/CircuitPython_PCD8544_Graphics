def drawFullScreenBitmap(display,image):
    for row in range(48):
        for column in range(84):
            display.pixel(column,row, image[row][column])
    display.show()
    
def clearScreen(display):
    display.fill(0)
    display.show()

def drawRect(x,y,width,height,display):
    for pixel in range(width):
        display.pixel(x+pixel, y, 1)
        display.pixel(x+pixel, y+height-1, 1)
    
    for pixel in range(height):
        display.pixel(x,y+pixel,1)
        display.pixel(x+width-1,y+pixel,1)
        
    display.show()
    
def drawLine(x0,y0,x1,y1,display):
    #Calculate "deltas" of the line (difference between two ending points)
    dx = x1 - x0
    dy = y1 - y0
    
    #Calculate the line equation based on deltas
    D = (2 * dy) - dx
    y = y0
    
    for x in range(x0,x1):
        display.pixel(x,y,1)
        if D > 0:
            y = y + 1
            D = D - 2*dx
        D = D + 2*dy
    
    display.show()
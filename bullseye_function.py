'''
Draw a bullseye in the centre of the screen
'''

def setup():
    size(640, 360)
    background(51)
    noStroke()
    noLoop()
    
def draw():
    drawTarget("#0dc620", 100, 300)
    drawTarget("#0dc620", 400, 200)
    drawTarget("#ff0000", width/2, height/2)
    
        
def drawTarget(colour, xloc, yloc):
    # right target
    for i in range(5):
        size = 200
        ring_size = 40
        
        #determine red or white ring
        if i % 2 == 0:
            fill(colour)  
        else:
            fill(255,255,255)# white ring
            
        ellipse(xloc, yloc, size - i*ring_size, size - i*ring_size)
        
    
        

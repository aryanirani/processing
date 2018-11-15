'''
Draw a bullseye in the centre of the screen
'''

def setup():
    size(640, 360)
    background(51)
    noStroke()
    noLoop()
    
def draw():
    for i in range(5):
        size = 200
        ring_size = 40
        
        #determine red or white ring
        if i % 2 == 0:
            fill(255,0,0)  # red ring
        else:
            fill(255,255,255)# white ring
            
        ellipse(width/2, height/2, size - i*ring_size, size - i*ring_size)

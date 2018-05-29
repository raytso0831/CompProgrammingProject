#Ray Tso
#5/23/18
#battleship.py

from ggame import *
def redrawall():
    RADIUS=33
    white=Color(0xFFFFFF,1)
    black=Color(0x000000,1)
    blackOutline=LineStyle(1, black)
    whiteRectangle=RectangleAsset(75,75,blackOutline,white) 
    for r in range(0,5):
        for c in range(0,5):
            Sprite(whiteRectangle,(10+(2*RADIUS+10)*r,10+(2*RADIUS+10)*c))
    for r in range(0,5):
        for c in range(0,5):
            Sprite(whiteRectangle,(500+(2*RADIUS+10)*r,10+(2*RADIUS+10)*c))


board=[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

if __name__ == '__main__':
    redrawall()
    App().run()
































'''
from ggame import *
 #graphics
white=Color(0xFFFFFF,1)
black=Color(0x000000,1)
    

blackOutline=LineStyle(1, black)
whiteRectangle=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle2=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle3=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle4=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle5=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle6=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle7=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle8=RectangleAsset(75,75,blackOutline,white) 
whiteRectangle9=RectangleAsset(75,75,blackOutline,white) 
    
Sprite(whiteRectangle,(0,0))
Sprite(whiteRectangle2,(75,0))
Sprite(whiteRectangle3,(150,0))
Sprite(whiteRectangle4,(225,0))
Sprite(whiteRectangle5,(300,0))
Sprite(whiteRectangle6,(300,150))
Sprite(whiteRectangle7,(0,300))
Sprite(whiteRectangle8,(150,300))
Sprite(whiteRectangle9,(300,300))
    
    
App().run()
'''
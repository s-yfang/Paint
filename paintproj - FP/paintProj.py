#paintproj.py
#december 2017
#Sheng Fang
from pygame import*
import os
from random import *
from math import *
from tkinter import *
from tkinter.colorchooser import *  # colourchooser
#from pygame.locals import *

root = Tk()             # initializes the Tk engine
root.withdraw()         # Tk root shows a little window by default
                        # This hides that window

#set window
init()
inf = display.Info()
os.environ['SDL_VIDEO_WINDOW_POS'] = '40,40'

# set screen width and height
screen = display.set_mode((1100,800), HWSURFACE|DOUBLEBUF|RESIZABLE)
#screen = display.set_mode((1100,600))

#loading screen
opening = image.load("images/loading.png")
screen.blit(opening,(0,0))
display.flip()
time.wait(800) #wait 

#textbox
font.init()   
comicFont = font.SysFont("Comic Sans MS", 20)

#colours
red =(255,0,0)
green =(0,255,0)
blue =(0,0,255)
yellow =(255,255,0)
white =(255,255,255)
black =(0,0,0)
pink =(249,166,160)
lightpink =(250,193,182)
darkbrown =(94,78,65)
cream =(255,241,232)
brown =(189,173,160)

#background
screen.fill(cream)
background = image.load("images/pusheen background.jpg")
smallbackground = transform.scale(background,(900,615))
screen.blit(smallbackground,(235,0))

#rect canvas
canvasRect = Rect(305,35,740,540)
border = Rect(295,25,760,560)
#draw canvas
draw.rect(screen,darkbrown,border,0)
draw.rect(screen,white,canvasRect,0)

#rect undo/redo
undoRect = Rect(40,100,65,35,)
redoRect = Rect(125,100,65,35,)

#load undo/redo picture
undopic = image.load("images/undo.png")
smundopic = transform.scale(undopic,(65,35))

redopic = image.load("images/redo.png")
smredopic = transform.scale(redopic,(65,35))

#rect tools
toolRect = Rect(30,90,170,460)
draw.rect(screen,white,toolRect,0)

pencilRect = Rect(40,150,65,70)
eraserRect = Rect(125,150,65,70)
paintRect = Rect(40,230,65,70)
sprayRect = Rect(125,230,65,70)

rectRect = Rect(40,310,65,70)
ellipseRect = Rect(125,310,65,70)
fill_rectRect = Rect(40,390,65,70)
fill_ellipseRect = Rect(125,390,65,70)

lineRect = Rect(40,470,65,70)
highlightRect = Rect(125,470,65,70)

#load tool picture
pencilpic = image.load("images/pencil.png")
smpencilpic = transform.scale(pencilpic,(65,70))

eraserpic = image.load("images/eraser.png")
smeraserpic = transform.scale(eraserpic,(65,70))

paintpic = image.load("images/paintbrush.png")
smpaintpic = transform.scale(paintpic,(65,70))

spraypic = image.load("images/spray.png")
smspraypic = transform.scale(spraypic,(65,70))

rectpic = image.load("images/unfillrect.png")
smrectpic = transform.scale(rectpic,(65,70))

ellipsepic = image.load("images/ellipse.png")
smellipsepic = transform.scale(ellipsepic,(65,70))

fill_rectpic = image.load("images/fillrect.jpg")
smfill_rectpic = transform.scale(fill_rectpic,(55,60))

fill_ellipsepic = image.load("images/fillellipse.jpg")
smfill_ellipsepic = transform.scale(fill_ellipsepic,(65,70))

linepic = image.load("images/line.png")
smlinepic = transform.scale(linepic,(65,70))

highlighterpic = image.load("images/highlighter.png")
smhighlighterpic = transform.scale(highlighterpic,(65,70))

#rect options
openRect = Rect(10,15,40,40)
saveRect = Rect(65,15,40,40)
newRect = Rect(115,15,40,40)
colourRect = Rect(165,15,40,40)

#load option pictures
openpic = image.load("images/open.png")
smopenpic = transform.scale(openpic,(40,40))

savepic = image.load("images/save.png")
smsavepic = transform.scale(savepic,(40,40))

newpic = image.load("images/new.png")
smnewpic = transform.scale(newpic,(40,40))

colourpic = image.load("images/colour.png")
smcolourpic = transform.scale(colourpic,(40,40))

#rect stamps
pusheenstmp = Rect(985,640,60,60)
hellostmp = Rect(915,640,60,60)
sadstmp = Rect(845,640,60,60)

sleepingstmp = Rect(985,710,60,60)
donutstmp = Rect(915,710,60,60)
moustachestmp = Rect(845,710,60,60)

#load stamp pictures
pusheenpic = image.load("images/stmppusheen.png")
smpusheen = transform.scale(pusheenpic,(87,60))

hellopic = image.load("images/stmphello.png")
smhello = transform.scale(hellopic,(55,60))

sadpic = image.load("images/stmpsad.png")
smsad = transform.scale(sadpic,(60,70))

sleepingpic = image.load("images/stmpsleeping.png")
smsleeping = transform.scale(sleepingpic,(80,80))

donutpic = image.load("images/stmpdonut.png")
smdonut = transform.scale(donutpic,(60,60))

moustachepic = image.load("images/stmpmoustache.png")
smmoustache = transform.scale(moustachepic,(63,63))

#rect colour palette
colpaletteRect = Rect(10,615,180,180,)
draw.rect(screen,black,colpaletteRect,0)

#colour palette
colourwheel = image.load("images/colourpalette.jpg")
smallcolourwheel = transform.scale(colourwheel,(180,180))

#define
start= 0,0
size = 10
mx,my = 0,0
drawColour = 0

#tool
tool = "Pencil"
info1 = "Click and drag the left mouse"
info2 = "button to use pencil"

#undo/redo
undolist = [(screen.subsurface(canvasRect)).copy()] 
redolist = []

#setup
running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
            
        if evt.type == MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) and evt.button!=5 and evt.button!=4: #doesnt copy when scroll
                undolist.append(screen.subsurface(canvasRect).copy()) #copy canvas
                
        if evt.type == MOUSEBUTTONDOWN:
            sx,sy = evt.pos    #tuple (x,y) position of click
            copy = screen.copy()
            if evt.button == 1:  #left click
                start = evt.pos
                
                #click on undo
                if undoRect.collidepoint(mx,my): 
                    tool="Undo"
                    info1="Undo your last action"
                    info2="Ctrl + Z"
                    if len(undolist)>1: #if at least 2 elements
                        screen.blit(undolist[-2],(305,35)) #blit second last of screen captures
                        redolist.append(undolist.pop())#add last screen capture of undolist to redolist
                
                #click on redo
                if redoRect.collidepoint(mx,my):
                    tool="Redo"
                    info1="Redo your last action"
                    info2="Ctrl + Y"
                    if len(redolist)>=1:
                        screen.blit(redolist[-1],(305,35)) #redos last undo
                        undolist.append(redolist.pop())

            #change size
            elif evt.button==5:   #scroll down
                size -= 1
                size = max(1,size) #cannot be neg

            elif evt.button==4:   #scroll up
                size += 1
                
        #change size
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT:
                size -= 1
                size = max(1,size)  #cannot be neg
            if evt.key == K_RIGHT:
                size += 1
            #key shortcuts
            if evt.mod | KMOD_CTRL > 0:
               if evt.key == K_z:
                   if len(undolist)>1:
                        screen.blit(undolist[-2],(305,35))
                        redolist.append(undolist.pop())
               if evt.key == K_y:
                   if len(redolist)>=1:
                        screen.blit(redolist[-1],(305,35))
                        undolist.append(redolist.pop())

    oldmx,oldmy = mx,my 
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    #draw options
    draw.rect(screen,cream,openRect,0)
    draw.rect(screen,cream,saveRect,0)
    draw.rect(screen,cream,newRect,0)
    draw.rect(screen,cream,colourRect,0)
    
    #options highlight
    if tool=="Open":
        draw.rect(screen,lightpink,openRect)

    if tool=="Save":
        draw.rect(screen,lightpink,saveRect)

    if tool=="New":
        draw.rect(screen,lightpink,newRect)

    if tool=="Colour":
        draw.rect(screen,lightpink,colourRect)

    #draw undo/redo
    draw.rect(screen,pink,undoRect,0)
    draw.rect(screen,pink,redoRect,0)

    #undo/redo highlight
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,red,undoRect,1)
    if tool=="Undo":
        draw.rect(screen,lightpink,undoRect)

    if redoRect.collidepoint(mx,my):
        draw.rect(screen,red,redoRect,1)
    if tool=="Redo":
        draw.rect(screen,lightpink,redoRect)
    
    #draw tool boxes
    draw.rect(screen,pink,pencilRect,0)
    draw.rect(screen,pink,eraserRect,0)
    draw.rect(screen,pink,paintRect,0)
    draw.rect(screen,pink,sprayRect,0)
    draw.rect(screen,pink,rectRect,0)
    draw.rect(screen,pink,ellipseRect,0)
    draw.rect(screen,pink,fill_rectRect,0)
    draw.rect(screen,pink,fill_ellipseRect,0)
    draw.rect(screen,pink,lineRect,0)
    draw.rect(screen,pink,highlightRect,0)

    #toolbox highlight
    if tool=="Pencil":
        draw.rect(screen,lightpink,pencilRect)

    if tool=="Eraser":
        draw.rect(screen,lightpink,eraserRect)

    if tool=="Paintbrush":
        draw.rect(screen,lightpink,paintRect)

    if tool=="Spray":
        draw.rect(screen,lightpink,sprayRect)

    if tool=="Rectangle":
        draw.rect(screen,lightpink,rectRect)

    if tool=="Ellipse":
        draw.rect(screen,lightpink,ellipseRect)

    if tool=="Filled rectangle":
        draw.rect(screen,lightpink,fill_rectRect)

    if tool=="Filled ellipse":
        draw.rect(screen,lightpink,fill_ellipseRect)

    if tool=="Line":
        draw.rect(screen,lightpink,lineRect)

    if tool=="Highlighter":
        draw.rect(screen,lightpink,highlightRect)

    #draw stamps
    draw.rect(screen,cream,pusheenstmp,0)
    draw.rect(screen,cream,hellostmp,0)
    draw.rect(screen,cream,sadstmp,0)
    draw.rect(screen,cream,sleepingstmp,0)
    draw.rect(screen,cream,donutstmp,0)
    draw.rect(screen,cream,moustachestmp,0)

    #stamp highlight
    if tool=="Pusheen":
        draw.rect(screen,lightpink,pusheenstmp)

    if tool=="Hello":
        draw.rect(screen,lightpink,hellostmp)

    if tool=="Sad Pusheen":
        draw.rect(screen,lightpink,sadstmp)

    if tool=="Sleeping":
        draw.rect(screen,lightpink,sleepingstmp)

    if tool=="Donut":
        draw.rect(screen,lightpink,donutstmp)

    if tool=="Moustache":
        draw.rect(screen,lightpink,moustachestmp)
    
    #colour palette
    screen.blit(smallcolourwheel,(10,615))
    #click on colour palette
    if colpaletteRect.collidepoint(mx,my) and mb[0]==1:
        drawColour = screen.get_at((mx,my))  #get colour at position

    #highlighter
    cover = Surface((50,50)).convert() #make blank Surface
    cover.set_alpha(5) #transparency
    cover.fill((255,0,255)) 
    cover.set_colorkey((255,0,255))
    draw.circle(cover,(drawColour),(25,25),24)
    
    #click on options
    if openRect.collidepoint(mx,my):
        draw.rect(screen,red,openRect,1)
        tool="Open"
        info1="Open file"
        info2=""
        try:
            if mb[0]==1:
                result = filedialog.askopenfilename(title="Open a file!")
                pic = image.load(result)
                screen.blit(pic,(305,35))
        except:     #prevents crashing if window closed
            pass

    if saveRect.collidepoint(mx,my):
        draw.rect(screen,red,saveRect,1)
        tool="Save"
        info1="Save your picture!"
        info2=""
        try:
            if mb[0]==1:
                result = filedialog.asksaveasfilename(title="Save your work!")
                image.save(screen.subsurface(canvasRect),result)    
        except:     #prevents crashing
            pass
        
    if newRect.collidepoint(mx,my):
        draw.rect(screen,red,newRect,1)
        if mb[0]==1:
            tool="New"
            info1="Clear canvas" 
            info2=""
            screen.fill(white,(305,35,740,540))
            
    if colourRect.collidepoint(mx,my):
        draw.rect(screen,red,colourRect,1)
        tool="Colour"
        info1="Chose colour" 
        info2=""
        if mb[0]==1:
            drawColour, drawcolorAsString = askcolor(title="Even more rainbow!")
    
    #click on tool boxes    
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,red,pencilRect,1)
        if mb[0]==1:
            tool="Pencil"
            info1="Click and drag the left mouse"   #tool description
            info2="button to use pencil"

    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,red,eraserRect,1)
        if mb[0]==1:
            tool="Eraser"
            info1="Click and drag the left mouse"
            info2="button to use eraser"

    if paintRect.collidepoint(mx,my):
        draw.rect(screen,red,paintRect,1)
        if mb[0]==1:
            tool="Paintbrush"
            info1="Click and drag the left mouse"
            info2="button to use paint brush"
            
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,red,sprayRect,1)
        if mb[0]==1:
            tool="Spray"
            info1="Click and hold the left mouse"
            info2="button to use spray paint"
            
    if rectRect.collidepoint(mx,my):
        draw.rect(screen,red,rectRect,1)
        if mb[0]==1:
            tool="Rectangle"
            info1="Click and drag the left mouse"
            info2="button to make a rectangle"
            
    if ellipseRect.collidepoint(mx,my):
        draw.rect(screen,red,ellipseRect,1)
        if mb[0]==1:
            tool="Ellipse"
            info1="Click and drag the left mouse"
            info2="button to make an ellipse"

    if fill_rectRect.collidepoint(mx,my):
        draw.rect(screen,red,fill_rectRect,1)
        if mb[0]==1:
            tool="Filled rectangle"
            info1="Click and drag the left mouse"
            info2="button to make a filled rectangle"
            
    if fill_ellipseRect.collidepoint(mx,my):
        draw.rect(screen,red,fill_ellipseRect,1)
        if mb[0]==1:
            tool="Filled ellipse"
            info1="Click and drag the left mouse"
            info2="button to make a filled ellipse"

    if lineRect.collidepoint(mx,my):
        draw.rect(screen,red,lineRect,1)
        if mb[0]==1:
            tool="Line"
            info1="Click and drag the left mouse"
            info2="button to draw a line"

    if highlightRect.collidepoint(mx,my):
        draw.rect(screen,red,highlightRect,1)
        if mb[0]==1:
            tool="Highlighter"
            info1="Click and drag the left mouse"
            info2="button to use highlighter"

    #click on stamps
    if pusheenstmp.collidepoint(mx,my):
        draw.rect(screen,red,pusheenstmp,1)  
        if mb[0]==1:
            tool="Pusheen"
            draw.rect(screen,blue,pusheenstmp,1)
            info1="Click the left mouse button"
            info2="to use stamp"

    if hellostmp.collidepoint(mx,my):
        draw.rect(screen,red,hellostmp,1)  
        if mb[0]==1:
            tool="Hello"
            screen.blit(txtPic,(380,645))
            info1="Click the left mouse button"
            info2="to use stamp"

    if sadstmp.collidepoint(mx,my):
        draw.rect(screen,red,sadstmp,1)  
        if mb[0]==1:
            tool="Sad Pusheen"
            draw.rect(screen,blue,sadstmp,1)
            info1="Click the left mouse button"
            info2="to use stamp"

    if sleepingstmp.collidepoint(mx,my):
        draw.rect(screen,red,sleepingstmp,1)  
        if mb[0]==1:
            tool="Sleeping"
            draw.rect(screen,blue,sleepingstmp,1)
            info1="Click the left mouse button"
            info2="to use stamp"

    if donutstmp.collidepoint(mx,my):
        draw.rect(screen,red,donutstmp,1)  
        if mb[0]==1:
            tool="Donut"
            draw.rect(screen,blue,donutstmp,1)
            info1="Click the left mouse button"
            info2="to use stamp"

    if moustachestmp.collidepoint(mx,my):
        draw.rect(screen,red,moustachestmp,1)  
        if mb[0]==1:
            tool="Moustache"
            draw.rect(screen,blue,moustachestmp,1)
            info1="Click the left mouse button"
            info2="to use stamp"
            

    #click on canvas
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect)  #tools stay on canvas

        if tool=="Pencil":
            draw.line(screen,drawColour,(oldmx,oldmy),(mx,my),2)

        if tool=="Eraser":
            dx = mx - oldmx  
            dy = my - oldmy
            dist = int(sqrt(dx**2+dy**2))   
            for i in range(1,dist+1):
                dotX = int(oldmx+i*dx/dist)    
                dotY = int(oldmy+i*dy/dist)
                draw.circle(screen,white,(dotX,dotY),size)

        if tool=="Paintbrush":    
            dx = mx - oldmx  #dx is base 
            dy = my - oldmy  #dy is height
            dist = int(sqrt(dx**2+dy**2)) #length of hypot from starting point 
            for i in range(1,dist+1):
                dotX = int(oldmx+i*dx/dist)    
                dotY = int(oldmy+i*dy/dist)
                draw.circle(screen,drawColour,(dotX,dotY),size)

        if tool=="Spray":        
            for i in range(int(size*2)):  #speed which pixels fill
                px = randint(-size,size)  #random coordinate of pixel within range size
                py = randint(-size,size)
                if px**2 + py**2 < size**2:   #hypot  #to make circle
                    screen.set_at((mx+px,my+py),drawColour) #sets position of pixels
                    
        if tool=="Rectangle":
            screen.blit(copy,(0,0))
            if abs(mx-sx)>3 and abs(my-sy)>3:   #width cannot be greater than radius
                draw.rect(screen,drawColour,((sx,sy),(mx-sx,my-sy)),2)
            else:
                draw.rect(screen,drawColour,((sx,sy),(mx-sx,my-sy)))

        if tool=="Ellipse":
            screen.blit(copy,(0,0))
            rec = Rect(sx,sy,mx-sx,my-sy)
            rec.normalize()   #turns any neg width/height and makes it pos
            if abs(mx-sx)>3 and abs(my-sy)>3:   #width cannot be greater than radius
                draw.ellipse(screen,drawColour,(rec),2)
            else:
                draw.ellipse(screen,drawColour,(rec))

        if tool=="Filled rectangle":
            screen.blit(copy,(0,0))
            draw.rect(screen,drawColour,((sx,sy),(mx-sx,my-sy)))
            
        if tool=="Filled ellipse":
            screen.blit(copy,(0,0))
            rec = Rect(sx,sy,mx-sx,my-sy)
            rec.normalize()
            draw.ellipse(screen,drawColour,(rec))

        if tool=="Line":
            screen.blit(copy,(0,0))
            draw.line(screen,drawColour,start,(mx,my),size)

        if tool=="Highlighter":
            screen.blit(cover,(mx-25,my-25))
            
        #stamps
        if tool=="Pusheen":
            screen.blit(pusheenpic,(mx-250,my-106))

        if tool=="Hello":
            screen.blit(hellopic,(mx-149,my-200))

        if tool=="Sad Pusheen":
            screen.blit(sadpic,(mx-86,my-86))

        if tool=="Sleeping":
            screen.blit(sleepingpic,(mx-160,my-160))

        if tool=="Donut":
            screen.blit(donutpic,(mx-100,my-93))

        if tool=="Moustache":
            screen.blit(moustachepic,(mx-129,my-94))
            
        screen.set_clip(None)

    #blit option pictures
    screen.blit(smopenpic,(10,15))
    screen.blit(smsavepic,(65,15))
    screen.blit(smnewpic,(115,15))
    screen.blit(smcolourpic,(165,15))

    #blit undo/redo pictures
    screen.blit(smundopic,(40,100))
    screen.blit(smredopic,(125,100))

    #blit tool pictures
    screen.blit(smpencilpic,(40,150))
    screen.blit(smeraserpic,(125,150))
    screen.blit(smpaintpic,(40,230))
    screen.blit(smspraypic,(125,230))
    screen.blit(smrectpic,(40,310))
    screen.blit(smellipsepic,(125,310))
    screen.blit(smfill_rectpic,(45,395))
    screen.blit(smfill_ellipsepic,(125,390))
    screen.blit(smlinepic,(40,470))
    screen.blit(smhighlighterpic,(125,470))

    #blit stamp pictures
    screen.blit(smpusheen,(970,640))
    screen.blit(smhello,(918,640))
    screen.blit(smsad,(845,640))
    screen.blit(smsleeping,(975,710))
    screen.blit(smdonut,(915,710))
    screen.blit(smmoustache,(843,710))

    #textbox
    draw.rect(screen,darkbrown,(235,630,425,160))
    textRect = Rect(240,635,415,150)
    draw.rect(screen,white,textRect,0)#text
    txtPic = comicFont.render("Tool:",True,black)
    screen.blit(txtPic,(250,645))

    #x,y position
    xpos = str(mx)
    ypos = str(my)
    coordinateText = comicFont.render("x:" + xpos,True,black)
    screen.blit(coordinateText,(465,645))

    coordinateText = comicFont.render("y:" + ypos,True,black)
    screen.blit(coordinateText,(535,645))
    
    #size text
    size1 = comicFont.render("Scroll or press the left/right arrow",True,black)
    screen.blit(size1,(250,730))

    size2 = comicFont.render("keys to decrease/increase size!",True,black)
    screen.blit(size2,(250,750))
        
    #tool and info text
    txtPic = comicFont.render(tool,True,black)
    screen.blit(txtPic,(300,645))
    
    txtPic = comicFont.render(info1,True,black)
    screen.blit(txtPic,(250,680))

    txtPic = comicFont.render(info2,True,black)
    screen.blit(txtPic,(250,700))

    #chosen colour
    draw.rect(screen,drawColour,(595,645,50,50))
    
    display.flip()
quit()
            



















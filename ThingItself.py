import pygame,keyboard

pygame.init()
defaultWidth = 800
defaultHeight = 1000
screen = pygame.display.set_mode((defaultWidth,defaultHeight))
generalAlMa = ''
preinput = ''
run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run=False
    try: #a=1, s=2, w=3, d=4 
        if keyboard.is_pressed("a"):
            preinput = 1
        elif keyboard.is_pressed("s"):
            preinput = 2
        elif keyboard.is_pressed("w"):
            preinput = 3
        elif keyboard.is_pressed("d"):
            preinput = 4
        
    except:
        break
    print(preinput)
pygame.quit()
    
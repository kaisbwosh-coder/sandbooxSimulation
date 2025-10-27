import pygame,keyboard,random

pygame.init()
defaultWidth = 800
defaultHeight = 1000
screen = pygame.display.set_mode((defaultWidth,defaultHeight))
x = 300
y = 500
mxC = 0
myC = 0
currentElement = 3
fps = 120
clock = pygame.time.Clock()
#0 = air #1 = solid, #2 = Dirt, #3 = water
class solid:
    sizeX = 5
    sizeY = 5
    def __init__(self,types,x,y,upd):
        self.coDx = x
        self.coDy = y
        self.types = types
        self.updated = upd
        self.dyingCT = 15
    def trwaterMove(self,leftUnit,rightUnit,downUnit,leftdownUnit,rightdownUnit) ->int:
        #0:None,1q,2w,3e,4a,5d,6z,7x,8c
        ic = random.randint(1,2)
        if self.updated == True:
            self.updated = False
            return 0
       # ic = 
        match ic:
            case 1:
                if downUnit.getTypes() == "air":
                    self.updated = True
                    return 7
                elif leftdownUnit.getTypes() == "air":
                    self.updated = True
                    return 6
                elif rightdownUnit.getTypes() == "air":
                    self.updated = True
                    return 8
                elif rightUnit.getTypes() == "air":
                    self.updated = True
                    return 5
                elif leftUnit.getTypes() == "air":
                    self.updated = True
                    return 4
                else:
                    self.updated = True
                    return 0
            case 2:
                if downUnit.getTypes() == "air":
                    self.updated = True
                    return 7
                elif leftUnit.getTypes() == "air":
                    self.updated = True
                    return 4
                elif rightUnit.getTypes() == "air":
                    self.updated = True
                    return 5
                elif rightdownUnit.getTypes() == "air":
                    self.updated = True
                    return 8
                elif leftdownUnit.getTypes() == "air":
                    self.updated = True
                    return 6
                else:
                    self.updated = True
                    return 0
            case _:
                return -1
    def trdirtMove(self,leftUnit,rightUnit,downUnit,leftdownUnit,rightdownUnit) ->int:
        #0:None,1q,2w,3e,4a,5d,6z,7x,8c
        ic = random.randint(1,2)
        if self.updated == True:
            self.updated = False
            return 0
       # ic = 
        match ic:
            case 1:
                if downUnit.getTypes() == "air" or downUnit.getTypes() =="water" :
                    self.updated = True
                    return 7
                elif leftdownUnit.getTypes() == "air" or leftdownUnit.getTypes() =="water":
                    self.updated = True
                    return 6
                elif rightdownUnit.getTypes() == "air" or rightdownUnit.getTypes() =="water":
                    self.updated = True
                    return 8
                else:
                    self.updated = True
                    return 0
            case 2:
                if downUnit.getTypes() == "air" or downUnit.getTypes() =="water" :
                    self.updated = True
                    return 7
                elif rightdownUnit.getTypes() == "air" or rightdownUnit.getTypes() =="water":
                    self.updated = True
                    return 8
                elif leftdownUnit.getTypes() == "air" or leftdownUnit.getTypes() =="water":
                    self.updated = True
                    return 6
                else:
                    self.updated = True
                    return 0
            case _:
                return -1
    def trfireMove(self,leftUnit,rightUnit,upUnit,leftupUnit,rightupUnit) ->int:
            ic = random.randint(1,2)
            if self.updated == True:
                self.updated = False
                return 0
            if self.dyingCT <= 0:
                return 10
        # ic = 
            match ic:
                case 1:
                    if leftUnit.getTypes() == "dirt" or leftUnit.getTypes() == "solid":
                        self.updated = True
                        self.dyingCT -=1
                        return 4
                    elif rightUnit.getTypes() == "dirt" or rightUnit.getTypes() == "solid":
                        self.updated = True
                        self.dyingCT -=1
                        return 5
                    elif leftupUnit.getTypes() == "dirt" or leftupUnit.getTypes() =="solid":
                        self.updated = True
                        self.dyingCT -=1
                        return 1
                    elif rightupUnit.getTypes() == "dirt" or rightupUnit.getTypes() =="solid":
                        self.updated = True
                        self.dyingCT -=1
                        return 3
                    elif upUnit.getTypes() == "dirt" or upUnit.getTypes() =="solid" :
                        self.updated = True
                        self.dyingCT -=1
                        return 2
                    else:
                        self.updated = True
                        self.dyingCT -=1
                        return 0
                case 2:
                    if rightUnit.getTypes() == "dirt" or rightUnit.getTypes() == "solid":
                        self.updated = True
                        self.dyingCT -=2
                        return 5
                    elif leftUnit.getTypes() == "dirt" or leftUnit.getTypes() == "solid":
                        self.updated = True
                        self.dyingCT -=2
                        return 4
                    elif rightupUnit.getTypes() == "dirt" or rightupUnit.getTypes() =="solid":
                        self.updated = True
                        self.dyingCT -=2
                        return 3
                    elif leftupUnit.getTypes() == "dirt" or leftupUnit.getTypes() =="solid":
                        self.updated = True
                        self.dyingCT -=2
                        return 1
                    elif upUnit.getTypes() == "dirt" or upUnit.getTypes() =="solid" :
                        self.updated = True
                        self.dyingCT -=2
                        return 2
                    else:
                        self.updated = True
                        self.dyingCT -=1
                        return 0
                case _:
                    return -1
    def getsizeX(self):
        return self.sizeX
    def getsizeY(self):
        return self.sizeY
    def getTypes(self):
        return self.types
    def getCoodX(self):
        return self.coDx
    def getCoodY(self):
        return self.coDy
    def getUPD(self):
        return self.updated
    def setFi(self,c):
        self.dyingCT = c
    def getFi(self):
        return self.dyingCT
canvas = []
for i in range(160):
    cn = []
    for c in range(200):
        if i == 0 or i == 159:
            e = solid("solid",i*5,c*5,False)
        elif c == 0 or c == 199:
            e = solid("solid",i*5,c*5,False)
        else:
            e = solid("air",i*5,c*5,False)
        cn.append(e)
    canvas.append(cn.copy())
#[0[size200]],[1[size200]],[2[size200]]...[159[size200]]
preinput = ''
run = True
while run:
    screen.fill((255,255,255))
    #Graphics
    for i in range(160):
        for c in range(200):
            #canvas[i][c].getCoodX()
            sphere = pygame.Rect((canvas[i][c].getCoodX(),canvas[i][c].getCoodY(),5,5))
            match canvas[i][c].getTypes():
                case "air":
                    pygame.draw.rect(screen,(255,255,255),sphere,width=0)
                case "solid":
                    pygame.draw.rect(screen,(158, 158, 158),sphere,width=0)
                case "water":
                    pygame.draw.rect(screen,(25, 94, 255),sphere,width=0)
                case "dirt":
                    pygame.draw.rect(screen,(255, 224, 20),sphere,width=0)
                case "fire":
                    pygame.draw.rect(screen,(255, 81, 18),sphere,width=0)
                case _:
                    continue
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #mouse position to coord in matrix
        if event.type == pygame.MOUSEMOTION:
            mxC,myC = pygame.mouse.get_pos()
            mxC = int((mxC-mxC%5)/5)
            myC = int((myC-myC%5)/5)
            if myC>197:
                myC = 197
            if myC<3:
                myC = 3
            if mxC>157:
                mxC = 157
            if mxC<3:
                mxC = 3
        mouseA = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        #determine action
        if keys[pygame.K_1]:
            currentElement = 1
        if keys[pygame.K_3]:
            currentElement = 2
        if keys[pygame.K_2]:
            currentElement = 3
        if keys[pygame.K_0]:
            currentElement = 0
        if keys[pygame.K_4]:
            currentElement = 4
        if mouseA[0]:
            canvas[mxC][myC] = solid("solid",mxC*5,myC*5,False)
            if currentElement == 1:
                for i in range(-2,2):
                    for x in range(-2,2):
                        canvas[mxC+i][myC+x] = solid("solid",(mxC+i)*5,(myC+x)*5,False)
            elif currentElement == 3:
                for i in range(-2,2):
                    for x in range(-2,2):
                        canvas[mxC+i][myC+x] = solid("water",(mxC+i)*5,(myC+x)*5,False)
            elif currentElement == 2:
                for i in range(-2,2):
                    for x in range(-2,2):
                        canvas[mxC+i][myC+x] = solid("dirt",(mxC+i)*5,(myC+x)*5,False)
            elif currentElement == 0:
                for i in range(-2,2):
                    for x in range(-2,2):
                        canvas[mxC+i][myC+x] = solid("air",(mxC+i)*5,(myC+x)*5,False)
            elif currentElement == 4:
                for i in range(-2,2):
                    for x in range(-2,2):
                        canvas[mxC+i][myC+x] = solid("fire",(mxC+i)*5,(myC+x)*5,False)
    #Logics
    wor = canvas.copy()
    for i in range(1,159):
        for c in range(1,199):
            if canvas[i][c].getTypes() == "water":
                match canvas[i][c].trwaterMove(canvas[i-1][c],canvas[i+1][c],canvas[i][c+1],canvas[i-1][c+1],canvas[i+1][c+1]):
                    case 0:
                        continue
                    case 5:#Right
                        wor[i][c] = solid("air",i*5,c*5,False)
                        wor[i+1][c] = solid("water",(i+1)*5,c*5,canvas[i][c].getUPD())
                    case 4:#left
                        wor[i-1][c] = solid("water",(i-1)*5,c*5,canvas[i][c].getUPD())
                        wor[i][c] = solid("air",i*5,c*5,False)
                    case 6:#Leftdown
                        wor[i-1][c+1] = solid("water",(i-1)*5,(c+1)*5,canvas[i][c].getUPD())
                        wor[i][c] = solid("air",i*5,c*5,False)
                    case 7:#Down
                        wor[i][c+1] = solid("water",i*5,(c+1)*5,canvas[i][c].getUPD())
                        wor[i][c] = solid("air",i*5,c*5,False)
                    case 8:#Rightdown
                        wor[i][c] = solid("air",i*5,c*5,False)
                        wor[i+1][c+1] = solid("water",(i+1)*5,(c+1)*5,canvas[i][c].getUPD()) 
                    case _:
                        continue
            elif canvas[i][c].getTypes() == "dirt":
                match canvas[i][c].trdirtMove(canvas[i-1][c],canvas[i+1][c],canvas[i][c+1],canvas[i-1][c+1],canvas[i+1][c+1]):
                    case 0:
                        continue
                    case 6:#Leftdown
                        p = wor[i-1][c+1].getTypes()
                        wor[i-1][c+1] = solid("dirt",(i-1)*5,(c+1)*5,canvas[i][c].getUPD())
                        wor[i][c] = solid(p,i*5,c*5,False)
                    case 7:#Down
                        p = wor[i][c+1].getTypes()
                        wor[i][c+1] = solid("dirt",i*5,(c+1)*5,canvas[i][c].getUPD())
                        wor[i][c] = solid(p,i*5,c*5,False)
                    case 8:#Rightdown
                        p = wor[i+1][c+1].getTypes()
                        wor[i][c] = solid(p,i*5,c*5,False)   
                        wor[i+1][c+1] = solid("dirt",(i+1)*5,(c+1)*5,canvas[i][c].getUPD()) 
                    case _:
                        continue
            elif canvas[i][c].getTypes() == "fire":
                match canvas[i][c].trfireMove(canvas[i-1][c],canvas[i+1][c],canvas[i][c-1],canvas[i-1][c-1],canvas[i+1][c-1]):
                    case 2:#leftUp
                        wor[i][c] = solid("fire",i*5,c*5,canvas[i][c].getUPD())   
                        wor[i-1][c-1] = solid("fire",(i-1)*5,(c-1)*5,canvas[i][c].getUPD())
                    case 1:#up
                        wor[i][c] = solid("fire",i*5,c*5,canvas[i][c].getUPD())
                        wor[i][c-1] = solid("fire",i*5,(c-1)*5,canvas[i][c].getUPD())
                    case 3:#Rightup
                        wor[i][c] = solid("fire",i*5,c*5,canvas[i][c].getUPD())
                        wor[i+1][c-1] = solid("fire",(i+1)*5,(c-1)*5,canvas[i][c].getUPD()) 
                    case 1:#Left
                        wor[i][c] = solid("fire",i*5,c*5,canvas[i][c].getUPD())
                        wor[i-1][c] = solid("fire",(i-1)*5,c*5,canvas[i][c].getUPD())
                    case 3:#Right
                        wor[i][c] = solid("fire",i*5,c*5,canvas[i][c].getUPD())
                        wor[i+1][c] = solid("fire",(i+1)*5,(c)*5,canvas[i][c].getUPD()) 
                    case 0:
                        if canvas[i][c-1].getTypes() == "air":
                            wor[i][c-1] = canvas[i][c]
                            wor[i][c-1].setFi(canvas[i][c].getFi())
                            #canvas[i][c] = solid("air",i*5,c*5,canvas[i][c].getUPD())
                        if canvas[i][c-1].getTypes() == "fire":
                            continue
                        else:
                            wor[i][c]= solid("air",i*5,c*5,canvas[i][c].getUPD())
                    case 10:
                            wor[i][c]= solid("air",i*5,c*5,canvas[i][c].getUPD())
                    case _:
                        continue
    canvas = wor.copy()
    #print("Position x: ",canvas[int((mxC-mxC%5)/5)][int((myC-myC%5)/5)].getCoodX(),"  Position y: ",canvas[int((mxC-mxC%5)/5)][int((myC-myC%5)/5)].getCoodY())
    #pygame.time.wait(1000)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()


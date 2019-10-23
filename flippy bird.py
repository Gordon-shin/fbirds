import pygame,sys

class Bird(object):
    def __init__(self):
        """"df"""
        self.birdStatus = [pygame.image.load("resource/1.png"),
                           pygame.image.load("resource/2.png"),
                           pygame.image.load("resource/dead.png")
                           ]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jumpSpeed = 12
        self.gravity = 4
        self.dead =False

    def Movebird(self):
        if self.jump:
            self.jumpSpeed -=0.7
            self.birdY -= self.jumpSpeed
        else:
            self.gravity +=0.2
            self.birdY += self.gravity


class PipeLine(object):
    '''定义管道类'''
    def __init__(self):
        self.wallx = 400
        self.pipleUp = pygame.image.load("resource/top.png")
        self.pipleDown = pygame.image.load("resource/bottom.png")

    def MovePipeLine(self):
       self.wallx -=5
       if self.wallx < -80:
           self.wallx = 400
pygame.init()
windows = [420,640]
screen = pygame.display.set_mode((windows))
clock = pygame.time.Clock()
Bird = Bird()
PipeLine = PipeLine()
def createMap(windows):
    background = pygame.image.load("resource/background.png")
    background = pygame.transform.scale(background, windows)  # 将图片拉伸到和窗口一样宽
    screen.blit(background, (0, 0))
    createBird()
    createPillar("up")
    createPillar("down")
    PipeLine.MovePipeLine()
    pygame.display.update()

def createPillar(updown):
    if(updown=="up"):
        screen.blit(PipeLine.pipleUp,(PipeLine.wallx,-300))
    else:
        screen.blit(PipeLine.pipleDown,(PipeLine.wallx,500))

def createBird():
    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1
    else:
        Bird.status = 0
    screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))
    Bird.Movebird()


if __name__ == '__main__':
    while True:
        clock.tick(60)
        for event in pygame.event.get(): #获取所有的事件
            ''' print(Bird.status)
                        print(Bird.jumpSpeed)
                        print(Bird.gravity)
                        '''
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN and not Bird.dead:
                Bird.jump = True
                #print(Bird.jubmpSpeed)
                #print(Bird.birdY)
                Bird.jumpSpeed = 12
                Bird.gravity = 4
            else:
                Bird.jump = False
                Bird.jumpSpeed = 12
                Bird.gravity = 4
        createMap(windows)


import pygame
import sys
#初始化pygame
pygame.init()
speed = [5,5]
windows = [1000,500]
screen = pygame.display.set_mode((windows[0],windows[1]))# 设置窗口
ball = pygame.image.load('./resource/qiu.png')
ballrect = ball.get_rect()
angle = 1
#print(ballrect)
clock= pygame.time.Clock() #pygame 时间模块

while True:
    clock.tick(60)#本循环每秒执行时间
    for event in pygame.event.get(): #获取所有的事件
        if event.type == pygame.QUIT:
            exit()
    #-------------碰撞检测-----------------------------
    if ballrect.left< 0 or ballrect.right>windows[0]:
        speed[0] =-speed[0]
    if ballrect.top<0 or ballrect.bottom> windows[1]:
        speed[1] = -speed[1]
    #--------------------------------------------------
    newball = pygame.transform.rotate(ball,angle)
    angle -=1
    ballrect = ballrect.move(speed) #speed表示 rect元组前两位参数的增加量
    screen.fill((255,255,255))
    screen.blit(newball,ballrect);
    '''ballrect表示小球的矩形框 （位置的意思）
     /ball表示图片（surface）'''
    pygame.display.update()

import pygame
import sys
#初始化pygame
pygame.init()

screen = pygame.display.set_mode((320,420))

while True:
    for event in pygame.event.get(): #获取所有的事件
        if event.type == pygame.QUIT:
            exit()

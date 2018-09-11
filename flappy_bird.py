import pygame
import sys
import random
from pygame.locals import *

def print_text(font, x, y, text, color=(0, 0, 0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

pygame.init()

font1 = pygame.font.SysFont('simhei', 24)
window_width,window_height=800,600
screen=pygame.display.set_mode((window_width,window_height))
bd_image = pygame.image.load("resources/images/background2.8.png")
bird_image = pygame.image.load("resources/images/1212.png")
bird_width, bird_height = bird_image.get_size()
pillar1_image = pygame.image.load("resources/images/1313.png")
pillar2_image = pygame.image.load("resources/images/1414.png")
pygame.display.set_caption('。。。')
bird_image = pygame.transform.smoothscale(bird_image, (50, 50))
bird_left, bird_top = 0, 50

while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            if mouse_down == 1:
                bird_top = bird_top - 35
    bird_top = bird_top + 2
    if bird_top >= 550:
        bird_top = 550
    if bird_top <= 0:
        bird_top = 0
    screen.blit(bd_image, (0, 0))
    screen.blit(bird_image, (bird_left, bird_top))
    screen.blit(pillar1_image, (0, 0))
    screen.blit(pillar2_image, (0, 300))
    print_text(font1, 0, 0, str(bird_top))
    pygame.display.update()
# 其他事件
# QUIT            点击关闭按钮时触发
# KEYDOWN         按键按下时触发
# KEYUP           按键抬起时触发
# MOUSEMOTION     鼠标移动时触发
# MOUSEBUTTONUP   鼠标按下时触发
# MOUSEBUTTONDOWN 鼠标抬起时触发

# Import libraries
import re
import pygame
import time
import random

# Constants
DISPLAY_WIDTH = 1080
DISPLAY_HEIGHT = 600
SPEED = 2




# Checkpoints

CHECKPOINT_1 = (
    (999, 582),(988, 493),(969, 472),(944, 462),
    (873, 454),(846, 438),(821, 413),(806, 367),
    (815, 314),(837, 280),(897, 263),(972, 244),
    (993, 215),(1008, 172),(1008, 172),(997, 127),
    (975, 93),(938, 74),(869, 68),(800, 66),(743, 43),
    (698, 43),(659, 66),(512, 68),(421, 74),(392, 105),
    (374, 146),(372, 211),(341, 248),(251, 269),(204, 291)
    ,(188, 330),(180, 410),(143, 440),(120, 454),(-25, 452)
)







CHECKPOINT_1 = list(CHECKPOINT_1)





# Functions
def quit_game():
    pygame.quit()
    quit()

def running(sprite_mov,rect, target, speed):
    pos = pygame.Vector2(rect.center)
    target = pygame.Vector2(target)
    dt = speed

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit_game()

    pos = pos.move_towards(target, dt)
    rect.center = pos


    sprite_mov.draw(game_display)





def Map(CP,sprite_mov,rect):
    
        try:
            running(sprite_mov,rect,CP[0],1)




            c_pos = rect.center
            if c_pos == CP[0]:
                del CP[0]
        except Exception:
            pass
            






# Main
size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
game_display = pygame.display.set_mode(size)

















#####SPAM#####

# class Entities():
#         def __init__(self,surface,rectangle):
#             self.surf = surface
#             self.rect = rectangle


#         def running(self,target,speed=2):
#             self.pos = pygame.Vector2(self.rect.center)
#             self.target = pygame.Vector2(target)
#             self.dt = speed
#             events = pygame.event.get()
#             for event in events:
#                 if event.type == pygame.QUIT:
#                     quitgame()

#             self.pos = self.pos.move_towards(target, self.dt)
#             self.rect.center = self.pos

#             gameDisplay.blit(self.surf,self.rect)





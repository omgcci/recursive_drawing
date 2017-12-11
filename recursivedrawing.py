import pygame
from pygame.locals import *
import sys





def recursive_draw(x, y, width, height, count):
    pygame.draw.line(DS, White,
                     [x + width*.20, height // 3 + y],
                     [x + width*.90, height // 3 + y],
                     1)
    pygame.draw.line(DS, Black,
                     [x + width * .25, (height * .5) // 2 + y],
                     [x + width * .25,  (height * 1.5) // 2 + y],
                     9)
    pygame.draw.line(DS, Blue,
                     [x + width * .75, (height * .5) // 2 + y],
                     [x + width * .75, (height * 1.5) // 2 + y],
                     1)
    pygame.draw.line(DS, Purple,
                     [x - width // 3, (height + (y*.7))],
                     [x - width // 2, (height + (y*.7))],
                     1)
    pygame.draw.line(DS, Red,
                     [x + width * .9, (height + (y*.15))],
                     [x + width * .3, (height - (y*.7))],
                     )
 
    if count > 0:
        count -= 1
        # Top left
        recursive_draw(x+.1, y+.1, width // 2, height // 2, count)
        # Top right
        recursive_draw(x + width // 2, y, width // 2, height // 2, count)
        # Bottom left
        recursive_draw(x, y + width // 2, width, height, count)
        # Bottom right
        recursive_draw(x + width // 3, y + height, width*.5, height // 2, count)
 




##################
            
W, H = 1200, 768
Black = (0, 0, 0)
Red = (255, 0, 0)
Purple = (102, 0, 255)
Blue = (0, 255, 255)
White = (255, 255, 255)
qq = False

##################
pygame.init()
FPS = 1
DS = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
print(type(DS))
CLOCK = pygame.time.Clock()
pygame.display.get_surface
DS.get_shifts
while not qq:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            qq = True
            pygame.display.quit
            pygame.quit()
            sys.exit()
    DS.fill(White)
    recursive_draw(20, 20, 1900, 40, 10)
    pygame.display.flip()
    CLOCK.tick(FPS)


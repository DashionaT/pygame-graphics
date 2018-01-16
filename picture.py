import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Winter Night"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (1, 53, 1)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0)
BROWN = (143, 82, 52)
ORANGE = (217, 103, 19)
GREY = (149, 134, 135)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

''' Make stars'''
   
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    ''' sky '''
    screen.fill(BLACK)

    ''' moon '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)

    '''stars'''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)
        
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, BROWN, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, BROWN, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, BROWN, [0, 410], [800, 410], 5)


    '''snowman'''
    pygame.draw.ellipse(screen, WHITE, [300, 375, 200, 200])
    pygame.draw.ellipse(screen, WHITE, [325, 270, 150, 150])
    pygame.draw.ellipse(screen, WHITE, [350, 200, 100, 100])

    '''arms'''
    pygame.draw.line(screen, BROWN, [465, 320], [500, 245], 10)
    pygame.draw.line(screen, BROWN, [300, 240], [340, 315], 10)
    
    '''buttons'''
    pygame.draw.ellipse(screen, BLACK, [395, 300, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [395, 350, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [395, 400, 15, 15])

    '''eyes'''
    pygame.draw.ellipse(screen, BLACK, [375, 225, 10, 10])
    pygame.draw.ellipse(screen, BLACK, [410, 225, 10, 10])

    '''nose'''
    pygame.draw.polygon(screen, ORANGE, [[403, 240], [403, 255], [425, 248]])

    '''hat'''           
    pygame.draw.rect(screen, GREY, [375, 150, 50, 55])
    pygame.draw.rect(screen, GREY, [363, 190, 75, 25])
   
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

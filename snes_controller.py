import pygame

import pygame
from Commodore_64_color_palettes import *

pygame.init()

screen_width = 640  
screen_height = 480
boarder_width  = 40
TITLE = "SNES"
BGCOLOR = CC_LIGHTBLUE



# for all the connected joysticks
joysticks = []
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick '", joysticks[-1].get_name() ,"'")

joy_name = ""
joy_x = 0
joy_y = 0
joy_btn_a = False
joy_btn_b  = False
joy_btn_x = False
joy_btn_y = False
joy_btn_l = False
joy_btn_r = False
joy_btn_start = False
joy_btn_select  = False

font = pygame.font.Font('Fixedsys500c.ttf', 32)

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption(TITLE)

all_sprites_list = pygame.sprite.Group()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        elif event.type == pygame.JOYAXISMOTION:
            joy_name = joysticks[event.joy].get_name().strip()
            joy_x = round(joysticks[event.joy].get_axis(0))
            joy_y = round(joysticks[event.joy].get_axis(1))
            if not(joy_x == 0 and  joy_y == 0):
                print(joy_name, joy_x, joy_y)
        elif event.type == pygame.JOYBUTTONDOWN:
            joy_name = joysticks[event.joy].get_name().strip()
            if event.button == 0:
                print("A pressed")
                joy_btn_a = True
            if event.button == 1:
                print("B pressed")
                joy_btn_b = True
            if event.button == 2:
                print("X pressed")
                joy_btn_x = True
            if event.button == 3:
                print("Y pressed")
                joy_btn_y = True
            if event.button == 4:
                print("L pressed")
                joy_btn_l = True
            if event.button == 5:
                print("R pressed")
                joy_btn_r = True
            if event.button == 6:
                print("Select pressed")
                joy_btn_select = True
            if event.button == 7:
                print("Start pressed")
                joy_btn_start = True
        elif event.type == pygame.JOYBUTTONUP:
            joy_name = joysticks[event.joy].get_name().strip()
            if event.button == 0:
                print("A released")
                joy_btn_a = False
            if event.button == 1:
                print("B released")
                joy_btn_b = False
            if event.button == 2:
                print("X released")
                joy_btn_x = False
            if event.button == 3:
                print("Y released")
                joy_btn_y = False
            if event.button == 4:
                print("L released")
                joy_btn_l = False
            if event.button == 5:
                print("R released")
                joy_btn_r = False
            if event.button == 6:
                print("Select released")
                joy_btn_select = False
            if event.button == 7:
                print("Start released")
                joy_btn_start = False
                
    # Clear the screen
    screen.fill(WHITE)

    
    joy_label = font.render(joy_name, True, BLACK, WHITE)
    screen.blit(joy_label, [0,0]) 
    
    #snes controller
    snes_x  =  270
    snes_y  = 150
    snes_h = 70
    snes_w = 120
    snes_r = 40

    #shoulder buttons
    pygame.draw.arc(screen, CC_GREY, (snes_x-snes_r-3, snes_y-3, snes_r*2, snes_r*2), 20.1, 21.5, 8)
    pygame.draw.arc(screen, CC_GREY, (snes_x+snes_w-snes_r+3, snes_y-3, snes_r*2, snes_r*2)
                    , 19.4, 20.8, 8)


    
    pygame.draw.rect(screen, CC_LIGHTGREY, [snes_x
                                       , snes_y
                                       , snes_w
                                       , snes_h])

    pygame.draw.circle(screen, CC_LIGHTGREY, [snes_x, snes_y+snes_r], snes_r)
    pygame.draw.circle(screen, CC_LIGHTGREY, [snes_x+snes_w, snes_y+snes_r], snes_r)

    #d-pad
    pygame.draw.rect(screen, CC_DARKGREY,  [snes_x-6, snes_y+20, 12, 36])
    pygame.draw.rect(screen, CC_DARKGREY,  [snes_x-18, snes_y+32, 36, 12])

    

    pygame.draw.circle(screen, CC_BLUE, [snes_x + snes_w-5 , snes_y + 25 ], snes_r//4)
    pygame.draw.circle(screen, CC_RED, [snes_x + snes_w+20 , snes_y + 35 ], snes_r//4)

    pygame.draw.circle(screen, CC_GREEN, [snes_x + snes_w-20 , snes_y + 45 ], snes_r//4)
    pygame.draw.circle(screen, CC_YELLOW, [snes_x + snes_w+5 , snes_y + 55 ], snes_r//4)

    #select/start
    pygame.draw.ellipse(screen, CC_GREY, [snes_x + snes_w/4 +5, snes_y + (snes_h - snes_h/4), 20, 10])
    pygame.draw.ellipse(screen, CC_GREY, [snes_x + snes_w/2 +5, snes_y + (snes_h - snes_h/4), 20, 10])

    if not(joy_x == 0):
        if (joy_x == 1):
            #right
            pygame.draw.rect(screen, (255,0,0),  [snes_x, snes_y+32, 36//2, 12])
        elif(joy_x == -1):
            #left
            pygame.draw.rect(screen, (255,0,0),  [snes_x-18, snes_y+32, 36//2, 12])
    
    if not(joy_y == 0):
        if (joy_y == 1):
            #down
            pygame.draw.rect(screen, (255,0,0),  [snes_x-6, snes_y+40, 12, 36//2])
        elif(joy_y == -1):
            #up
            pygame.draw.rect(screen, (255,0,0),  [snes_x-6, snes_y+20, 12, 36//2])
    if (joy_btn_a):
        pygame.draw.circle(screen, (255,0,0), [snes_x + snes_w+20 , snes_y + 35 ], snes_r//4)
    if (joy_btn_b):
        pygame.draw.circle(screen, (255,255,0), [snes_x + snes_w+5 , snes_y + 55 ], snes_r//4)
    if (joy_btn_x):
        pygame.draw.circle(screen, (0,0,255), [snes_x + snes_w-5 , snes_y + 25 ], snes_r//4)
    if (joy_btn_y):
        pygame.draw.circle(screen, (0,255,0), [snes_x + snes_w-20 , snes_y + 45 ], snes_r//4)
    if (joy_btn_l):
        pygame.draw.arc(screen, (255,0,0), (snes_x-snes_r-3, snes_y-3, snes_r*2, snes_r*2), 20.1, 21.5, 8)
    if (joy_btn_r):
        pygame.draw.arc(screen, (255,0,0), (snes_x+snes_w-snes_r+3, snes_y-3, snes_r*2, snes_r*2)
                    , 19.4, 20.8, 8)
    if (joy_btn_select):
        pygame.draw.ellipse(screen, (255,0,0), [snes_x + snes_w/4 +5, snes_y + (snes_h - snes_h/4), 20, 10])
    if (joy_btn_start):
        pygame.draw.ellipse(screen, (255,0,0), [snes_x + snes_w/2 +5, snes_y + (snes_h - snes_h/4), 20, 10])

    # Draw all the spites
    all_sprites_list.draw(screen)

    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

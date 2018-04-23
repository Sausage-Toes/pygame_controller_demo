import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super(Block,self).__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        

pygame.init()
# Set the height and width of the screen
screen_width = 320
screen_height = 240
#screen_width = 640
#screen_height = 480

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('TITLE')

# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Create a RED player block
player = Block(RED, 15, 15)
player.rect.x = screen_width/2
player.rect.y = screen_height/2
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

use_joystick =  False
joystick = None

joy_name = pygame.joystick.Joystick(0).get_name()
joy_name = joy_name.strip().lower()

print ("'",joy_name,"'")

font = pygame.font.SysFont('Calibri', 12, True, False)
joyname_text = font.render(pygame.joystick.Joystick(0).get_name(),True,BLACK)
screen.blit(joyname_text, [10, 10])


if joy_name == "2600-daptor ii" \
   or joy_name == "motioninJoy virtual game controller" \
   or joy_name == "usb gamepad" \
   or joy_name == "thec64 joystick" \
   or joy_name == "controller (xbox 360 wireless receiver for windows)":
    print ("Joystick found!")
    # Initialize the joystick
    pygame.joystick.Joystick(0).init()
    joystick = pygame.joystick.Joystick(0)
    use_joystick =  True
    
joy_x = 0
joy_y = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.JOYAXISMOTION:
            joy_x = round(joystick.get_axis(0))
            joy_y = round(joystick.get_axis(1))
            # -0.0 REALY? MINUS ZERO?
            if joy_x == 0: joy_x =  abs(joy_x)
            if joy_y == 0: joy_y =  abs(joy_y)
            print ("x:",joy_x," y:",joy_y)
        elif event.type == pygame.JOYBUTTONDOWN:
            print ("FIRE!")
        elif event.type == pygame.KEYDOWN:
            print ("Keydown,", event.key)


            
    # Clear the screen
    screen.fill(WHITE)
    screen.blit(joyname_text, [0, 0])
    
    #GetJoystick()
    player.rect.x = player.rect.x + joy_x
    player.rect.y = player.rect.y + joy_y

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()




    












    

import pygame
from pygame.locals import *
from player import Player
from block import Block

import pygame
import random
import time


class game:
    def __init__(self,debug):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.width=1400
        self.height=800
        self.playerQuit=False


def ApplyGravity(self,all_sprites_list):
    for sprite in all_sprites_list:
	       if(sprite.gravity==True):
		             sprite.rect.y=1
time.sleep(0.01)

def ClimbObsticle(self,player,block_list):
    blocks_hit = pygame.sprite.spritecollide(player, block_list,False)
    for hit_block in blocks_hit:
        if(player.rect.yplayer.height < hit_block.rect.y or
    	       player.rect.y < hit_block.rect.yplayer.height
    	          ):
    	             player.rect.y = hit_block.rect.y-player.height
def run(self):
 #####################################
    # Initialize Pygame
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    pygame.init()



    # Set the height and width of the screen
    screen_width = 1400
    screen_height = 800
    screen = pygame.display.set_mode([screen_width, screen_height])

    player = Player(RED, 10, 15)
    player.rect.y=screen_height/4
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()

    # This is a list of every sprite.
    # All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()


    lag = screen_height/4
    for i in range(screen_width/player.width):
   # This represents a block
        block = Block(BLACK, 20, 15)

   # Set a random location for the block
    block.rect.x = i*block.width
    block.rect.y = (lag-15)
    random.randrange(30)
    lag = block.rect.y
   # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

    # Create a RED player block

    all_sprites_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

   # Clear the screen
    screen.fill(WHITE)

    self.ApplyGravity(all_sprites_list)
    self.ClimbObsticle(player,block_list)



    keys=pygame.key.get_pressed()
    player.flush()
    if keys[K_LEFT]:
        player.moveleft(screen_width)

        if keys[K_RIGHT]:
            player.moveright(screen_width)






   # Get the current mouse position. This returns the position
   # as a list of two numbers.
        '''pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location


   player.rect.x = pos[0]
   player.rect.y = pos[1]
   # See if the player block has collided with anything.
   blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

   # Check the list of collisions.
   for block in blocks_hit_list:
       score = 1
       print(score)
       '''
   # Draw all the spites
        all_sprites_list.draw(screen)

   # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

   # Limit to 60 frames per second
        clock.tick(60)
    ###############################################
    pygame.quit()
    if __name__ == "__main__" :
        theApp = game(False)

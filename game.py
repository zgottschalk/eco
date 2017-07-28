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
                sprite.rect.y+=1
        time.sleep(0.01)

    def ClimbObsticle(self,player,block_list):
        blocks_hit = pygame.sprite.spritecollide(player, block_list,False)
        for hit_block in blocks_hit:
            if(player.rect.y+player.height < hit_block.rect.y or
                player.rect.y < hit_block.rect.y+player.height):
                player.rect.y = hit_block.rect.y-player.height
    def run(self):

        GREEN = (  24,   180,   19)
        WHITE = (107, 239, 209)
        BROWN   = (125,   86,   13)
        pygame.init()
        screen_width = 1400
        screen_height = 900
        screen = pygame.display.set_mode([screen_width, screen_height])
        background = pygame.image.load("jungletemple.jpg")
        player = Player(BROWN, 10, 15)
        player.rect.y=screen_height/4



        subblocks_list = pygame.sprite.Group()

        block_list = pygame.sprite.Group()

        all_sprites_list = pygame.sprite.Group()

        lag = screen_height/4
        for i in range(int(screen_width/player.width)):
            # This represents a block
            block = Block(GREEN, 20, 15)

            # Set a random location for the block
            block.rect.x = i*block.width
            block.rect.y = (lag-15) + random.randrange(30)
            height=block.rect.y
            while(height < screen_height ):
                subblock = Block(GREEN, 20, 15)
                subblock.rect.x=block.rect.x
                height = height + subblock.height
                subblock.rect.y= height
                subblocks_list.add(subblock)
                all_sprites_list.add(subblock)


            lag = block.rect.y
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)

        all_sprites_list.add(player)

        done = False
        clock = pygame.time.Clock()
        background = pygame.image.load("jungletemple.jpg")
        pygame.mixer.music.load("Indiana_Jones_Theme.mp3")
        pygame.mixer.music.play(-1,0.0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
        # -------- Main Program Loop -----------
                            while not True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:


            # Clear the screen
                                        screen.blit(background, [0,0])
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
                score += 1
                print(score)
            '''
            # Draw all the spites that may need to be drawn
            all_sprites_list.draw(screen)



            # Go ahead and update the screen with what we've drawn.
            pygame.image.load("jungletemple.jpg")

            pygame.display.flip()
            # Limit to 60 frames per second
            clock.tick(120)

        pygame.quit()
#############################################
if __name__ == "__main__" :
    theApp = game(False)

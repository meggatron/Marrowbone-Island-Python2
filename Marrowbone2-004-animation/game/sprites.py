# Marrowbone2-004-pygame-GUI/game/sprites.py


# import pygame for sprites, images, keyboard input, and movement
import pygame

# import os so we can build paths to our image files
import os


# create our PlayerSprite Class
# pygame.sprite.Sprite is the parent Class
class PlayerSprite(pygame.sprite.Sprite):

    # initialize a new PlayerSprite with an x and y position
    def __init__(self, x, y):

        # run the initializer from the parent Sprite Class
        super().__init__()


        # load the first animation image from the assets folder
        self.image1 = pygame.image.load(
            os.path.join("assets", "orca-1.png")
        ).convert_alpha()

        ############################################
        # resize the first image to 240 x 240 pixels
        # TYPO CHECK FROM YESTERDAY
        # there must be a comma between self.image1 and (240, 240)
        self.image1 = pygame.transform.scale(
            self.image1, (240, 240)
        )

        ########################################################
        # load the second animation image from the assets folder
        # TYPO CHECK FROM YESTERDAY
        # I had convert.alpha() on the slide
        # the correct method is convert_alpha() with an underscore
        self.image2 = pygame.image.load(
            os.path.join("assets", "orca-2.png")
        ).convert_alpha()


        # resize the second image to 240 x 240 pixels
        self.image2 = pygame.transform.scale(
            self.image2, (240, 240)
        )


        # pygame draws whatever image is currently stored in self.image
        # start with our first animation image
        self.image = self.image1


        # create a rectangle that stores the sprite's position
        # center it at the x and y values passed into the Class
        self.rect = self.image.get_rect(center=(x, y))


        # how many pixels the sprite moves each update
        self.speed = 4

        # keep track of when to switch animation images
        self.animation_counter = 0


    # update() controls what the sprite does as the game updates
    def update(self):

        # check which keyboard keys are currently being pressed
        keys = pygame.key.get_pressed()


        # moving will be True if any arrow key is being pressed
        # otherwise moving will be False
        moving = (
            keys[pygame.K_LEFT]
            or keys[pygame.K_RIGHT]
            or keys[pygame.K_UP]
            or keys[pygame.K_DOWN]
        )


        # if the player is moving, advance the animation
        if moving:

            # add 1 each time update() runs while we are moving
            self.animation_counter += 1


            # % is the modulo operator
            # it gives us the remainder after division
            # this lets us repeatedly switch between our two images
            if self.animation_counter % 20 < 10:
                self.image = self.image1

            else:
                self.image = self.image2


        # if no arrow keys are pressed, stop the animation
        else:

            # return to the first image
            self.image = self.image1

            # reset the animation counter
            self.animation_counter = 0


        # move left by subtracting speed from the x position
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed


        # move right by adding speed to the x position
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


        # move up by subtracting speed from the y position
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed


        # move down by adding speed to the y position
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
# Marrowbone2-009-backgrounds/game/sprites.py

import pygame
import os


class PlayerSprite(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image1 = pygame.image.load(
            os.path.join("assets", "orca-1.png")
        ).convert_alpha()

        self.image2 = pygame.image.load(
            os.path.join("assets", "orca-2.png")
        ).convert_alpha()

        self.image1 = pygame.transform.scale(
            self.image1,
            (160, 180)
        )

        self.image2 = pygame.transform.scale(
            self.image2,
            (160, 180)
        )

        # New artwork faces left.
        # Create right-facing versions by flipping it.
        self.image1_right = pygame.transform.flip(
            self.image1,
            True,
            False
        )

        self.image2_right = pygame.transform.flip(
            self.image2,
            True,
            False
        )

        # Orca starts facing right.
        self.facing = "right"
        self.image = self.image1_right

        self.rect = self.image.get_rect(
            center=(x, y)
        )

        self.speed = 4
        self.animation_counter = 0
        self.talking = False
        self.talk_timer = 0

    def update(self):

        keys = pygame.key.get_pressed()

        moving = (
            keys[pygame.K_LEFT]
            or keys[pygame.K_RIGHT]
            or keys[pygame.K_UP]
            or keys[pygame.K_DOWN]
        )

        # Remember horizontal direction
        if keys[pygame.K_LEFT]:
            self.facing = "left"
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.facing = "right"
            self.rect.x += self.speed

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Animate while moving
        if moving:

            self.animation_counter += 1

            if self.animation_counter % 20 < 10:
                frame = 1
            else:
                frame = 2

            self.set_frame(frame)

        # Animate while talking
        elif self.talking:

            self.animation_counter += 1

            if self.animation_counter % 20 < 10:
                frame = 1
            else:
                frame = 2

            self.set_frame(frame)

            self.talk_timer -= 1

            if self.talk_timer <= 0:
                self.talking = False
                self.set_frame(1)

    def set_frame(self, frame):

        if self.facing == "left":

            if frame == 1:
                self.image = self.image1
            else:
                self.image = self.image2

        else:

            if frame == 1:
                self.image = self.image1_right
            else:
                self.image = self.image2_right

    def talk(self):
        self.talking = True
        self.talk_timer = 90
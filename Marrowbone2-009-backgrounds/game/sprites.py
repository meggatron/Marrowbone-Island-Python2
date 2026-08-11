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

        self.image1 = pygame.transform.scale(self.image1, (240, 240))
        self.image2 = pygame.transform.scale(self.image2, (240, 240))

        self.image = self.image1

        self.rect = self.image.get_rect(center=(x, y))

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

        if moving:

            self.animation_counter += 1

            if self.animation_counter % 20 < 10:
                self.image = self.image1
            else:
                self.image = self.image2

            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed

            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

            if keys[pygame.K_UP]:
                self.rect.y -= self.speed

            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
        if self.talking:

            self.animation_counter += 1

            if self.animation_counter % 20 < 10:
                self.image = self.image1
            else:
                self.image = self.image2

            self.talk_timer -= 1

            if self.talk_timer <= 0:
                self.talking = False
                self.image = self.image1

    def talk(self):
        self.talking = True
        self.talk_timer = 90
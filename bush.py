import pygame
from player import player


class Bush(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bush.gif")
        self.rect = self.image.get_rect()
        self.locx = x
        self.locy = y
        self.rect.x = x
        self.rect.y = y

    def weaponfound(self):
        if self.rect.colliderect(player.hitbox):
            print("YOU FOUND AN AXE")
            player.weapon = player.axe
            self.rect.x = -100
            self.rect.y = -100

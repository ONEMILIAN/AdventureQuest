import pygame
from player import player
from setup import setup


class Bush(pygame.sprite.Sprite):
    def __init__(self, rectx, recty):
        super().__init__()
        self.image = pygame.image.load("bush.gif")
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty

    def weaponfound(self):
        if self.rect.colliderect(player.hitbox):
            print("YOU FOUND AN AXE")
            player.weapon = player.axe
            self.rect.x = -100
            self.rect.y = -100

    def draw(self, posx, posy):
        setup.screen.blit(self.image, (posx, posy))

    def drawrect(self, rectcolor):
        pygame.draw.rect(setup.screen, rectcolor, self.rect)


class Bush2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("bush.gif")

    def draw(self, posx, posy):
        setup.screen.blit(self.img, (posx, posy))

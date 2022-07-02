import pygame

from player import player
from mouse import mouse
from setup import setup


class Enemys:
    def __init__(self, x, y):
        self.enemys = pygame.image.load("goblin.gif")
        self.enemysdead = pygame.image.load("goblin_dead.gif")
        self.currentstate = self.enemys
        self.life = 5
        self.enemyx = x
        self.enemyy = y
        self.enemyrect2 = self.currentstate.get_rect()
        self.enemyrect2.x = self.enemyx
        self.enemyrect2.y = self.enemyy

    def draw(self):
        setup.screen.blit(self.currentstate, (self.enemyx, self.enemyy))

    def drawrect(self, rectcolor):
        pygame.draw.rect(setup.screen, rectcolor, self.enemyrect2)

    def getdamage(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and self.enemyrect2.colliderect(mouse.mouserect) and player.hitbox.colliderect(self.enemyrect2):
                self.life += -player.weapon
                print(self.life)

    def makedamage(self):
        if self.enemyrect2.colliderect(player.hitbox):
            player.life += -0.1 / player.currentshield

    def death(self):
        if self.life < 0:
            self.life = 0
            print("IT'S DEAD!! +250XP")
            player.xp += 250
            player.score += 90
            self.currentstate = self.enemysdead
            self.enemyrect2.x = -100
            self.enemyrect2.y = -100


enemys = Enemys(0, 0)

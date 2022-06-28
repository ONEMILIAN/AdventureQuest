import pygame

from player import player
from mouse import mouse


class Enemys:
    def __init__(self, x, y):
        self.enemys = pygame.image.load("goblin.gif")
        self.enemysdead = pygame.image.load("goblin_dead.gif")
        self.currentstate = self.enemys
        self.life = 5
        self.enemyx = x
        self.enemyy = y
        self.enemyrect = pygame.Rect(x, y, 32, 32)
        self.enemyrect2 = self.currentstate.get_rect()
        self.enemyrect2.x = x
        self.enemyrect2.y = y


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
            self.enemyrect.x = -100
            self.enemyrect.y = -100

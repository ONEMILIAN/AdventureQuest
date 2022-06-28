import pygame
import sys


class Player:
    def __init__(self):
        self.character = pygame.image.load("character.gif")
        self.characterleft = pygame.image.load("character_links.gif")
        self.characterdown = pygame.image.load("character_unten.gif")
        self.characterright = pygame.image.load("character_rechts.gif")
        self.currentchar = self.character
        self.playerx = 400
        self.playery = 300
        self.armor = 0
        self.life = 100
        self.maxlife = 100
        self.potions = 5
        self.lvl = 1
        self.mana = 50
        self.maxmana = 50
        self.xp = 0
        self.ore = 0
        self.score = 0
        self.hitbox = pygame.Rect(self.playerx, self.playery, 15, 15)
        self.sword = 1
        self.axe = 2
        self.bettersword = 3
        self.weapon = self.sword
        self.none = 1
        self.shield = 2
        self.currentshield = self.none

    def movement(self, playerX_change, playerY_change):
        self.playerx += playerX_change
        self.playery += playerY_change

    def gameover(self):
        if self.life <= 0:
            print("GAME OVER")
            pygame.quit()
            sys.exit()

    def level2up(self):
        if self.xp > 999:
            self.lvl += 1
            self.maxlife += 12
            self.maxmana += 6
            print("LEVEL UP!!!")
            self.life = self.maxlife
            self.mana = self.maxmana
            self.xp = 0

    def nomana(self):
        if self.mana < 0:
            self.mana = 0

player = Player()

import pygame


class Ladderrect:
    def __init__(self, posx, posy):
        self.rect = pygame.Rect(posx, posy, 32, 32)


ladder = Ladderrect(610, 40)

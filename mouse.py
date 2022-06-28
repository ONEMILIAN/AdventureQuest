import pygame


class Mouse:
    def __init__(self):
        pygame.init()
        self.posx, self.posy = pygame.mouse.get_pos()
        self.mouserect = pygame.Rect(self.posx, self.posy, 2, 2)


mouse = Mouse()

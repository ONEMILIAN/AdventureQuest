import pygame
from player import player

coordinates_x = [0, 100, 200, 300, 400, 500, 600, 700]
coordinates_y = [0, 100, 200, 300, 400, 500]

class Hole:
    def __init__(self):
        self.holerect = pygame.Rect(coordinates_x[4], coordinates_y[1], 15, 15)

    def falling(self):
        if self.holerect.colliderect(player.hitbox):
            player.life += -9
            print("YOU HAVE FALLEN INTO A HOLE!")
            player.playerx = 400
            player.playery = 300


hole = Hole()

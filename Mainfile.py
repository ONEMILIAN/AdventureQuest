import sys
import pygame
from tkinter import *
from shop1 import Buymenu

coordinates_x = [0, 100, 200, 300, 400, 500, 600, 700]
coordinates_y = [0, 100, 200, 300, 400, 500]
running = True

perfectgreen = 100, 255, 100
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


class Gamestate:
    def __init__(self):
        self.state = "intro"

    def statemanager(self):
        if self.state == "main_game":
            gamestate.main_game()
            pygame.display.update()
        if self.state == "intro":
            gamestate.intro()
            pygame.display.update()

    def intro(self):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gamestate.main_game()
            game.screen.blit(game.title, (0, 0))
            pygame.display.update()

    def main_game(self):
        game.run()

    def shop1(self):
        player.playerx = 400
        player.playery = 300
        buymenu.buying()
        pygame.display.update()


class Bush(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bush.gif")
        self.rect = self.image.get_rect()
        self.locx = [50, 150, 250, 350, 450, 550, 650]
        self.locy = [50, 150, 250, 350, 450, 550]
        self.rect.x = self.locx[2]
        self.rect.y = self.locy[2]

    def weaponfound(self):
        if self.rect.colliderect(player.hitbox):
            print("YOU FOUND AN AXE")
            player.weapon = player.axe
            self.rect.x = -100
            self.rect.y = -100


class Castle:
    def __init__(self):
        self.castleimg = pygame.image.load("castle.gif")
        self.castlerect = pygame.Rect(555, 160, 32, 32)
        self.castlerect2 = pygame.Rect(155, 465, 32, 32)

    def collision(self):
        if self.castlerect.colliderect(player.hitbox):
            gamestate.shop1()
        if self.castlerect2.colliderect(player.hitbox):
            print("RAUS HIER")


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.camera_offset = pygame.math.Vector2()

        self.ground_surf = pygame.image.load("background.gif").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def custom_draw(self):
        ground_offset = self.ground_rect.topleft + self.camera_offset

        self.display_surface.blit(self.ground_surf, self.camera_offset)




class Enemys:
    def __init__(self):
        self.enemys = pygame.image.load("goblin.gif")
        self.enemysdead = pygame.image.load("goblin_dead.gif")
        self.currentstate = self.enemys
        self.life = 5
        self.enemyx = [100, 200, 300, 400, 500, 600, 700]
        self.enemyy = [100, 200, 300, 400, 500]
        self.enemyrect = pygame.Rect(self.enemyx[2], self.enemyy[3], 32, 32)

    def death(self):
        if self.life < 0:
            self.life = 0
            print("IT'S DEAD!! +250XP")
            player.xp += 250
            player.score += 90
            self.currentstate = self.enemysdead
            enemys.enemyrect.x = -100
            enemys.enemyrect.y = -100


class Mouse:
    def __init__(self):
        self.posx, self.posy = pygame.mouse.get_pos()
        self.mouserect = pygame.Rect(self.posx, self.posy, 2, 2)


class Hole:
    def __init__(self):
        self.holerect = pygame.Rect(coordinates_x[4], coordinates_y[1], 15, 15)

    def falling(self):
        if hole.holerect.colliderect(player.hitbox):
            player.life += -9
            print("YOU HAVE FALLEN INTO A HOLE!")
            player.playerx = 400
            player.playery = 300


class Text:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.lifetext = self.font.render(str(player.life), True, white, red)
        self.lifetextrect = self.lifetext.get_rect()
        self.lifetextrect.x = 80
        self.lifetextrect.y = 0
        self.lifelife = self.font.render("LIFE:", True, white, red)
        self.lifeliferect = self.lifelife.get_rect()
        self.lifeliferect.x = 0
        self.lifeliferect.y = 0

        self.manatext = self.font.render(str(player.mana), True, white, blue)
        self.manatextrect = self.manatext.get_rect()
        self.manatextrect.x = 360
        self.manatextrect.y = 0
        self.manamana = self.font.render("MANA:", True, white, blue)
        self.manamanarect = self.manamana.get_rect()
        self.manamanarect.x = 250
        self.manamanarect.y = 0

        self.lvltext = self.font.render(str(player.lvl), True, white, yellow)
        self.lvltextrect = self.lvltext.get_rect()
        self.lvltextrect.x = 662
        self.lvltextrect.y = 0
        self.lvllvl = self.font.render("LEVEL:", True, white, yellow)
        self.lvllvlrect = self.lvllvl.get_rect()
        self.lvllvlrect.x = 550
        self.lvllvlrect.y = 0


class Rock:
    def __init__(self):
        self.rock = pygame.image.load("rock.gif")
        self.rock_destroyed = pygame.image.load("rock_destroyed.gif")
        self.rock_current_state1 = self.rock
        self.rockx = [0, 100, 200, 300, 400, 500, 600, 700]
        self.rocky = [0, 100, 200, 300, 400, 500]
        self.rockrect = pygame.Rect(self.rockx[3], self.rocky[2], 32, 32)
        self.rockrect2 = pygame.Rect(self.rockx[5], self.rocky[4], 32, 32)
        self.rockrect3 = pygame.Rect(self.rockx[7], self.rocky[3], 32, 32)

    def currentstate(self):
        pass


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

    def movement(self, playerX_change, playerY_change):
        self.playerx += playerX_change
        self.playery += playerY_change

    def gameover(self):
        if player.life <= 0:
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


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("ADVENTURE QUEST")
        self.shop = pygame.image.load("shop1.png")
        self.explosionspell = pygame.image.load("explosion.gif")
        self.background = pygame.image.load("background.gif")
        self.title = pygame.image.load("title.png")
        self.timesnrfinaltry = 10
        self.timesnrfinaltry2 = 10
        self.timesnrfinaltry3 = 10
        self.hole = pygame.image.load("hole.gif")
        self.fps = 60
        self.color = 0, 0, 0

    def run(self):
        while running:
            self.screen.fill((self.color))
            pygame.draw.rect(self.screen, white, mouse.mouserect)
            pygame.draw.rect(self.screen, (perfectgreen), player.hitbox)
            pygame.draw.rect(self.screen, (perfectgreen), hole.holerect)
            pygame.draw.rect(self.screen, (perfectgreen), rock.rockrect)
            pygame.draw.rect(self.screen, (perfectgreen), castle.castlerect)
            pygame.draw.rect(self.screen, (perfectgreen), rock.rockrect2)
            pygame.draw.rect(self.screen, (perfectgreen), rock.rockrect3)
            pygame.draw.rect(self.screen, (perfectgreen), enemys.enemyrect)
            pygame.draw.rect(self.screen, (perfectgreen), castle.castlerect2)

            self.screen.blit(self.background, (coordinates_x[0], coordinates_y[0]))

            self.screen.blit(rock.rock_current_state1, (rock.rockx[3], rock.rocky[2]))
            self.screen.blit(rock.rock, (rock.rockx[5], rock.rocky[4]))
            self.screen.blit(rock.rock, (rock.rockx[7], rock.rocky[3]))

            self.screen.blit(self.hole, (coordinates_x[4], coordinates_y[1]))

            self.screen.blit(enemys.currentstate, (enemys.enemyx[2], enemys.enemyy[3]))

            self.screen.blit(castle.castleimg, (coordinates_x[5], coordinates_y[1]))
            self.screen.blit(castle.castleimg, (coordinates_x[1], coordinates_y[4]))

            self.screen.blit(bush.image, (bush.locx[2], bush.locy[2]))
            self.screen.blit(bush.image, (bush.locx[4], bush.locy[4]))
            self.screen.blit(bush.image, (bush.locx[6], bush.locy[1]))
            self.screen.blit(bush.image, (bush.locx[0], bush.locy[4]))
            self.screen.blit(bush.image, (bush.locx[3], bush.locy[5]))
            self.screen.blit(bush.image, (bush.locx[0], bush.locy[0]))

            self.screen.blit(player.currentchar, (player.playerx, player.playery))

            self.screen.blit(text.lifelife, text.lifeliferect)
            self.screen.blit(text.lifetext, text.lifetextrect)
            self.screen.blit(text.manatext, text.manatextrect)
            self.screen.blit(text.manamana, text.manamanarect)
            self.screen.blit(text.lvltext, text.lvltextrect)
            self.screen.blit(text.lvllvl, text.lvllvlrect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        print("EXP:", player.xp, "SCORE:", player.score, "ORE:", player.ore, "LIFEPOTIONS:", player.potions)
                        print("WEAPON DAMAGE:", player.weapon)
                    if event.key == pygame.K_1 and player.mana > 0:
                        self.screen.blit(self.explosionspell, (mouse.posx, mouse.posy))
                        self.explosionspellhitbox = pygame.Rect(mouse.posx, mouse.posy, 32, 32)
                        pygame.draw.rect(self.screen, (perfectgreen), self.explosionspellhitbox)
                        player.mana += -7
                    if event.key == pygame.K_q and player.potions > 0:
                        player.potions += -1
                        print("POTION DRANK ", player.potions, " LEFT")
                        player.life = player.maxlife
                if event.type == pygame.MOUSEBUTTONDOWN and enemys.enemyrect.colliderect(mouse.mouserect) and player.hitbox.colliderect(enemys.enemyrect):
                    enemys.life += -player.weapon
                    print(enemys.life)
                if enemys.enemyrect.colliderect(player.hitbox):
                    player.life += -1
                if event.type == pygame.MOUSEBUTTONDOWN and rock.rockrect.colliderect(mouse.mouserect) and player.hitbox.colliderect(rock.rockrect):
                    print("MINING")
                    self.timesnrfinaltry += -1
                    player.score += 5
                    player.ore += 1
                    player.xp += 100
                    print(self.timesnrfinaltry)
                if self.timesnrfinaltry < 0:
                    print("THIS ORE IS EMPTY")
                    self.timesnrfinaltry = 0
                    player.ore += -1
                    player.score += -5
                    player.xp += -100
                if self.timesnrfinaltry == 0:
                    rock.rock_current_state1 = rock.rock_destroyed
                if event.type == pygame.MOUSEBUTTONDOWN and rock.rockrect2.colliderect(mouse.mouserect) and player.hitbox.colliderect(rock.rockrect2):
                    print("MINING")
                    self.timesnrfinaltry2 += -1
                    player.score += 5
                    player.ore += 1
                    player.xp += 100
                    print(self.timesnrfinaltry2)
                if self.timesnrfinaltry2 < 0:
                    print("THIS ORE IS EMPTY")
                    self.timesnrfinaltry2 = 0
                    player.ore += -1
                    player.score += -5
                    player.xp += -100
                if event.type == pygame.MOUSEBUTTONDOWN and rock.rockrect3.colliderect(mouse.mouserect) and player.hitbox.colliderect(rock.rockrect3):
                    print("MINING")
                    self.timesnrfinaltry3 += -1
                    player.score += 5
                    player.ore += 1
                    player.xp += 100
                    print(self.timesnrfinaltry3)
                if self.timesnrfinaltry3 < 0:
                    print("THIS ORE IS EMPTY")
                    self.timesnrfinaltry3 = 0
                    player.ore += -1
                    player.score += -5
                    player.xp += -100

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                player.movement(0, -1.5)
                player.currentchar = player.character

            if keys[pygame.K_a]:
                player.movement(-1.5, 0)
                player.currentchar = player.characterleft

            if keys[pygame.K_s]:
                player.movement(0, 1.5)
                player.currentchar = player.characterdown

            if keys[pygame.K_d]:
                player.movement(1.5, 0)
                player.currentchar = player.characterright

            hole.falling()
            player.gameover()
            enemys.death()
            castle.collision()
            rock.__init__()
            text.__init__()
            camera_group.__init__()
            mouse.__init__()
            bush.weaponfound()
            player.level2up()
            player.nomana()
            player.hitbox.x = player.playerx
            player.hitbox.y = player.playery

            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(self.fps)


game = Game()
hole = Hole()
rock = Rock()
player = Player()
text = Text()
mouse = Mouse()
enemys = Enemys()
castle = Castle()
bush = Bush()
camera_group = Camera()
gamestate = Gamestate()
buymenu = Buymenu()


camera_group.draw(game.screen)
bush_group = pygame.sprite.Group()
bush_group.add(bush)
bush_group.draw(game.screen)
player.gameover()
player.level2up()
hole.falling()
enemys.death()
castle.collision()

gamestate.statemanager()




import pygame
from player import player
from mouse import Mouse
from enemys import Enemys
from playerinfo import Playerinfo
from buymenu import Buymenu
from setup import setup
from hole import Hole
from ladder import ladder
from bush import Bush
from bush import Bush2
from tkinter import *

coordinates_x = [0, 100, 200, 300, 400, 500, 600, 700]
coordinates_y = [0, 100, 200, 300, 400, 500]
running = True

perfectgreen = 100, 255, 100
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


def load_many_enemies_from_file(file):
    my_dictionary = {}

    for enemy in file:
        name = enemy['goblin']
        health = enemy['5']
        alive_image = pygame.image.load(f"goblin.gif")
        dead_image = pygame.image.load(f"goblin_dead.gif")
        my_dictionary.update({name: {'health': health, 'alive_image': alive_image, 'dead_image': dead_image}})

    return my_dictionary


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
            setup.screen.blit(game.title, (0, 0))
            pygame.display.update()

    def main_game(self):
        game.run()

    def shop(self):
        player.playerx = 400
        player.playery = 300
        buymenu.buying()
        pygame.display.update()

    def cave(self):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        playerinfo.playerinfo()
                    if event.key == pygame.K_q and player.potions > 0:
                        player.potions += -1
                        print("POTION DRANK ", player.potions, " LEFT")
                        player.life = player.maxlife

                if event.type == pygame.MOUSEBUTTONDOWN and enemys3.enemyrect2.colliderect(mouse.mouserect) and player.hitbox.colliderect(enemys3.enemyrect2):
                    enemys.life += -player.weapon
                    print(enemys.life)

            pygame.draw.rect(setup.screen, (220, 100, 100), player.hitbox)
            pygame.draw.rect(setup.screen, white, mouse.mouserect)
            pygame.draw.rect(setup.screen, (220, 100, 100), ladder.rect)
            enemys3.drawrect((220, 100, 100))

            setup.screen.blit(game.cave, (0, 0))

            setup.screen.blit(player.currentchar, (player.playerx, player.playery))

            setup.screen.blit(text.lifelife, text.lifeliferect)
            setup.screen.blit(text.lifetext, text.lifetextrect)
            setup.screen.blit(text.manatext, text.manatextrect)
            setup.screen.blit(text.manamana, text.manamanarect)
            setup.screen.blit(text.lvltext, text.lvltextrect)
            setup.screen.blit(text.lvllvl, text.lvllvlrect)

            text.__init__()

            enemys3.draw()
            enemys3.makedamage()
            enemys3.getdamage()
            enemys3.death()
            intothecave.collision2()
            mouse.__init__()

            player.hitbox.x = player.playerx
            player.hitbox.y = player.playery

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

            pygame.display.update()
            pygame.display.flip()
            clock = pygame.time.Clock()
            clock.tick(game.fps)


class Intothecave:
    def collision(self):
        if hole.holerect.colliderect(player.hitbox):
            gamestate.cave()
    def collision2(self):
        if ladder.rect.colliderect(player.hitbox):
            gamestate.main_game()


class Castle:
    def __init__(self):
        self.castleimg = pygame.image.load("castle.gif")
        self.castlerect = pygame.Rect(555, 160, 32, 32)
        self.castlerect2 = pygame.Rect(155, 465, 32, 32)

    def collision(self):
        if self.castlerect.colliderect(player.hitbox):
            gamestate.shop()
        if self.castlerect2.colliderect(player.hitbox):
            print("RAUS HIER")


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
        self.rock_current_state2 = self.rock
        self.rock_current_state3 = self.rock
        self.rockx = [0, 100, 200, 300, 400, 500, 600, 700]
        self.rocky = [0, 100, 200, 300, 400, 500]
        self.rockrect = pygame.Rect(self.rockx[3], self.rocky[2], 32, 32)
        self.rockrect2 = pygame.Rect(self.rockx[5], self.rocky[4], 32, 32)
        self.rockrect3 = pygame.Rect(self.rockx[7], self.rocky[3], 32, 32)

    def nothingleft(self):
        if game.timesnrfinaltry == 0:
            rock.rock_current_state1 = self.rock_destroyed
        if game.timesnrfinaltry2 == 0:
            rock.rock_current_state2 = self.rock_destroyed
        if game.timesnrfinaltry3 == 0:
            rock.rock_current_state3 = self.rock_destroyed


class Game:
    def __init__(self):
        self.explosionspell = pygame.image.load("explosion.gif")
        self.background = pygame.image.load("background.gif")
        self.title = pygame.image.load("title.png")
        self.cave = pygame.image.load("cave.gif")
        self.timesnrfinaltry = 10
        self.timesnrfinaltry2 = 10
        self.timesnrfinaltry3 = 10
        self.hole = pygame.image.load("hole.gif")
        self.fps = 60
        self.color = 0, 0, 0

    def run(self):
        while running:
            setup.screen.fill((self.color))
            pygame.draw.rect(setup.screen, white, mouse.mouserect)
            pygame.draw.rect(setup.screen, (perfectgreen), player.hitbox)
            pygame.draw.rect(setup.screen, (perfectgreen), hole.holerect)
            enemys.drawrect((100, 255, 100))
            enemys2.drawrect((100, 255, 100))
            pygame.draw.rect(setup.screen, (perfectgreen), rock.rockrect)
            pygame.draw.rect(setup.screen, (perfectgreen), castle.castlerect)
            pygame.draw.rect(setup.screen, (perfectgreen), rock.rockrect2)
            pygame.draw.rect(setup.screen, (perfectgreen), rock.rockrect3)
            pygame.draw.rect(setup.screen, (perfectgreen), castle.castlerect2)

            setup.screen.blit(self.background, (coordinates_x[0], coordinates_y[0]))

            setup.screen.blit(rock.rock_current_state1, (rock.rockx[3], rock.rocky[2]))
            setup.screen.blit(rock.rock_current_state2, (rock.rockx[5], rock.rocky[4]))
            setup.screen.blit(rock.rock_current_state3, (rock.rockx[7], rock.rocky[3]))

            setup.screen.blit(self.hole, (coordinates_x[4], coordinates_y[1]))

            setup.screen.blit(castle.castleimg, (coordinates_x[5], coordinates_y[1]))
            setup.screen.blit(castle.castleimg, (coordinates_x[1], coordinates_y[4]))

            setup.screen.blit(bush.image, (bush.locx, bush.locy))
            setup.screen.blit(bush.image, (bush.locx, bush.locy))
            setup.screen.blit(bush.image, (bush.locx, bush.locy))
            setup.screen.blit(bush.image, (bush.locx, bush.locy))
            setup.screen.blit(bush.image, (bush.locx, bush.locy))
            setup.screen.blit(bush.image, (bush.locx, bush.locy))

            setup.screen.blit(player.currentchar, (player.playerx, player.playery))

            setup.screen.blit(text.lifelife, text.lifeliferect)
            setup.screen.blit(text.lifetext, text.lifetextrect)
            setup.screen.blit(text.manatext, text.manatextrect)
            setup.screen.blit(text.manamana, text.manamanarect)
            setup.screen.blit(text.lvltext, text.lvltextrect)
            setup.screen.blit(text.lvllvl, text.lvllvlrect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        playerinfo.playerinfo()
                    if event.key == pygame.K_1 and player.mana > 0:
                        setup.screen.blit(self.explosionspell, (mouse.posx, mouse.posy))
                        player.mana += -7
                    if event.key == pygame.K_q and player.potions > 0:
                        player.potions += -1
                        print("POTION DRANK ", player.potions, " LEFT")
                        player.life = player.maxlife
                    if event.type == pygame.MOUSEBUTTONDOWN and enemys.enemyrect2.colliderect(mouse.mouserect) and player.hitbox.colliderect(enemys.enemyrect2):
                        enemys.life += -player.weapon
                        print(enemys.life)
                if event.type == pygame.MOUSEBUTTONDOWN and enemys.enemyrect2.colliderect(mouse.mouserect) and player.hitbox.colliderect(enemys.enemyrect2):
                    enemys.life += -player.weapon
                    print(enemys.life)
                if event.type == pygame.MOUSEBUTTONDOWN and enemys2.enemyrect2.colliderect(mouse.mouserect) and player.hitbox.colliderect(enemys2.enemyrect2):
                    enemys.life += -player.weapon
                    print(enemys.life)
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

            bush.__init__(100, 100)
            bush.weaponfound()
            bush2.__init__(250, 200)
            bush3.__init__(350, 450)
            bush4.__init__(650, 150)

            enemys.draw()
            enemys.getdamage()
            enemys.makedamage()
            enemys.death()

            enemys2.draw()
            enemys2.getdamage()
            enemys2.makedamage()
            enemys2.death()

            castle.collision()
            rock.__init__()
            text.__init__()
            mouse.__init__()

            intothecave.collision()

            rock.nothingleft()
            player.level2up()
            player.nomana()
            player.hitbox.x = player.playerx
            player.hitbox.y = player.playery

            pygame.display.update()

            clock = pygame.time.Clock()
            clock.tick(self.fps)


game = Game()
rock = Rock()
text = Text()
mouse = Mouse()
hole = Hole()
enemys = Enemys(300, 300)
enemys2 = Enemys(450, 550)
enemys3 = Enemys(200, 400)
castle = Castle()
bush = Bush(0, 0)
bush2 = Bush2(0, 0)
bush3 = Bush2(0, 0)
bush4 = Bush2(0, 0)
gamestate = Gamestate()
playerinfo = Playerinfo()
buymenu = Buymenu()
intothecave = Intothecave()

bush.weaponfound()
bush_group = pygame.sprite.Group()
bush_group.add(bush)
bush_group.draw(setup.screen)
player.gameover()
player.level2up()
hole.falling()
castle.collision()

gamestate.statemanager()

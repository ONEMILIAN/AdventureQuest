from tkinter import *
from player import player


class Playerinfo:

    def playerinfo(self):
        fenster = Tk()
        character = Label(text="CHARACTER")
        character.pack()
        level = Label(text="LEVEL:")
        level.pack()
        level2 = Label(text=player.lvl)
        level2.pack()
        exp = Label(text="EXPERIENCE:")
        exp.pack()
        exp2 = Label(text=player.xp)
        exp2.pack()
        score = Label(text="SCORE:")
        score.pack()
        score2 = Label(text=player.score)
        score2.pack()
        ore = Label(text="ORE:")
        ore.pack()
        ore2 = Label(text=player.ore)
        ore2.pack()
        potions = Label(text="POTIONS:")
        potions.pack()
        potions2 = Label(text=player.potions)
        potions2.pack()
        damage = Label(text="DAMAGE:")
        damage.pack()
        damage2 = Label(text=player.weapon)
        damage2.pack()
        armor = Label(text="ARMOR:")
        armor.pack()
        armor2 = Label(text=player.armor)
        armor2.pack()
        shield = Label(text="SHIELD PROTECTION:")
        shield.pack()
        shield2 = Label(text=player.currentshield)
        shield2.pack()

        fenster.mainloop()

from tkinter import *
from player import player


class Buyshield(Button):

    def buyshield(self):
        if player.ore > 19:
            player.currentshield = player.shield
            player.ore += -20
            print("THANK YOU VERY MUCH")
        else:
            print("NOT ENOUGH ORE")


class Buybtrswrd(Button):

    def buybtrswrd(self):
        if player.ore > 29:
            player.weapon = player.bettersword
            player.ore += -30
            print("THANK YOU VERY MUCH")
        else:
            print("NOT ENOUGH ORE")


class Buymenu:

    def buying(self):
        fenster = Tk()
        introtxt = Label(text="WHAT DO YOU WANT TO BUY?")
        introtxt.pack()
        btrswrd = Label(text="1. BETTER SWORD = 30 ORE")
        btrswrd.pack()
        btrswrdbuybtn = Buybtrswrd(text="BUY AND EQUIP BETTER SWORD")
        btrswrdbuybtn["command"] = btrswrdbuybtn.buybtrswrd
        btrswrdbuybtn.pack()
        shld = Label(text="2. SHIELD = 20 ORE")
        shld.pack()
        shldbuybtn = Buyshield(text="BUY AND EQUIP SHIELD")
        shldbuybtn["command"] = shldbuybtn.buyshield
        shldbuybtn.pack()
        verlassen = Button(text="EXIT", command=fenster.destroy)
        verlassen.pack()

        fenster.mainloop()

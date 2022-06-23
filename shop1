from tkinter import *
from druff import player


class Buybtrswrd(Button):
    def buybtrswrd(self):
        if player.ore > 29:
            player.weapon = player.bettersword
            player.ore += -30
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
        btrswrdbuybtn["command"] = btrswrdbuybtn.buybtrswrd()
        btrswrdbuybtn.pack()
        shld = Label(text="2. SHIELD = 20 ORE")
        shld.pack()
        shldbuybtn = Button(text="BUY AND EQUIP SHIELD")
        shldbuybtn.pack()
        verlassen = Button(text="EXIT", command=fenster.destroy)
        verlassen.pack()

        fenster.mainloop()


buymenu = Buymenu()

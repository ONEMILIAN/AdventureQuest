from tkinter import *
import subprocess


class MyButton2(Button):
    def aktion2(self):
        subprocess.call("druff.py", shell=True)


class MyButton3(Button):
    def aktion3(self):
        subprocess.call("helpme.txt", shell=True)


fenster = Tk()
fenster.geometry("300x150")
label = Label(text="HAUPTMENÜ")
label.place(x=40, y=0)
label2 = Label(text="BITTE WÄHLEN:")
label2.place(x=80, y=60)
button = MyButton2(fenster, text="SPIELEN")
button["command"] = button.aktion2
button.place(x=50, y=100)
button2 = Button(fenster, text="VERLASSEN", command=fenster.destroy)
button2.place(x=150, y=100)
button3 = MyButton3(fenster, text="?")
button3["command"] = button3.aktion3
button3.place(x=120, y=100)
fenster.title("ADVENTURE QUEST")
fenster.mainloop()

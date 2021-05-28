import os
from time import sleep
from tkinter import *
import pygame
root = Tk()
path = 'songs'
song_list = os.listdir(path)

pygame.mixer.init()  # initialise the pygame
root.geometry("600x400")

title = Label(root, text="Music Player", bd=9, relief=GROOVE,
            font=("times new roman", 50, "bold"), bg="white", fg="green")
title.pack(side=TOP, fill=X)


def stop():
    pygame.mixer.music.stop()

listbox = Listbox(root)
for i in range(len(song_list)):
    listbox.insert(i+1, song_list[i][:-4])
unpicked = ['0']
def CurSelet(event):
    stop()
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    global unpicked
    with open(f"songs/{song_list[selection[0]]}", 'r') as lyric:
        lyric_print = lyric.read()
    if picked != unpicked[-1]:
        lyricer.configure(text=picked)
        left.configure(text=lyric_print)
        def play():
            print("played")
            pygame.mixer.music.load(f"mp3/{picked}.mp3")
            pygame.mixer.music.play(loops=0)
            for i in lyric_print.split('\n'):
                print(i)
                sleep(3)
        b.configure(command=play)
    unpicked.append(picked)
listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.pack(side=LEFT, fill=Y)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
b = Button(root,text="Play")
b.pack(side=BOTTOM)
canvas = Canvas(root,yscrollcommand = scrollbar.set)
canvas.pack(fill='both')
scrollbar.config(command = canvas.yview )
lyricer = LabelFrame(canvas, labelanchor='n', text="")
lyricer.pack(fill="both", expand="yes")
left = Label(lyricer, text='')
left.pack()
root.mainloop()

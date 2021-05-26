import os
from tkinter import *
import pygame
root = Tk()
path = 'songs'
song_list = os.listdir(path)

pygame.mixer.init()  # initialise the pygame
def play():
    pygame.mixer.music.load("mp3/kya.mp3")
    pygame.mixer.music.play(loops=0)
root.geometry("600x400")

title = Label(root, text="Music Player", bd=9, relief=GROOVE,
            font=("times new roman", 50, "bold"), bg="white", fg="green")
title.pack(side=TOP, fill=X)

listbox = Listbox(root)
for i in range(len(song_list)):
    listbox.insert(i+1, song_list[i][:-4])
unpicked = ['0']
def CurSelet(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    global unpicked
    with open(f"songs/{song_list[selection[0]]}", 'r') as lyric:
        lyric_print = lyric.read()
    if picked != unpicked[-1]:
        lyricer.configure(text=picked)
        left.configure(text=lyric_print)
    unpicked.append(picked)
listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.pack(side=LEFT, fill=Y)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
canvas = Canvas(root,yscrollcommand = scrollbar.set)
canvas.pack(fill='both')
scrollbar.config(command = canvas.yview )
lyricer = LabelFrame(canvas, labelanchor='n', text="")
lyricer.pack(fill="both", expand="yes")
left = Label(lyricer, text='')
left.pack()
root.mainloop()

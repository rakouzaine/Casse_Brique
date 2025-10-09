# -*- coding: utf-8 -*-
"""
qui : Rayan Souni, Yassine Zair

quand : 09/10/2025

quoi : programmation du jeu casse brique sur TKinter

"""

from tkinter import * 

def on_begin():
    print("Le jeu commence…")

root = tk.Tk()
root.title("Jeu du casse-briques")
root.configure(bg="bisque")



begin_button = tk.Button(root, text="Begin", command=on_begin)
begin_button.pack(side=tk.LEFT, padx=5, pady=5)

canvas = Canvas(root , width = 800 , height = 400, bg = "black")

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()

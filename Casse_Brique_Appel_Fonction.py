# -*- coding: utf-8 -*-
"""
qui : Rayan Souni, Yassine Zair

quand : 09/10/2025

quoi : programmation du jeu casse brique sur TKinter

a faire : Rayan doit faire la page vie et destruction brique
          Yassine doit finir score avec destruction brique, faire page de jeu et de presentation 
"""

import tkinter as tk
import math
import random
from tkinter import Canvas, Frame, Label, LEFT, RIGHT

        


class Page_Presentation : 
    
class Page_Jeu : 
# root = tk.Tk()
# root.title("Jeu du casse-briques")
# root.configure(bg="bisque")

# # Canvas unique
# canvas = tk.Canvas(root, width=800, height=400, bg="white")
# canvas.pack(pady=10)

# # Instanciation de la plateforme
# paddle = MouvementPlateforme(canvas)

# begin_button = tk.Button(root, text="Begin", command=paddle.plateforme)
# begin_button.pack(side=tk.LEFT, padx=5, pady=5)

# quit_button = tk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(side=tk.LEFT, padx=5, pady=5)

# root.mainloop()

    
    
class Creation_Brique :

    def __init__(self, canvas: Canvas):
        self.canvas = canvas   
        self.bricks = [] 

    def Brique(self):
        # crée une brique et retourne son id
        
        n    = 10     # nombre de briques
        x0   = 40     # x de départ
        y0   = 50     # y de départ
        w    = 60     # largeur d'une brique
        h    = 20     # hauteur d'une brique
        gap  = 5    # espace entre deux briques
        color = "blue"  # couleur unique pour toutes les briques
        

        for j in range(5):  # 5 lignes
            for i in range(n):  # n colonnes
                x1 = x0 + i * (w + gap)
                y1 = y0 + j * (h + gap)
                x2 = x1 + w
                y2 = y1 + h
                brick_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                self.bricks.append({
                    "id": brick_id,
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2})
def brick_hit_at(self, x, y):
        """Supprime une brique si le point (x, y) entre en collision avec elle."""
        for brick in list(self.bricks):  # itérer sur une copie car on peut supprimer
            if brick["x1"] <= x <= brick["x2"] and brick["y1"] <= y <= brick["y2"]:
                self.canvas.delete(brick["id"])
                self.bricks.remove(brick)
                return True
        return False
    
    
    
class Score:
    def __init__(self, root):
        # Utilisation de Frame/Label tels qu'ils étaient dans ton fichier
        self.frame = Frame(root)
        self.label_score = Label(self.frame, text="Score : 0")
        self.label_vies = Label(self.frame, text="Vies : 3")
        self.label_vies.pack(side=LEFT, padx=10)
        self.label_score.pack(side=RIGHT, padx=10)
        
    def pack(self):
        self.frame.pack()

    def modifier(self, score=None, vies=None):
        if score is not None:
            self.label_score.config(text=f"Score : {score}")
        if vies is not None:
            self.label_vies.config(text=f"Vies : {vies}")
            
            
    
class Creation_Balle:
    def __init__(self, canvas, x, y, rayon=8, vitesse=6):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rayon = rayon
        self.vitesse = vitesse

        # direction initiale vers le haut (valeur vy négative)
        angle = random.uniform(-math.pi/4, math.pi/4)
        self.vx = vitesse * math.sin(angle)
        self.vy = -abs(vitesse * math.cos(angle))

        # Dessiner la balle
        self.id = canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill="red")

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.canvas.coords(self.id, self.x-self.rayon, self.y-self.rayon, self.x+self.rayon, self.y+self.rayon)


class MouvementPlateforme:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.vx = 0          # vitesse horizontale
        self.speed = 10      # pixels par tick
        
    def plateforme(self):
        self.plat = self.canvas.create_rectangle(
            240, 372, 360, 388, fill="#333"
            )
        return self.plat

    def _left(self):  self.vx = -self.speed
    def _right(self, _): self.vx =  self.speed
    def _stop(self, _):  self.vx = 0

    def _tick(self):
        if self.vx != 0:
            x1, y1, x2, y2 = self.canvas.coords(self.plat)
            W = int(self.canvas.cget("width"))


            self.canvas.move(self.plat, dx, 0)  # seulement sur l’axe X

class Deplacement_Clavier_plateforme : 
    
    def __init__(self, root: tk.Tk, mp: MouvementPlateforme, fps: int = 60):
        self.root = root
        self.mp = mp

        #  Surcharger la vitesse si on continue a appuyer
        if speed is not None:
            self.mp.speed = speed
            

        # Largeur du canvas pour le clipping aux bords
        self.W = int(self.mp.canvas.cget("width"))

        # Bind clavier (flèches)
        root.bind("<Left>",  self._left)
        root.bind("<Right>", self._right)
        root.bind("<KeyRelease-Left>",  self._stop)
        root.bind("<KeyRelease-Right>", self._stop)

        # Boucle d'update
        self.period_ms = max(1, int(1000 / fps))
        self._tick()

    def _left(self, _evt):   self.mp.vx = -self.mp.speed
    def _right(self, _evt):  self.mp.vx =  self.mp.speed
    def _stop(self, _evt):   self.mp.vx = 0

    def _tick(self):
        # Si on a une vitesse horizontale, on essaie de bouger
        if self.mp.vx != 0 :
            x1, y1, x2, y2 = self.mp.canvas.coords(self.mp.plat)
            dx = self.mp.vx

            # arrêt aux bords
            if x1 + dx < 0:
                dx = -x1
            elif x2 + dx > self.W:
                dx = self.W - x2

            if dx != 0:
                self.mp.canvas.move(self.mp.plat, dx, 0)  # déplacement uniquement sur X

        self.mp.canvas.after(self.period_ms, self._tick)

    


    



def on_begin():




def game_loop():





















root = tk.Tk()
root.title("Jeu du casse-briques")
root.configure(bg="bisque")



begin_button = tk.Button(root, text="Begin", command=on_begin)
begin_button.pack(side=tk.LEFT, padx=5, pady=5)

canvas = Canvas(root , width = 800 , height = 400, bg = "black")

"""affichage score """
text

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()

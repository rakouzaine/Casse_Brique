# -*- coding: utf-8 -*-
"""
qui : Rayan Souni, Yassine Zair

quand : 09/10/2025

quoi : programmation du jeu casse brique sur TKinter

a faire : Rayan doit faire la page vie et destruction brique
          Yassine doit finir score avec destruction brique, faire page de jeu et de presentation 
"""

from tkinter import * 


        


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

    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas

    def Brique(self):
        # crée une brique et retourne son id
        
        n    = 10     # nombre de briques
        x0   = 40     # x de départ
        y0   = 50     # y de départ
        w    = 60     # largeur d'une brique
        h    = 20     # hauteur d'une brique
        gap  = 5    # espace entre deux briques
        

        for j in range(5):  # 5 lignes
            y1 = y0 + j * 25
            for i in range(n):  # n colonnes
                x1 = x0 + i * (w + gap)
                x2 = x1 + w
                y2 = y1 + h
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="")
    
class rebond_cadre : 
    # faire rebondir la balle sur le cadre du jeu     
    
class Destruction_Brique :   
    # supprimer la brique
    # Supperimer brique = True
    
    
    
class Score : 
    def __init__(self , brique):
        self.__brique = brique
        self.__point = []
    def compte_point(self):
        if brique ==     :
            
            
    
class Creation_Balle : 
class Mouvement_Balle :
    # mouvement physique dans l'espace 
    # rebond de la balle sur la brique , prendre True 
   

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

class vie :
    # compter le nb de vie 
    # reinitialiser le jeu ( remtettre la page _Jeu)
    
class Fin_Jeu : 
    
    


    

























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

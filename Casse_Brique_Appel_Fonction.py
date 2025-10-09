# -*- coding: utf-8 -*-
"""
qui : Rayan Souni, Yassine Zair

quand : 09/10/2025

quoi : programmation du jeu casse brique sur TKinter

"""

from tkinter import * 


        


class Page_Presentation : 
    
class Page_Jeu : 
    
    
class Creation_Brique :
    # creer la forme et la couleur de la brique
    # les aligner une par une en haut de la page jeu
    
    
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
   
class Mouvement_plateforme :  
class Deplacement_Clavier_plateforme : 
    
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

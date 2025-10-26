class CreationBrique:
    def __init__(self, canvas: Canvas):
        """Initialise le gestionnaire de briques."""
        self.canvas = canvas
        self.briques = []  # Liste qui stocke les briques (id + coordonnées)

    def creer_briques(self):
        """Crée et affiche les briques sur le canvas."""
        n = 10       # nombre de briques par ligne
        rows = 5     # nombre de lignes
        x0 = 40      # x de départ
        y0 = 50      # y de départ
        w = 60       # largeur d'une brique
        h = 20       # hauteur d'une brique
        gap = 5      # espace entre deux briques

        

        for j in range(rows):
            for i in range(n):

                couleur = f'#{random.randrange(256**3):06x}'# couleur unique pour toutes les briques
                x1 = x0 + i * (w + gap)
                y1 = y0 + j * (h + gap)
                x2 = x1 + w
                y2 = y1 + h

                brique_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur , outline="")
                self.briques.append({
                    "id": brique_id,
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                })

    def supprimer_brique(self, x, y):
        """Supprime une brique si le point (x, y) entre en collision avec elle."""
        for brique in list(self.briques):  # itérer sur une copie car on peut supprimer
            if brique["x1"] <= x <= brique["x2"] and brique["y1"] <= y <= brique["y2"]:
                self.canvas.delete(brique["id"])
                self.briques.remove(brique)
                return True
        return False

class CreationBrique:
    def __init__(self, canvas: Canvas):
        """Initialise le gestionnaire de briques."""
        self.canvas = canvas
        self.bricks = []  # Liste qui stocke les briques (id + coordonnées)

    def create_brique(self):
        """Crée et affiche les briques sur le canvas."""
        # Efface l'état précédent si on relance
        for b in self.bricks:
            self.canvas.delete(b["id"])
        self.bricks.clear()

        n = 10       # nombre de briques par ligne
        rows = 5     # nombre de lignes
        x0 = 40      # x de départ
        y0 = 50      # y de départ
        w = 60       # largeur d'une brique
        h = 20       # hauteur d'une brique
        gap = 5      # espace entre deux briques

        for j in range(rows):
            for i in range(n):
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # couleur au hasard pour chaque brique
                x1 = x0 + i * (w + gap)
                y1 = y0 + j * (h + gap)
                x2 = x1 + w
                y2 = y1 + h

                brick_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                self.bricks.append({"id": brick_id, "x1": x1, "y1": y1, "x2": x2, "y2": y2})

    def brick_hit_at(self, x, y):
        """Supprime une brique si le point (x, y) entre en collision avec elle."""
        for brick in list(self.bricks):  # itérer sur une copie car on peut supprimer
            if brick["x1"] <= x <= brick["x2"] and brick["y1"] <= y <= brick["y2"]:
                self.canvas.delete(brick["id"])
                self.bricks.remove(brick)
                return True
        return False
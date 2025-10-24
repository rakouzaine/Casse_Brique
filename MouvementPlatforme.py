class MouvementPlateforme:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.vx = 0          # vitesse horizontale
        self.speed = 10      # pixels par tick
        self.plat = None     # id du rectangle de la plateforme (créé plus tard)
        
    def plateforme(self):
        # (re)crée la plateforme centrée en bas
        if self.plat is not None:
            self.canvas.delete(self.plat)
        W = int(self.canvas.cget("width"))
        y1, y2 = 372, 388
        w = 120
        x1 = (W - w) // 2
        x2 = x1 + w
        self.plat = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#333")
        return self.plat

    # méthodes non utilisées directement pour les bindings (contrôle via DeplacementClavierplateforme)
    def _left(self):
        self.vx = -self.speed

    def _right(self):
        self.vx = self.speed

    def _stop(self):
        self.vx = 0
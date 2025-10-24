class DeplacementClavierplateforme:
    def __init__(self, root: tk.Tk, mp: MouvementPlateforme, fps: int = 60):
        self.root = root
        self.mp = mp
        self.W = int(self.mp.canvas.cget("width"))

        # Bind clavier (flèches)
        root.bind("<Left>",  self._left)
        root.bind("<Right>", self._right)
        root.bind("<KeyRelease-Left>",  self._stop)
        root.bind("<KeyRelease-Right>", self._stop)

        # Boucle d'update
        self.period_ms = max(1, int(1000 / fps))
        self._tick()

    def _left(self, _evt):
        self.mp.vx = -self.mp.speed

    def _right(self, _evt):
        self.mp.vx = self.mp.speed

    def _stop(self, _evt):
        self.mp.vx = 0

    def _tick(self):
        # tant que la plateforme n'existe pas, on ne fait rien
        if getattr(self.mp, "plat", None) is None:
            self.mp.canvas.after(self.period_ms, self._tick)
            return

        # Si on a une vitesse horizontale, on essaie de bouger
        if self.mp.vx != 0:
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
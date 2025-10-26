class MouvementPlateforme:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.vx = 0          # vitesse horizontale
        self.speed = 10      # déplacement en pixels par actualisation
        
    def creer_plateforme(self):
        """Crée la plateforme sur la toile."""
        self.plat = self.canvas.create_rectangle(240, 372, 360, 388, fill="white")
        return self.plat

    # méthodes non utilisées directement pour les bindings (contrôle via Deplacement_Clavier_plateforme)
    def _left(self):
        """Déplace la plateforme vers la gauche."""
        self.vx = -self.speed

    def _right(self):
        """Déplace la plateforme vers la droite."""
        self.vx = self.speed

    def _stop(self):
        """Arrête le mouvement horizontal."""
        self.vx = 0
    # méthodes non utilisées directement pour les bindings (contrôle via DeplacementClavierplateforme)
    def _left(self):
        self.vx = -self.speed

    def _right(self):
        self.vx = self.speed

    def _stop(self):
        self.vx = 0
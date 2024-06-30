import pygame
import sys

class PageCredits:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.font = pygame.font.Font(None, 36)  # Police et taille de texte
        self.credits = [
            "Ahmed Khairi",
            "Alexis Pretti",
            "Nathan Rognon",
            "Edouard Stamboulian",
            "",
            "Langage utilisé: python",
            "Librairie utilisée: pygame"
        ]

    def afficher(self):
        # Effacer l'écran avec une photo
        background_image = pygame.image.load("assets/text/black-screen.jpg")
        self.fenetre.blit(background_image, (0, 0))

        # Calculer la position verticale pour centrer les crédits
        vertical_center = self.fenetre.get_height() // 2.6

        # Afficher chaque membre de l'équipe centré verticalement
        for index, credit in enumerate(self.credits):
            text_surface = self.font.render(credit, True, (255, 255, 255))  # Texte blanc
            text_rect = text_surface.get_rect(center=(self.fenetre.get_width() // 2, vertical_center + index * 40))  # Espacement de 40 pixels
            self.fenetre.blit(text_surface, text_rect)
            #mouse normal
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        pygame.display.flip()  # Mettre à jour l'écran
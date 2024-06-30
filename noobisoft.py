import pygame
from pygame import mixer


class EcranNoobisoft:
    def __init__(self) -> None:
        self.image_noobisoft = pygame.image.load(
            "assets/text/noobisoft-presents.png")
        self.image_black = pygame.image.load("assets/text/black-screen.jpg")

        # Rectangle de l'image Noobisoft
        self.rect_noobisoft = self.image_noobisoft.get_rect()

        mixer.init()
        mixer.music.load("assets/sounds/death.wav")
        self.volume = 0.8
        mixer.music.set_volume(self.volume)

        # Rectangle de l'image noire (même taille que l'écran)
        self.rect_black = pygame.Rect(0, 0, 1024, 768)

        # Place le rectangle de l'image Noobisoft au centre de l'écran en utilisant les dimensions spécifiées
        self.rect_noobisoft.center = (1024 / 2, 768 / 2)

        # Gestion de l'opacité de l'image noire
        self.alpha_black = 0  # Valeur initiale de l'opacité
        self.alpha_black_step = 4  # Incrémentation/décrémentation de l'opacité

        # Variable pour suivre l'état de la transition
        self.transition_done = False  # Transition terminée

    def update(self):
        if not self.transition_done:
            # Augmente progressivement l'opacité de l'image noire pour le fondu
            if self.alpha_black < 255:
                self.alpha_black += self.alpha_black_step
                self.volume -= 0.01
                mixer.music.set_volume(self.volume)
            else:
                mixer.music.set_volume(0)
                self.alpha_black = 255
                self.transition_done = True

    def draw(self, screen):
        self.image_noobisoft.set_alpha(255)
        screen.blit(self.image_noobisoft, self.rect_noobisoft)

        # Affiche l'image noire avec l'opacité mise à jour (pour le fondu)
        self.image_black.set_alpha(self.alpha_black)
        screen.blit(self.image_black, self.rect_black)

        if self.alpha_black == 8:
            mixer.music.play()
            pygame.time.wait(2000)

import pygame
from pygame import mixer
from buttons import ButtonSprite
from credits import PageCredits


class EcranAccueil:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.start_game = False
        self.quit_game = False
        self.afficher_credits = False

        # mettre l'image du fond
        background_image = pygame.image.load(
            "assets/text/title-background.png")

        # les redimensionner
        self.background = pygame.transform.scale(
            background_image, (fenetre.get_width(), fenetre.get_height()))

        # Créez des instances de ButtonSprite pour les boutons "Jouer" et "Quitter"
        play_button_images = ["assets/text/play1.png",
                              "assets/text/play2.png", "assets/text/play3.png"]
        quit_button_images = ["assets/text/exit1.png",
                              "assets/text/exit2.png", "assets/text/exit3.png"]

        # mettre en place le bouton credits
        self.credits_font = pygame.font.Font(None, 36)
        self.credits_text = "Crédits"  # Le texte du bouton "Crédits"
        self.credits_color = (0, 0, 0)  # Couleur du texte

        # Chargez les images pour obtenir leurs dimensions
        play_image = pygame.image.load(play_button_images[0])
        quit_image = pygame.image.load(quit_button_images[0])

        # Calculez les positions pour centrer les boutons
        center_x = fenetre.get_width() // 2
        center_y = fenetre.get_height() // 1.7

        play_x = center_x - play_image.get_width() // 2
        play_y = center_y - play_image.get_height() // 2

        quit_x = center_x - quit_image.get_width() // 2
        quit_y = center_y + play_image.get_height() // 2 + 20

        # Créez des instances de ButtonSprite avec les nouvelles positions
        self.button_play = ButtonSprite(play_button_images, play_x, play_y)
        self.button_quit = ButtonSprite(quit_button_images, quit_x, quit_y)
        credits_button_width = 20
        credits_button_height = 10

        # Coordonnées du bouton "Crédits" en bas à droite
        self.credits_x = fenetre.get_width() - credits_button_width
        self.credits_y = fenetre.get_height() - credits_button_height

        self.page_credits = PageCredits(fenetre)

        # Groupe de sprites pour faciliter les mises à jour et le rendu
        self.button_sprites = pygame.sprite.Group(
            self.button_play, self.button_quit)

    def gerer_evenements(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.button_play.rect.collidepoint(event.pos) or self.button_quit.rect.collidepoint(event.pos):
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_play.rect.collidepoint(event.pos):
                    self.start_game = True
                elif self.button_quit.rect.collidepoint(event.pos):
                    self.quit_game = True
                elif self.credits_button_rect.collidepoint(event.pos):
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                    self.afficher_credits = True

    def afficher(self, dt):
        # Afficher le fond blanc
        self.fenetre.blit(self.background, (0, 0))

        # Mettre à jour et afficher les sprites des boutons
        self.button_sprites.update()
        self.button_sprites.draw(self.fenetre)

        # Afficher le bouton "Crédits"
        self.credits_button_surface = self.credits_font.render(
            self.credits_text, True, self.credits_color)
        self.credits_button_rect = self.credits_button_surface.get_rect(
            bottomright=(self.credits_x, self.credits_y))
        self.fenetre.blit(self.credits_button_surface,
                          self.credits_button_rect)

        if self.afficher_credits:
            self.page_credits.afficher()

    def start_disappearing_animation(self):
        self.disappearing = True

        pygame.display.flip()

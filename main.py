import pygame
import noobisoft
import accueil
import personnage
import histoire

# Initialisation de Pygame
pygame.init()

# Définir la résolution de la fenêtre
largeur, hauteur = 1024, 768
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Gravitron")

frameRate = 60
clock = pygame.time.Clock()

# Créez des instances d'écrans
ecran_noobisoft = noobisoft.EcranNoobisoft()
ecran_accueil = accueil.EcranAccueil(fenetre)

ecran_jeu = pygame.sprite.GroupSingle()
ecran_jeu.add(personnage.Personnage())
player = personnage.Personnage()

sky_surface = pygame.image.load('assets/earth/earth-background.png').convert()
ground_surface = pygame.image.load('assets/earth/earth-ground.png').convert()

# Définissez l'écran actif comme écran de présentation au début
ecran_actif = ecran_noobisoft

# Temps d'attente avant de passer à l'écran d'accueil (en ms)
temps_attente_noobisoft = 4000
temps_debut_noobisoft = pygame.time.get_ticks()

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if ecran_actif == ecran_noobisoft:
        ecran_noobisoft.update()
        ecran_noobisoft.draw(fenetre)

        # Vérifiez si le temps d'attente est écoulé
        temps_actuel = pygame.time.get_ticks()
        if temps_actuel - temps_debut_noobisoft >= temps_attente_noobisoft:
            ecran_actif = ecran_accueil

    dt = clock.tick(frameRate)

    if ecran_actif == ecran_accueil:
        ecran_accueil.gerer_evenements(events)
        ecran_accueil.afficher(dt / 1000)

        if ecran_accueil.start_game:
            histoire.introduction(fenetre)
            ecran_actif = ecran_jeu  # Passez à l'écran de jeu

        elif ecran_accueil.quit_game:
            running = False
        elif ecran_accueil.afficher_credits:
            ecran_accueil.afficher_credits = False
            ecran_actif = ecran_accueil.page_credits

    elif ecran_actif == ecran_jeu:
        ecran_jeu.update(dt, fenetre)
        ecran_jeu.draw(fenetre)
        # jeuhj.bonhommes()

    pygame.display.flip()

pygame.quit()

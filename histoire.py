import pygame


def introduction(fenetre):

    running_intro = True

    # Jouer le son d'introduction

    temps_attente = 10000
    temps_debut = pygame.time.get_ticks()

    while running_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_intro = False

        # Affichez un fond noir
        fenetre.fill((0, 0, 0))

                # Définir la taille de la fenêtre
        largeur, hauteur = 1024, 678

        # Charger une police
        font = pygame.font.Font("assets/font/Handjet-Medium.ttf", 36)

        # Texte avec des sauts de ligne
        phrase = """       2069, le nucléaire est la seule source d'énergie.

        Après une attaque de robots venus d'ailleurs,
        
        toutes les centrales de la planète ont explosées en chaîne :

        C'est l'Apocalypse !

        Enfuyez-vous pour éviter une mort certaine !"""

        # Obtenir la taille totale du texte
        texte_surface = pygame.Surface((largeur, hauteur))
        y = 0

        for ligne in phrase.splitlines():
            texte = font.render(ligne, 1, (255, 255, 255))
            texte_rect = texte.get_rect(center=(largeur // 2, y + texte.get_height() // 2))
            texte_surface.blit(texte, texte_rect)
            y += texte.get_height()

        # Centrer le texte dans la fenêtre
        texte_rect = texte_surface.get_rect(center=(largeur // 2.08, hauteur // 1.3))

        # Afficher le texte centré
        fenetre.blit(texte_surface, texte_rect)


        pygame.display.flip()

        # Attendez que le son d'introduction se termine
        temps_actuel = pygame.time.get_ticks()
        if temps_actuel - temps_debut >= temps_attente:
            running_intro = False

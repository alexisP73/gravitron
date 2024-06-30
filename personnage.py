import pygame
import pygame.mixer
from pygame import mixer


class Personnage(pygame.sprite.Sprite):
    pygame.mixer.init()
    music = pygame.mixer.Sound('assets/sounds/apocalypse.mp3')
    music_started = False
    music_started2 = False
    music2 = pygame.mixer.Sound('assets/sounds/game-over.wav')
    music3 = pygame.mixer.Sound('assets/sounds/happy_ending.mp3')

    def __init__(self):
        super().__init__()
        self.blkimg = pygame.image.load(
            'assets/text/black-screen.jpg').convert_alpha()
        player_walk_1 = pygame.image.load(
            'assets/hero/hero-standing.png').convert_alpha()
        player_walk_2 = pygame.image.load(
            'assets/hero/hero-walk1.png').convert_alpha()
        player_walk_3 = pygame.image.load(
            'assets/hero/hero-walk1-5.png').convert_alpha()
        player_walk_4 = pygame.image.load(
            'assets/hero/hero-walk2.png').convert_alpha()
        player_walk_5 = pygame.image.load(
            'assets/hero/hero-walk2-5.png').convert_alpha()

        player_walk_1_flip = pygame.image.load(
            'assets/hero/hero-standing-reverse.png').convert_alpha()
        player_walk_2_flip = pygame.image.load(
            'assets/hero/hero-walk1-reverse.png').convert_alpha()
        player_walk_3_flip = pygame.image.load(
            'assets/hero/hero-walk1-5-reverse.png').convert_alpha()
        player_walk_4_flip = pygame.image.load(
            'assets/hero/hero-walk2-reverse.png').convert_alpha()
        player_walk_5_flip = pygame.image.load(
            'assets/hero/hero-walk2-5-reverse.png').convert_alpha()

        player_jump1 = pygame.image.load(
            'assets/hero/hero-jump1.png').convert_alpha()
        player_jump2 = pygame.image.load(
            'assets/hero/hero-jump2.png').convert_alpha()

        player_jump1_flip = pygame.image.load(
            'assets/hero/hero-jump1-reverse.png').convert_alpha()
        player_jump2_flip = pygame.image.load(
            'assets/hero/hero-jump2-reverse.png').convert_alpha()

        self.player_walk_flip = [player_walk_1_flip, player_walk_3_flip, player_walk_2_flip,
                                 player_walk_3_flip, player_walk_1_flip, player_walk_5_flip, player_walk_4_flip, player_walk_5_flip]
        self.player_walk = [player_walk_1, player_walk_3, player_walk_2,
                            player_walk_3, player_walk_1, player_walk_5, player_walk_4, player_walk_5]
        self.player_jump = [player_jump1, player_jump2,
                            player_jump1_flip, player_jump2_flip]
        self.sky_surface = pygame.image.load(
            'assets/earth/earth-background.png').convert()
        self.ground_surface = pygame.image.load(
            'assets/earth/earth-ground.png').convert()

        self.vaisseau_back = pygame.image.load(
            'assets/spaceship/vaisseau-background-long.png').convert()
        self.vaisseausol = pygame.image.load(
            'assets/spaceship/vaisseau-ground-long.png').convert()
        self.obstaclePneu = pygame.image.load(
            'assets/earth/pneus-brulants.png')
        self.tonneau = pygame.image.load('assets/earth/debrit3.png')
        self.vaisseau = pygame.image.load('assets/earth/vaisseau-terre.png')
        self.personne = pygame.image.load('assets/earth/running-man1.png')

        self.sky = self.sky_surface.get_rect()
        self.vaisseauu = self.vaisseau_back.get_rect()

        self.sky.x = 0
        self.current_image_index = 0
        self.image = self.player_walk[self.current_image_index]
        # Définissez les coordonnées de départ ici
        self.gravity = 0
        self.groundHeight = 718
        self.stand = True
        self.persoStart = 128
        self.rect = self.image.get_rect(
            midbottom=(self.persoStart, self.groundHeight))
        self.last = None
        self.debutMap = 0
        self.finMap = 3000

        self.tonneauxPos = [1200, 1800, 2000,
                            2350, 2700, 2850, 3300, 3390]
        self.tonneaux = []
        for tonneauPos in self.tonneauxPos:
            self.tonneaux.append(round(tonneauPos - self.persoStart) / 1.5)
            self.tonneaux.append(
                round(tonneauPos + 75 - self.persoStart) / 1.5)
        self.decorsPos = [1800, 2850, 3550, 4100, 5200]

        self.monstre1 = pygame.image.load('assets/spaceship/monstre-vaisseau.png')

        self.monstrePos = [1200, 1800,
                            2350, 3750, 3300]
        self.monstrePos2 = [1600, 4000,
                            3500]
        self.monstre = []
        self.monstre2 = []
        for monstrePos in self.monstrePos:
            self.monstre.append(round(monstrePos - self.persoStart) / 1.5)
            self.monstre.append(
                round(monstrePos + 200 - self.persoStart) / 1.5)

        for monstrePos2 in self.monstrePos2:
            self.monstre2.append(round(monstrePos2 - self.persoStart) / 1.5)
            self.monstre2.append(
                round(monstrePos2 + 200 - self.persoStart) / 1.5)

        self.monstreAlien = pygame.image.load('assets/mars/monstre-mars2.png')

        self.monstreAlienPos = [2000, 3000,4500]
        self.monstreAlienPos2 = [2700, 4300]
        self.monstreAlienliste = []
        self.monstreAlienliste2 = []
        for monstreAlienPos in self.monstreAlienPos:
            self.monstreAlienliste.append(round(monstreAlienPos - self.persoStart) / 1.5)
            self.monstreAlienliste.append(
                round(monstreAlienPos + 100 - self.persoStart) / 1.5)

        for monstreAlienPos2 in self.monstreAlienPos2:
            self.monstreAlienliste2.append(round(monstreAlienPos2 - self.persoStart) / 1.5)
            self.monstreAlienliste2.append(
                round(monstreAlienPos2 + 100 - self.persoStart) / 1.5)

        self.marsBg = pygame.image.load('assets/mars/mars-background-grand.png')
        self.marsg = pygame.image.load('assets/mars/mars-ground-long.png')

        self.mars = self.marsBg.get_rect()

        

        

        self.walking_timer = 0

        self.player_speed = 250  # Vitesse de déplacement du joueur
        self.is_jumping = False

    def player_input(self, dt):
        keys = pygame.key.get_pressed()
        self.stand = True

        if keys[pygame.K_SPACE] and self.rect.bottom == self.groundHeight:
            self.stand = False
            self.is_jumping = True
            if self.sky.x < 2900:
                self.gravity = -20
            if self.sky.x >= 2900:
                self.gravity = -55

        # gauche
        if keys[pygame.K_q] and not keys[pygame.K_d]:
            if self.sky.x > self.debutMap and self.sky.x < 2900:
                self.stand = False
                self.sky.x -= (self.player_speed * dt)
                self.walking_timer += dt
                self.last = pygame.K_q
            if self.sky.x >= 2900 and self.vaisseauu.x < 3000:
                if self.vaisseauu.x > self.debutMap:
                    self.stand = False
                    self.vaisseauu.x -= (self.player_speed * dt)
                    self.walking_timer += dt
                    self.last = pygame.K_q
            if self.vaisseauu.x >= 2900:
                if self.mars.x > self.debutMap:
                    self.stand = False
                    self.mars.x -= (self.player_speed * dt)
                    self.walking_timer += dt
                    self.last = pygame.K_q


        # droite
        if keys[pygame.K_d] and not keys[pygame.K_q]:
            if self.sky.x < self.finMap and self.sky.x < 2900:
                self.stand = False
                self.sky.x += (self.player_speed * dt)
                self.walking_timer += dt
                self.last = pygame.K_d
            if self.sky.x >= 2900 and self.vaisseauu.x < 3000:
                if self.vaisseauu.x < self.finMap:
                    self.stand = False
                    self.vaisseauu.x += (self.player_speed * dt)
                    self.walking_timer += dt
                    self.last = pygame.K_d
            if self.vaisseauu.x >= 2900:
                if self.mars.x < self.finMap:
                    self.stand = False
                    self.mars.x += (self.player_speed * dt)
                    self.walking_timer += dt
                    self.last = pygame.K_d

    def apply_gravity(self):
        self.gravity += 1
        if self.sky.x < 2900:
            self.rect.y += self.gravity
        if self.sky.x >= 2900:
            self.rect.y += self.gravity * 0.3
        if self.rect.bottom >= self.groundHeight:
            self.rect.bottom = self.groundHeight
            self.is_jumping = False

    def animation_state(self, dt):
        if self.rect.bottom < self.groundHeight and self.rect.bottom > (self.groundHeight - 120):
            if self.last == pygame.K_q:
                self.image = self.player_jump[2]
            else:
                self.image = self.player_jump[0]
        elif self.rect.bottom < self.groundHeight:
            if self.last == pygame.K_q:
                self.image = self.player_jump[3]
            else:
                self.image = self.player_jump[1]
        elif self.stand:
            if self.last == pygame.K_q:
                self.image = self.player_walk_flip[0]
            else:
                self.image = self.player_walk[0]
        elif self.last == pygame.K_d:
            self.current_image_index += 0.2
            if self.current_image_index >= len(self.player_walk):
                self.current_image_index = 0
            self.image = self.player_walk[int(self.current_image_index)]
        elif self.last == pygame.K_q:
            self.current_image_index += 0.2
            if self.current_image_index >= len(self.player_walk):
                self.current_image_index = 0
            self.image = self.player_walk_flip[int(
                self.current_image_index)]

    def set_ground_height(self, height=718):
        if height:
            self.groundHeight = height

    def update(self, dt, fenetre, gh=718):

        if not self.music_started:
            self.music.play(loops=-1)
            self.music_started = True

        fenetre.blit(self.sky_surface, (-self.sky.x, 0))
        fenetre.blit(self.ground_surface, (-self.sky.x*1.5, 668))
        for decorPos in self.decorsPos:
            fenetre.blit(self.obstaclePneu,
                         (-self.sky.x * 1.5 + decorPos, 450))
        for tonneau in self.tonneauxPos:
            fenetre.blit(self.tonneau, (-self.sky.x*1.5 + tonneau, 645))
        fenetre.blit(self.vaisseau, (-self.sky.x*1.5 + 4500, 270))
        self.player_input(dt/1000)
        self.apply_gravity()
        self.animation_state(dt/1000)
        self.set_ground_height(gh)
        self.died()

        if self.sky.x >= 2900 and self.vaisseauu.x <= 3000:
            self.died()
            fenetre.blit(self.vaisseau_back, (-self.vaisseauu.x - 10, 0))
            fenetre.blit(self.vaisseausol, (-self.vaisseauu.x*1.5 - 10, 668))
           
            for monstres in self.monstrePos:
                fenetre.blit(self.monstre1, (-self.vaisseauu.x*1.5 + monstres, 600))

            for monstree in self.monstrePos2:
                fenetre.blit(self.monstre1, (-self.vaisseauu.x*1.5 + monstree, 200))

            for monstresAlien in self.monstreAlienPos:
                fenetre.blit(self.monstreAlien, (-self.vaisseauu.x*1.5 + monstresAlien, 300))

            for monstresAlien in self.monstreAlienPos2:
                fenetre.blit(self.monstreAlien, (-self.vaisseauu.x*1.5 + monstresAlien, 600))  
        
        if self.vaisseauu.x >= 3000:
            fenetre.blit(self.marsBg,(-self.mars.x - 10 , 0))
            fenetre.blit(self.marsg, (-self.mars.x*1.5 - 10, 668))
            self.music_started == False
            if not self.music_started2:
                self.music_started == False
                self.music3.play(loops=-1)
                self.music_started2 = True



           

            

    def died(self):
        if self.sky.x < 2900:
            for i in range(0, len(self.tonneaux), 2):
                if (self.sky.x >= self.tonneaux[i] and self.sky.x <= self.tonneaux[i+1]):
                    if self.rect.bottom >= 650:
                        self.music2.play()
                        self.sky.x = 0
        
        if self.sky.x >= 2900:
            for i in range(0, len(self.monstre), 2):
                if (self.vaisseauu.x >= self.monstre[i] and self.vaisseauu.x <= self.monstre[i+1]):
                    if self.rect.bottom >= 650:
                        self.music2.play()
                        self.vaisseauu.x = 0
            for i in range(0, len(self.monstre2), 2):
                if (self.vaisseauu.x >= self.monstre2[i] and self.vaisseauu.x <= self.monstre2[i+1]):
                    if self.rect.bottom <= 450:
                        self.music2.play()
                        self.vaisseauu.x = 0

            for i in range(0, len(self.monstreAlienliste2), 2):
                if (self.vaisseauu.x >= self.monstreAlienliste2[i] and self.vaisseauu.x <= self.monstreAlienliste2[i+1]):
                    if self.rect.bottom >= 600:
                        self.music2.play()
                        self.vaisseauu.x = 0
            for i in range(0, len(self.monstreAlienliste), 2):
                if (self.vaisseauu.x >= self.monstreAlienliste[i] and self.vaisseauu.x <= self.monstreAlienliste[i+1]):
                    if self.rect.bottom <= 550:
                        self.music2.play()
                        self.vaisseauu.x = 0

import pygame

class ButtonSprite(pygame.sprite.Sprite):
    def __init__(self, image_filenames, x, y):
        super().__init__()
        self.images = [pygame.image.load(filename) for filename in image_filenames]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image_index = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 125  # Vitesse de l'animation en millisecondes

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

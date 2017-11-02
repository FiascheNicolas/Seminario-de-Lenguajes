import pygame

class Piedra(pygame.sprite.Sprite):
    def __init__(self, posicionX, posicionY):
        pygame.sprite.Sprite.__init__(self)

        self.image = self.cargarImagen()
        self.y = posicionY
        self.x = posicionX
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def cargarImagen(self):
        self.path = pygame.image.load("imagenes/Background/Piedra.png")

        return pygame.transform.scale(self.path, (30, 30))

    def update(self):
        key = pygame.key.get_pressed()

        if(self.rect.y != 660):
            self.rect.y += 2

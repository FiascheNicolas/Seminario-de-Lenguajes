import pygame
import Malvavisco

class Piedra(pygame.sprite.Sprite):
    def __init__(self, posicionX, posicionY):
        pygame.sprite.Sprite.__init__(self)

        self.image = self.cargarImagen()
        self.y = posicionY
        self.x = posicionX
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.tiempoActiva = 0

    def cargarImagen(self):
        self.path = pygame.image.load("imagenes/Background/Piedra.png")

        return pygame.transform.scale(self.path, (30, 30))

    def update(self):
        #key = pygame.key.get_pressed()
        self.image = pygame.transform.scale(self.path, (30, 30))
        self.tiempoActiva += 1

    def die(self):
        self.actualizarPosicion(-300, 660)

    def devolverPosicionX(self):
        return self.rect.x

    def actualizarPosicion(self, posicionX, posicionY):
        self.rect.x = posicionX
        self.rect.y = posicionY

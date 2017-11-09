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
        self.thrown = False
        self.grados = 0

    def cargarImagen(self):
        self.path = pygame.image.load("imagenes/Background/Piedra.png")

        return pygame.transform.scale(self.path, (30, 30))

    def update(self):
        #key = pygame.key.get_pressed()
        self.image = pygame.transform.scale(self.path, (30, 30))
        self.grados += 3

        if self.thrown:
            self.image = pygame.transform.rotate(self.image, self.grados)
            self.rect.y -= 5
            if self.rect.y < -30:
                self.thrown = False

    def die(self):
        self.actualizarPosicion(-300, 660)

    def devolverPosicionX(self):
        return self.rect.x

    def actualizarPosicion(self, posicionX, posicionY):
        self.rect.y = posicionY
        self.rect.x = posicionX

    def piedraLanzada(self, malvavisco):
        self.rect.y = malvavisco.rect.y - 10
        self.rect.x = malvavisco.rect.x + 25

    def haveBeenThrown(self):
        return self.thrown

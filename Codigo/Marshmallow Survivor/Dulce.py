import pygame
from random import randint

class Dulce(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = self.cargarImagen()
        self.y = 0
        self.x = randint(0, 1300)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def cargarImagen(self):
        numero = randint(1, 15)
        self.path = pygame.image.load("imagenes/Background/Dulces/" + str(numero) + ".png").convert_alpha()
        return pygame.transform.scale(self.path, (30, 30))
    
    def update(self):
        self.image = pygame.transform.scale(self.path, (30, 30))
        self.rect.y += 3
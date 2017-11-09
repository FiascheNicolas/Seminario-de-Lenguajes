import pygame
from __init__ import cargarDatos
LIFEBAR = 4
PATH_LIFEBAR = "imagenes/LifeBar/"
RED=(255,0,0)

class LifeBar(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho):
        pygame.sprite.Sprite.__init__(self)
        #Settings
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
       
        self.vidas = 4
        #
        #Carga de animaciones
        self.lifebar = self.cargarAnimacion(LIFEBAR, PATH_LIFEBAR)
        #
        
        #
        #Settings de sprite
        self.image = pygame.transform.scale(self.lifebar[self.vidas], (self.alto, self.ancho))
        self.rect = self.image.get_rect()
       
        self.rect.x = x
        self.rect.y = y

    

    def update(self, *args):
        self.image = pygame.transform.scale(self.lifebar[self.vidas], (self.alto, self.ancho))
        
         
    def dropLista(self):
        del self.lifebar    

    

    def cargarAnimacion(self, cantidad, path):
        contador = 0
        listaAnimacion = []
        while contador != cantidad + 1:
            listaAnimacion.append(pygame.image.load(path + str(contador) + ".png").convert_alpha())
            contador += 1

        return listaAnimacion
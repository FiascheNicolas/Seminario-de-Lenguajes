import pygame

class Background(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.fondo = pygame.image.load("imagenes/Background/imagen.png").convert_alpha()
        self.image = pygame.transform.scale(self.fondo, (self.alto, self.ancho)) # el alto y ancho debe ser el mismo q del screen
        self.rect = self.image.get_rect()
        self.rect.x = x                      #Las posiciones x e y tienen que ser 0,0
        self.rect.y = y
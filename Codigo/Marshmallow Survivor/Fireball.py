import pygame
import math
from math import atan2, degrees, pi


class Fireball(pygame.sprite.Sprite):

    def __init__(self, x, y, alto, ancho, posMalvaviscoX, posMalvaviscoY):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.animacionIdle = self.cargarImagen(posMalvaviscoX,posMalvaviscoY,x,y)
        self.posIdle = 0
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (50,80))
        self.rect = self.image.get_rect()
        self.rect.y = self.y
        self.rect.x = self.x
        self.inversa = False
        self.velocidad = 9
        self.grados = 0
        self.sonidoColision = pygame.mixer.Sound("Sonidos/colisionFireball.ogg")
        self.fireballExiste = False
        self.dx=0
        self.dy=0

    def cargarImagen(self, posMalvaviscoX, posMalvaviscoY, x, y):
            contador = 0
            listaAnimacion = []

            while(contador<=9):
                image = pygame.image.load("imagenes/Fireball/" + str(contador) + ".png").convert_alpha()

                dx = posMalvaviscoX - x
                dy = posMalvaviscoY - y
                rads = atan2(-dy,dx)
                rads %= 2*pi
                self.grados = degrees(rads)
                image = pygame.transform.rotate(image, self.grados+90)
                listaAnimacion.append(image)
                contador += 1

            return listaAnimacion


    def update(self):
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (50,80))

        self.rect.x += self.dx * self.velocidad
        self.rect.y += self.dy * self.velocidad

        if self.posIdle == 9:
            self.inversa = True
        elif self.posIdle == 1:
            self.inversa = False
        if self.inversa:
            self.posIdle -= 1
        else:
            self.posIdle += 1

        self.die(False)

    def die(self,colision):
        if self.rect.bottom > 710 or colision:
            self.rect.bottom = 0
            self.fireballExiste = False


    def actualizarPosicion(self,posChefX,posChefY,posMalvaX,posMalvaY):

        self.rect.y = posChefY
        self.rect.x = posChefX

        # Distancia entre las posiciones X y Y, y se saca la recta que une los 2 puntos
        self.dx, self.dy = (posMalvaX + 100) - posChefX , posMalvaY - posChefY
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist

        difX = posMalvaX - posChefX
        difY = posMalvaY - posChefY
        rads = atan2(-difY,difX)
        rads %= 2*pi
        self.grados = degrees(rads)
        self.animacionIdle = self.cargarImagen(posMalvaX,posMalvaY,posChefX,posChefY)


    def dropLista(self):
        del self.animacionIdle[:]

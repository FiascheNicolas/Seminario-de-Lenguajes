#!/usr/bin/env python
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
        self.animacionIdle = self.cargarImagen(posMalvaviscoX, posMalvaviscoY,x,y)
        self.posIdle = 0
        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))

        self.rect = self.image.get_rect()
<<<<<<< HEAD
        self.rect.y = self.y
        self.rect.x = self.x
=======
        self.rect.y = y
        self.rect.x = x
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
        self.inversa = False
        self.velocidad = 5
        self.velocidad = 5

        # Distancia entre las posiciones X y Y, y se saca la recta que une los 2 puntos
        self.dx, self.dy = posMalvaviscoX - self.rect.x , posMalvaviscoY - self.rect.y
<<<<<<< HEAD
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist

=======

        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.velocidad = 5
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3


    def update(self):

        self.image = pygame.transform.scale(self.animacionIdle[self.posIdle], (self.alto, self.ancho))

        self.rect.x += self.dx * self.velocidad
        self.rect.y += self.dy * self.velocidad

<<<<<<< HEAD
=======


>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
        if self.posIdle == 9:
            self.inversa = True
        elif self.posIdle == 1:
            self.inversa = False

        if self.inversa:
            self.posIdle -= 1
        else:
            self.posIdle += 1


<<<<<<< HEAD

=======
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
        self.die()


    def cargarImagen(self,posMalvaviscoX, posMalvaviscoY,x,y):
        contador = 0
        listaAnimacion = []

        while(contador<=9):
            image = pygame.image.load("imagenes/Fireball/" + str(contador) + ".png").convert_alpha()
<<<<<<< HEAD

=======
            #
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3
            dx = posMalvaviscoX - x
            dy = posMalvaviscoY - y
            rads = atan2(-dy,dx)
            rads %= 2*pi
            grados = degrees(rads)
            image = pygame.transform.rotate(image, grados+90)
            listaAnimacion.append(image)
            contador += 1

        return listaAnimacion


    def die(self):
        if self.rect.bottom > 710:
            self.kill()
<<<<<<< HEAD

=======
>>>>>>> edb0dcc10936c654e9d5d3a52a9e7ad84fecf0f3

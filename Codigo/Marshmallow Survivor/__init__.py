# -*- coding: utf-8 -*-
#!/usr/bin/env python
import pygame
from pygame.locals import *
import Nivel
import gc


ALTO = 1360
ANCHO = 768
sonido = pygame.mixer.Sound("Sonidos/Menu.wav")
elementos =[]
PATH_ANIMACION_MENU = "imagenes/Menu/AnimacionMenu/"


class Opcion:
    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 0))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:

    def __init__(self, x, y, dy):
        self.image = pygame.image.load("imagenes/Menu/cursor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    "Representa un menú con opciones para un juego"

    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font("imagenes/Menu/Bloodthirsty.ttf", 50)
        x = 105
        y = 370
        paridad = 1


        self.cursor = Cursor(x - 30, y, 50)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 45
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        "Altera el valor de 'self.seleccionado' con los direccionales."

        k = pygame.key.get_pressed()


        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()

        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):

        "Imprime sobre 'screen' el texto de cada opción del menú."

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)


def dropLista():
    global elementos
    del elementos[:]
    
    
def comenzar_nuevo_juego():
    print "Boss jefe"
    global sonido
    sonido.stop()


    dropLista() #ELIMINO ANIMCACION MENU
   
    nivel = Nivel.Nivel(screen, ALTO, ANCHO)
    nivel.iniciar()
    
    del nivel
    global sonido
    sonido.play(-1)
    
    cargarDatos(PATH_ANIMACION_MENU)
    

def mostrar_opciones():
    fondo = pygame.image.load("imagenes/Menu/InstruccionesV3.png").convert_alpha()
    salir = False
    while not salir:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    salir = True

        screen.blit(fondo, (0, 0))
        
        pygame.display.flip()
        pygame.time.delay(10)
        
    

def creditos():
    fondo = pygame.image.load("imagenes/Menu/Credits.png").convert_alpha()
    salir = False
    while not salir:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    salir = True

        screen.blit(fondo, (0, 0))
        
        pygame.display.flip()
        pygame.time.delay(10)
def cargarDatos(path):
    global elementos
    contador=1
    while contador != 30:
        elementos.append(pygame.image.load(path + str(contador) + ".png"))
        contador +=1
    
def salir_del_programa():
    import sys
    print " Chau."
    sys.exit(0)


if __name__ == '__main__':

    #gc.set_debug(gc.DEBUG_LEAK)
    gc.enable()
    #print gc.isenabled()
    salir = False
    opciones = [
        ("Play", comenzar_nuevo_juego),
        ("Instructions", mostrar_opciones),
        ("Credits", creditos),
        ("Exit", salir_del_programa)
        ]

    pygame.font.init()
    screen = pygame.display.set_mode((ALTO, ANCHO))
    pygame.display.toggle_fullscreen()
    cargarDatos(PATH_ANIMACION_MENU)
    global elementos
    fondo = pygame.transform.scale(elementos[0],(ALTO,ANCHO))
    posMenu=1
    menu = Menu(opciones)
    global sonido
    sonido.play(10)






    while not salir:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    salir = True

        
        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(10)
        fondo = pygame.transform.scale(elementos[posMenu],(ALTO,ANCHO))
        posMenu +=1
        if(posMenu==29):
            posMenu=1

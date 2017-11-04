import pygame
import random
import Malvavisco
import Chef
import Background
import threading
import time
import Fireball
import Piedra

#0 a 1300

class Nivel():

    def __init__(self, screenMenu, alto, ancho):
        self.threadFinalizado = False
        self.spritesPrincipales = pygame.sprite.Group()
        self.spriteBackground = pygame.sprite.Group()
        self.spritesPiedra = pygame.sprite.Group()
        self.spritesFireball = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.screen = screenMenu
        self.alto = alto
        self.ancho = ancho
        self.fps = 60
        self.colores = { "RED" : (255,0,0), "BLACK" : (0,0,0) }
        self.iteradorParaTexto = 0
        self.textoPantallaDeCarga = "Cargando"
        self.contador = 0
        self.pausado = False
        self.piedraVisible = False
        self.piedraSiendoLanzada = False
        self.chefFurioso = False

    def iniciar(self):
        self.pantallaDeCarga()
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Marshmellow Survivor")
        ejecutandoNivel = True
        pygame.mixer.music.load("Sonidos/Nivel.wav")
        pygame.mixer.music.play(-1)

        while ejecutandoNivel:
            self.clock.tick(self.fps)
            self.contador += 1

            if self.malvavisco.thrown:
                self.piedra.piedraLanzada(self.malvavisco)
                self.piedra.thrown = True

            if self.piedra.thrown:
                self.malvavisco.thrown = False
                if pygame.sprite.collide_rect(self.piedra, self.chef):
                    print "hit"

            if self.contador % 180 == 0 and not self.chefFurioso:
                self.fireball.actualizarPosicion(self.chef.rect.centerx-40, self.chef.rect.centery,self.malvavisco.devolverPosicionX(),self.malvavisco.devolverPosicionY())
                self.chef.attacking = True
                self.fireball.fireballExiste = True
                if not self.piedra.thrown:
                    self.piedra.die()

            if self.contador % 720 == 0 and not self.malvavisco.rock and not self.piedra.thrown and not self.chefFurioso:
                self.piedra.actualizarPosicion(random.randrange(1300), 660)

            if self.contador % 1000 == 0:
                self.chefFurioso = True
                if self.contador % 2000 == 0:
                    self.chefFurioso = False

            if self.chefFurioso and self.contador % 100 == 0:
                self.chef.attacking = True
                self.fireball.actualizarPosicion(self.chef.rect.centerx-40, self.chef.rect.centery,self.malvavisco.devolverPosicionX(),self.malvavisco.devolverPosicionY())
                self.fireball.fireballExiste = True

            if 0 <= self.piedra.rect.x <= 1300 and not self.piedra.thrown:
                if pygame.sprite.collide_rect(self.piedra, self.malvavisco) and not self.malvavisco.salto:
                    self.malvavisco.rock = True
                    self.piedra.die()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ejecutandoNivel = False
                    if event.key == pygame.K_p:
                        self.pausado = not self.pausado

            if self.fireball.fireballExiste:
                hits = pygame.sprite.spritecollide(self.malvavisco, self.spritesFireball,
                    False, pygame.sprite.collide_circle)
                if hits:
                    self.fireball.sonidoColision.play()
                    self.fireball.die(True)

            if not self.pausado:
                self.spritesPrincipales.update()
                self.spritesPiedra.update()
                if self.fireball.fireballExiste:
                    self.spritesFireball.update()

            self.spriteBackground.draw(self.screen)
            self.spritesPrincipales.draw(self.screen)
            self.spritesPiedra.draw(self.screen)
            self.spritesFireball.draw(self.screen)

            if self.pausado:
                self.drawPauseScreen("PAUSA", 105,(255,0,0), self.alto / 2, self.ancho / 2)

            pygame.display.flip()

    def cargaDeDatos(self):
        self.malvavisco = Malvavisco.Malvavisco(375,550,150,150)
        self.spritesPrincipales.add(self.malvavisco)
        self.chef = Chef.Chef(500,0,250,250)
        self.spritesPrincipales.add(self.chef)
        self.background = Background.Background(0,0,1360,760)
        self.spriteBackground.add(self.background)
        self.fireball = Fireball.Fireball(0, -200, 30, 30,0,0)
        self.fireball.actualizarPosicion(self.chef.rect.centerx-1300, self.chef.rect.centery,self.malvavisco.devolverPosicionX(),self.malvavisco.devolverPosicionY())
        self.spritesFireball.add(self.fireball)
        self.piedra = Piedra.Piedra(-100, 660)
        self.spritesPiedra.add(self.piedra)
        #
        self.threadFinalizado = True

    def drawText(self, surf, text, size, x, y):
            font_name = pygame.font.match_font('arial')
            font = pygame.font.Font(font_name,size)
            text_surface = font.render(text, True, self.colores["RED"])
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            surf.blit(text_surface,text_rect)

    def pantallaDeCarga(self):
        self.clock.tick(60)
        threadDeCarga = threading.Thread(target=self.cargaDeDatos)
        threadDeCarga.start()

        while not self.threadFinalizado:
            self.screen.fill(self.colores["BLACK"])
            self.actualizarCargando()
            self.drawText(self.screen , self.textoPantallaDeCarga, 18, self.alto/2, self.ancho/2)
            pygame.display.flip()
            time.sleep(1.5)

    def actualizarCargando(self):
        self.textoPantallaDeCarga = self.textoPantallaDeCarga + "."

        if (self.iteradorParaTexto > 2):
            self.textoPantallaDeCarga = "Cargando"
            self.iteradorParaTexto = 0

        self.iteradorParaTexto += 1

    def drawPauseScreen(self,text,size,color,x,y):
            font_name = pygame.font.match_font('arial')
            font = pygame.font.Font(font_name,size)
            text_surface = font.render(text,True,color)
            text_rect = text_surface.get_rect()
            text_rect.center = (x,y)
            self.screen.blit(text_surface,text_rect)

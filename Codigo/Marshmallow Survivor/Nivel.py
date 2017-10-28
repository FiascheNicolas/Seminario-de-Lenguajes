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
        self.estadoFireball = False
        self.colores = { "RED" : (255,0,0), "BLACK" : (0,0,0) }
        self.iteradorParaTexto = 0
        self.textoPantallaDeCarga = "Cargando"
        self.cont = 0
        self.pausado = False
        self.piedraVisible = False
        self.contadorPiedra = 0

    def iniciar(self):
        self.pantallaDeCarga()
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Marshmellow Survivor")
        ejecutandoNivel = True
        pygame.mixer.music.load("Sonidos/Alone.mp3")
        pygame.mixer.music.play(-1)

        while ejecutandoNivel:
            self.clock.tick(self.fps)
            self.cont += 1
            self.contadorPiedra += 1

            self.piedraVisible = False
            if(self.contadorPiedra == 720 and self.piedraVisible == False):
                self.piedraVisible = True
                self.contadorPiedra = 0
                self.piedra = Piedra.Piedra(random.randrange(1300), 660)
                self.spritesPiedra.add(self.piedra)
                self.contadorPiedra = 0

            if(self.cont == 180):
                self.fireball = Fireball.Fireball(500, 0, 30, 30, self.malvavisco.devolverPosicionX(),
                    self.malvavisco.devolverPosicionY())
                self.spritesFireball.add(self.fireball)
                self.cont = 0

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ejecutandoNivel = False
                    if event.key == pygame.K_p:
                        self.pausado = not self.pausado

            if self.estadoFireball:
                hits = pygame.sprite.spritecollide(self.malvavisco, self.spritesFireball,
                    False, pygame.sprite.collide_circle)
                if hits:
                    fireball.sonidoColision.play()
                    fireball.kill()

            if not self.pausado:
                self.spritesPrincipales.update()
                self.spritesFireball.update()
                self.spritesPiedra.update()

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

# Creado por Luciano Vidal
# el 08/11/2020
# luccho277@gmail.com
import pygame , random
pygame.init()

#Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ALTO = 600
ANCHO = 800
screen_size = (ANCHO, ALTO)
ANCHO_JUGADOR = 15
ALTO_JUGADOR = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

class Jugador():
	def __init__(self,jugador,x,y,velocidad_y):
		self.jugador = jugador
		self.x = x
		self.y = y
		self.velocidad_y = velocidad_y
		self.punto = 0
		self.anoto = False
	
	def update(self):
		self.velocidad_y = 0
		self.rect = (self.x,self.y,ANCHO_JUGADOR,ALTO_JUGADOR)
		keystate = pygame.key.get_pressed()
		if self.jugador == 1:
			if keystate[pygame.K_w]:
				self.velocidad_y = -3
			if keystate[pygame.K_s]:
				self.velocidad_y = 3
			self.y += self.velocidad_y
			if self.y > ALTO - 90:
				self.y = ALTO - 90
			if self.y < 0:
				self.y = 0
		if self.jugador == 2:
			if keystate[pygame.K_UP]:
				self.velocidad_y = -3
			if keystate[pygame.K_DOWN]:
				self.velocidad_y = 3
			self.y += self.velocidad_y
			if self.y > ALTO - 90:
				self.y = ALTO - 90
			if self.y < 0:
				self.y = 0
		
class Pelota():
	def __init__(self,x,y,vel_x,vel_y):
		self.x = x
		self.y = y
		self.radio = 10
		self.rect = (x,y,10,10)
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.stop = True

	def update(self,jugador1,jugador2):
		self.x += self.vel_x
		self.y += self.vel_y
		keystate = pygame.key.get_pressed()
		if self.stop and keystate[pygame.K_SPACE]and jugador1.punto == 0 and jugador2.punto == 0:
			while self.vel_x == 0:
				self.vel_x = random.randrange(-3, 4) 
			while self.vel_y == 0:
				self.vel_y = random.randrange(-3, 4)
			self.stop = False
		if jugador1.anoto and self.stop:
			self.y = jugador1.y + ALTO_JUGADOR//2
			if keystate[pygame.K_d]:
				self.vel_x = 3
				if jugador1.velocidad_y < 0:
					self.vel_y = -3
				else:
					self.vel_y = 3
				self.stop = False
				jugador1.anoto = False
		if jugador2.anoto and self.stop:
			self.y = jugador2.y + ALTO_JUGADOR//2
			if keystate[pygame.K_LEFT]:
				self.vel_x = -3
				if jugador2.velocidad_y < 0:
					self.vel_y = -3
				else:
					self.vel_y = 3
				self.stop = False
				jugador2.anoto = False
		# revisa que la pelota no salga por arriba o abajo
		if self.y > 590 or self.y < 10:
			self.vel_y *= -1
		# Revisa si la pelota sale del lado derecho
		if self.x > 800:
			jugador1.punto +=1
			jugador1.anoto = True
			self.x = jugador1.x + ANCHO_JUGADOR * 2 - 4
			self.y = jugador1.y + ALTO_JUGADOR//2
			self.vel_x = 0
			self.vel_y = 0
			self.stop = True
		# Revisa si la pelota sale del lado izquierdo
		if self.x < 10:
			jugador2.punto +=1
			jugador2.anoto = True
			self.x = jugador2.x - ANCHO_JUGADOR + 4
			self.y = jugador2.y + ALTO_JUGADOR//2
			self.vel_x = 0
			self.vel_y = 0
			self.stop = True

#Fuentes
def mensaje_en_pantalla(superficie, texto, size , x, y):
	font = pygame.font.SysFont("Berlin Sans FB", size, True)
	superficie_texto = font.render(texto,True, WHITE)
	texto_rect = superficie_texto.get_rect()
	texto_rect.midtop = (x,y)
	superficie.blit(superficie_texto,texto_rect)

#Coordenadas y velocidad del jugador 1 (izquierda)
jugador1 = Jugador(1,50,300-45,0)

#Coordenadas y velocidad del jugador 2 (derecha)
jugador2 = Jugador(2,750 - ANCHO_JUGADOR,300-45,0)

# Coordenadas de la pelota
pelota = Pelota(400,300,0,0)

def colision(pelota_dibujo,rectangulo1,rectangulo2):
	if pelota_dibujo.colliderect(rectangulo1) or pelota_dibujo.colliderect(rectangulo2):
		#si la velocidad es mayor la deja en 3
		if pelota.vel_x >0:
			pelota.vel_x = 3
		else:
			pelota.vel_x -3
		pelota.vel_x *= -1 #cambien el sentido
		#si esta en moviento el jugador al momento de la colision aumenta velocidad
		if jugador1.velocidad_y != 0 and pelota_dibujo.colliderect(rectangulo1) :
			pelota.vel_x = 5
		elif jugador2.velocidad_y != 0 and pelota_dibujo.colliderect(rectangulo2):
				pelota.vel_x = -5
def ping_pong():
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
		#Logica
		jugador1.update()
		jugador2.update()
		pelota.update(jugador1,jugador2)

		screen.fill(BLACK)
		#Zona de dibujo
		rectangulo1 = pygame.draw.rect(screen, WHITE, (jugador1.x, jugador1.y, ANCHO_JUGADOR, ALTO_JUGADOR))#jugador 1
		rectangulo2 = pygame.draw.rect(screen, WHITE, (jugador2.x, jugador2.y, ANCHO_JUGADOR, ALTO_JUGADOR))#jugador 2
		pelota_dibujo = pygame.draw.circle(screen, WHITE, (pelota.x, pelota.y), pelota.radio)#pelota
		pygame.draw.rect(screen,WHITE,(ANCHO/2,0,3,ALTO)) #linea division de centro
		mensaje_en_pantalla(screen, str(jugador1.punto),ALTO//6, ANCHO/4, 50)# puntaje jugador 1
		mensaje_en_pantalla(screen, str(jugador2.punto),ALTO//6, ANCHO/1.33, 50) # puntaje jugador 2

		# Colisiones con jugadores
		colision(pelota_dibujo,rectangulo1,rectangulo2)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()
# ping_pong()
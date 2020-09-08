import pygame
pygame.init()



#Colores
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)
#variables 
    # Pantalla

alto = 600
ancho = 800
size = (ancho, alto)

#creamos ventana
screen = pygame.display.set_mode(size)
#Definimos reloj
clock = pygame.time.Clock()
valor_tick = 60


    #Lineas de separacion de carriles
rec_1_x = 290
rec_2_x = 410
rec_3_x = 530
rec_y = 10
speed_rec_y = 3

coor_list_1 = []
x = rec_1_x
y = rec_y
for i in range(6):
    coor_list_1.append([x, y])
    y += 100
    
coor_list_2 = []
x = rec_2_x
y = rec_y
for i in range(6):
    coor_list_2.append([x, y])
    y += 100
 
    coor_list_3 = []
x = rec_3_x
y = rec_y
for i in range(6):
    coor_list_1.append([x, y])
    y += 100
    
# INICIO Vehiculos  #
    
    # JUGADOR
    
car_x = 230
car_y = alto - 102
speed_car_x = 0
car = pygame.image.load("car.png").convert()
car.set_colorkey(WHITE)

    #AMBULANCIA

class Ambulancia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ambulance.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        
ambulancia = Ambulancia()   
ambulancia.rect.x = 280
ambulancia.rect.y = 0 
ambulancia.speed_amb_y = 7 

all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(ambulancia)
# FIN VEHICULOS  ##






#Imagen de fondo
background = pygame.image.load("fondo.png").convert()

game_over = False

#Bucle del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    
            
    ###### INICIO LOGICA del JUEGO #################
        #EVENTOS DEL TECLADO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed_car_x = 3
            if event.key == pygame.K_LEFT:
                speed_car_x = -3
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed_car_x = 0
            if event.key == pygame.K_LEFT:
                speed_car_x = 0
       
   ########## FIN LOGICA del JUEGO #################
    ##### INICIO ANIMACIONES ###########
    
    rec_y += speed_rec_y
    car_x += speed_car_x
    if car_x < 162:
        car_x = 162
    if car_x > 605:
        car_x = 605
    ambulancia.rect.y += ambulancia.speed_amb_y
    if ambulancia.rect.y > alto :
        ambulancia.rect.y = 0
    ##### FIN ANIMACIONES ###############
            
     ########  INICIO ZONA DE DIBUJO  #########
    #Rellenar el fondo
    screen.blit(background, [0,0])
    
    for j in coor_list_1:
        pygame.draw.rect(screen, WHITE, (j[0], j[1], 10, 50))
        j[1] += speed_rec_y
        if j[1] > alto:
            j[1] = 0
            
    for j in coor_list_2:
        pygame.draw.rect(screen, WHITE, (j[0], j[1], 10, 50))
        j[1] += speed_rec_y
        if j[1] > alto:
            j[1] = 0
            
    for j in coor_list_3:
        pygame.draw.rect(screen, WHITE, (j[0], j[1], 10, 50))
        j[1] += speed_rec_y
        if j[1] > alto:
            j[1] = 0
     
    screen.blit(car, [car_x, car_y])
    all_sprite_list.draw(screen)
    ######## FIN ZONA DE DIBUJO ############
    
    # Actualizar pantalla
    pygame.display.flip()
    # Control de velocidad del juego
    clock.tick(valor_tick)
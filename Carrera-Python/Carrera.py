import pygame
import time
pygame.init()
pygame.display.set_caption('Carrera de Obstaculos')



#Colores
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)


#variables 
    # Pantalla

alto = 595
ancho = 1000
size = (ancho, alto)

#creamos ventana
screen = pygame.display.set_mode(size)
#Definimos reloj
clock = pygame.time.Clock()
valor_tick = 20



############### MENU INICIO ###############################
#Fuentes
font = pygame.font.SysFont(None, 50)

def mensaje_en_pantalla(msg, color, txt_x, txt_y):
    txt_pantalla = font.render(msg, True, color)
    screen.blit(txt_pantalla, [txt_x, txt_y])
    

############## FIN MENU INICIO ############################


    #Lineas de separacion de carriles
rec_1_x = 290
rec_2_x = 410
rec_3_x = 530
rec_y = 10
speed_rec_y = 8

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
    coor_list_3.append([x, y])
    y += 100
    
# INICIO Vehiculos  #
# CLASE JUGADOR
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.car_x = 400
        self.car_y = alto-180
        self.speed_car_x = 0
        self.image = pygame.image.load("Imagen/car.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 44
        self.alto = 98


car = Car()
car.rect.y = 0
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(car)

#CLASE AMBULANCIA
class Ambulancia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_amb_y = 6
        self.image = pygame.image.load("Imagen/ambulance.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 120

ambulancia = Ambulancia()
ambulancia.rect.x = 280
ambulancia.rect.y = 0
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(ambulancia)

#CLASE POLICIA
class Police(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_pol_y = 4
        self.image = pygame.image.load("Imagen/police.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 124
police = Police()
police.rect.x = 400
police.rect.y = 0
all_sprite_list.add(police)

#CLASE TAXI
class Taxi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_taxi_y = 7
        self.image = pygame.image.load("Imagen/taxi.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 124

taxi = Taxi()
taxi.rect.x = 540
taxi.rect.y = 0
all_sprite_list.add(taxi)

#CLASE MINITRUCK
class Minitruck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_mini_y = 7
        self.image = pygame.image.load("Imagen/mini_truck.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 124

minitruck = Minitruck()
minitruck.rect.x = 150
minitruck.rect.y = 0
all_sprite_list.add(minitruck)

######## FIN CREACION DE ENEMIGOS Y JUGADOR ########


#Imagen de fondo
background = pygame.image.load("Imagen/fondo.png").convert()
game_over = False

#Bucle del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
   
            
    ###### INICIO LOGICA del JUEGO #################
        #EVENTOS DEL TECLADO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.speed_car_x = 7
            if event.key == pygame.K_LEFT:
                car.speed_car_x = -7
            if event.key == pygame.K_UP:
                valor_tick += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.speed_car_x = 0
            if event.key == pygame.K_LEFT:
                car.speed_car_x = 0

   ########## FIN LOGICA del JUEGO #################
    ##### INICIO ANIMACIONES ###########
    
    rec_y += speed_rec_y
    car.car_x += car.speed_car_x
    if car.car_x < 162:
        car.car_x = 162
    if car.car_x > 605:
        car.car_x = 605
    ambulancia.rect.y += ambulancia.speed_amb_y
    if ambulancia.rect.y > alto:
        ambulancia.rect.y = -150

    police.rect.y += police.speed_pol_y
    if police.rect.y > alto:
        police.rect.y = -150
    taxi.rect.y += taxi.speed_taxi_y
    if taxi.rect.y > alto:
        taxi.rect.y = -150

    minitruck.rect.y += minitruck.speed_mini_y
    if minitruck.rect.y > alto:
        minitruck.rect.y = -150

    ##### COLISIONES #####
    if car.car_x >= ambulancia.rect.x and \
            car.car_x < ambulancia.rect.x + ambulancia.ancho +30 and \
                car.car_y +car.alto >= ambulancia.rect.y and \
                    car.car_y <= ambulancia.rect.y + ambulancia.alto:
                            game_over = True

    if car.car_x >= taxi.rect.x and \
            car.car_x < taxi.rect.x + taxi.ancho + 30 and \
                car.car_y + car.alto >= taxi.rect.y and \
                    car.car_y <= taxi.rect.y + taxi.alto:
                            game_over = True

    if car.car_x >= police.rect.x and \
            car.car_x < police.rect.x + police.ancho + 30 and \
                car.car_y + car.alto >= police.rect.y and \
                    car.car_y <= police.rect.y + police.alto:
                            game_over = True
                            
                            

    if car.car_x >= minitruck.rect.x and \
            car.car_x < minitruck.rect.x + minitruck.ancho +40 and \
                car.car_y + car.alto >= minitruck.rect.y and \
                    car.car_y <= minitruck.rect.y + minitruck.alto:
                            game_over = True

    ##### FIN COLISIONES ###############
    ##### FIN ANIMACIONES ###############
            
     ########  INICIO ZONA DE DIBUJO  #########
    #Rellenar el fondo
    screen.blit(background,[0,0])

    for j in coor_list_1:
        pygame.draw.rect(screen, WHITE, (j[0], j[1], 10, 50))
        j[1] += speed_rec_y
        if j[1] > alto:
            j[1] = -20
            
    for j in coor_list_2:
        pygame.draw.rect(screen, WHITE, (j[0], j[1], 10, 50))
        j[1] += speed_rec_y
        if j[1] > alto:
            j[1] = -20
            
    for j in coor_list_3:
        pygame.draw.rect(screen, WHITE, (j[0], j[1], 10, 50))
        j[1] += speed_rec_y
        if j[1] > alto:
            j[1] = -20
     
    screen.blit(car.image, [car.car_x, car.car_y])
    all_sprite_list.draw(screen)
    ######## FIN ZONA DE DIBUJO ############
    
    # Actualizar pantalla
    pygame.display.flip()
    # Control de velocidad del juego
    clock.tick(valor_tick)
mensaje_en_pantalla("SI VOLVES A PERDER, MERLINO TE DESAPRUEBA", RED, 50, 200)
pygame.display.update()    
    
    
#Mensaje parpadeante(cuelga la ventana)
#for i in range(10):
#    mensaje_en_pantalla("SI VOLVES A PERDER, MERLINO TE DESAPRUEBA", RED, 50, 200)
#   pygame.display.update()
#   time.sleep(0.3)
#    mensaje_en_pantalla("SI VOLVES A PERDER, MERLINO TE DESAPRUEBA", WHITE, 50, 200)
#    pygame.display.update()
#    time.sleep(0.3)
time.sleep(2)
pygame.quit()

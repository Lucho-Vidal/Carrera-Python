import pygame
import time
pygame.init()
pygame.display.set_caption('Carrera de Obstaculos')

########### $$$$CONSTANTES$$$$ ###########
#Colores
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)

#Variables
 # Pantalla
alto = 595
ancho = 795
size = (ancho, alto)

#Crear ventana
screen = pygame.display.set_mode(size)

#Imagen de fondo
background = pygame.image.load("Imagen/fondo.png").convert()

#Fuentes
font = pygame.font.SysFont(None, 50)

#Definimos reloj
clock = pygame.time.Clock()

############### MENU INICIO ###############################
def mensaje_en_pantalla(msg, color, txt_x, txt_y):
    txt_pantalla = font.render(msg, True, color)
    screen.blit(txt_pantalla, [txt_x, txt_y])

def menu():
    screen.fill(BLACK)
    mensaje_en_pantalla("CARRERA DE OBSTACULOS", RED, 150, 110)
    mensaje_en_pantalla("1. Jugar", WHITE, 180, 220)
    mensaje_en_pantalla("2. Instrucciones", WHITE, 180, 270)
    mensaje_en_pantalla("3. Puntaje más alto", WHITE, 180, 320)
    mensaje_en_pantalla("4. Salir", WHITE, 180, 370)
    pygame.display.update()

def instrucciones():
    screen.fill(BLACK)
    mensaje_en_pantalla("Use las flachas izquierda y ", WHITE, 20, 220)
    mensaje_en_pantalla("derecha para moverse", WHITE, 20, 270)
    mensaje_en_pantalla("Presione ESC para pausar", WHITE, 20, 320)
    pygame.display.update()
    time.sleep(3)

def puntajeAlto():
    screen.fill(BLACK)
    mensaje_en_pantalla("1. " + max_score(), WHITE, 155, 270)
    pygame.display.update()
    time.sleep(3)
############## FIN MENU INICIO ############################

################ Funcion Pausa ####
def pausa():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill(BLACK)
        pygame.draw.rect(screen,BLACK, (110,160,550,200))
        mensaje_en_pantalla("PAUSA", RED, 300, 200)
        mensaje_en_pantalla("Presiona ESC para continuar", WHITE, 150, 270)
        mensaje_en_pantalla("Presiona Q para salir", WHITE, 150, 320)
        pygame.display.update()
        clock.tick(5)
############ FIN Funcion Pausa #############
        
        
############## ARCHIVO DE PUNTAJE MÁS ALTO ########################
def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))
def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score
######## FIN ARCHIVO DE PUNTAJE MÁS ALTO ##########

######## INICIO  Clases Vehiculos  ########

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

#CLASE AMBULANCIA
class Ambulancia(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_amb_y = 5
        self.image = pygame.image.load("Imagen/ambulance.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 120

#CLASE POLICIA
class Police(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_pol_y = 3
        self.image = pygame.image.load("Imagen/police.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 124

#CLASE TAXI
class Taxi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_taxi_y = 4
        self.image = pygame.image.load("Imagen/taxi.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 124

#CLASE MINITRUCK
class Minitruck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed_mini_y = 10
        self.image = pygame.image.load("Imagen/mini_truck.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = 58
        self.alto = 124

######## FIN  Clases Vehiculos  ########


    
fin_bucle = False
score = 0

#Bucle del juego
def bucle_principal():
    global score, objetivo
    game_over = False
    
    valor_tick = 60

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
        
 ###########  CREACION DE VEHICULOS   ###########
    car = Car()
    car.rect.y = 0
    all_sprite_list = pygame.sprite.Group()
    all_sprite_list.add(car)
    
    ambulancia = Ambulancia()
    ambulancia.rect.x = 280
    ambulancia.rect.y = 0
    all_sprite_list = pygame.sprite.Group()
    all_sprite_list.add(ambulancia)       
            
    police = Police()
    police.rect.x = 150
    police.rect.y = 0
    all_sprite_list.add(police)
    
    taxi = Taxi()
    taxi.rect.x = 540
    taxi.rect.y = 0
    all_sprite_list.add(taxi)
    
    minitruck = Minitruck()
    minitruck.rect.x = 400
    minitruck.rect.y = -1000
    all_sprite_list.add(minitruck)

 ###########  FIN CREACION DE VEHICULOS  ###########

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                break

        ###### INICIO LOGICA del JUEGO #################
            #EVENTOS DEL TECLADO

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    car.speed_car_x = 7
                if event.key == pygame.K_LEFT:
                    car.speed_car_x = -7
                if event.key == pygame.K_UP:
                    valor_tick += 5
                if event.key == pygame.K_ESCAPE:
                    pausa()
                
                
                

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
            minitruck.rect.y = -1500

        ##### COLISIONES #####
        if ambulancia.rect.x <= car.car_x < ambulancia.rect.x + ambulancia.ancho +30 and \
                    car.car_y +car.alto >= ambulancia.rect.y and \
                        car.car_y <= ambulancia.rect.y + ambulancia.alto:
                                game_over = True
                                update_score(score)
                                score = 0

        if taxi.rect.x <= car.car_x < taxi.rect.x + taxi.ancho + 30 and \
                    car.car_y + car.alto >= taxi.rect.y and \
                        car.car_y <= taxi.rect.y + taxi.alto:
                                game_over = True
                                update_score(score)
                                score = 0
        if police.rect.x <= car.car_x < police.rect.x + police.ancho + 30 and \
                    car.car_y + car.alto >= police.rect.y and \
                        car.car_y <= police.rect.y + police.alto:
                                game_over = True
                                update_score(score)
                                score = 0
        if minitruck.rect.x <= car.car_x < minitruck.rect.x + minitruck.ancho +40 and \
                    car.car_y + car.alto >= minitruck.rect.y and \
                        car.car_y <= minitruck.rect.y + minitruck.alto:
                                game_over = True
                                update_score(score)
                                score = 0
        ##### FIN COLISIONES ###############
        ##### FIN ANIMACIONES ###############
                
         ########  INICIO ZONA DE DIBUJO  #########
        #Rellenar el fondo
        screen.blit(background, [0, 0])
    
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
        mensaje_en_pantalla(str(score), WHITE, 0, 0)

        score += 1
        if score%500 == 0:
            valor_tick += 10
        if score%5000 == 0:
            valor_tick += 20


        ######## FIN ZONA DE DIBUJO ############
        
        # Actualizar pantalla
        pygame.display.flip()
        # Control de velocidad del juego
        clock.tick(valor_tick)

    screen.fill(BLACK)
    mensaje_en_pantalla("SI VOLVES A PERDER", WHITE, 200, 220)
    mensaje_en_pantalla("MERLINO TE DESAPRUEBA", WHITE, 155, 270)


    pygame.display.update()
    time.sleep(2)

## FIN DE BUCLE DEL JUEGO ##### 

    
while not fin_bucle == True:

            menu()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        bucle_principal()
                    if event.key == pygame.K_2:
                        instrucciones()
                    if event.key == pygame.K_3:
                        puntajeAlto()
                    if event.key == pygame.K_4:
                        pygame.display.quit()
                        break





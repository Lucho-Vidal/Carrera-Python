import pygame ,  random
pygame.init() 
import time

pygame.display.set_caption('Carrera de Obstaculos')

########### $$$$CONSTANTES$$$$ ###########
#Colores
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0, 0, 255)


CARRIL_UNO = 150
CARRIL_DOS = 280
CARRIL_TRES = 400
CARRIL_CUATRO = 540
CARRIL = [CARRIL_UNO,CARRIL_DOS,CARRIL_TRES,CARRIL_CUATRO]
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

class Vehiculo(pygame.sprite.Sprite):
    def __init__(self, car_x , car_y , rect_x, rect_y , speed_x , speed_y , ruta_imagen , ancho, alto):
        super().__init__()
        self.car_x = car_x
        self.car_y = car_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = pygame.image.load(ruta_imagen).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = rect_y
        self.rect.x = rect_x
        self.ancho = ancho
        self.alto = alto
    
    def modificar_Velocidad(self,velocidad):
        self.speed_y = velocidad
    # modifico la velocida por carril para que no se sobrepongan
    def cambiar_carril(self, carril):
        self.rect.x = carril
        if carril == CARRIL_UNO:
            self.modificar_Velocidad(3)
        if carril == CARRIL_DOS:
            self.modificar_Velocidad(5)
        if carril == CARRIL_TRES:
            self.modificar_Velocidad(6)
        if carril == CARRIL_CUATRO:
            self.modificar_Velocidad(4)
    # voy a tratar de que no se sobrepongan los vehiculos
    def colisiones_vehiculos(self,vehiculo):
        colision = False
        if self.rect.x <= vehiculo.rect.x < self.rect.x + self.ancho + 30 and \
                    vehiculo.rect.y + vehiculo.alto >= self.rect.y and \
                        vehiculo.rect.y <= self.rect.y + self.alto:
                        colision = True
        return colision

######## FIN  Clases Vehiculos  ########

#Bucle del juego
score = 0
def bucle_principal():
    
    global score
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
    car = Vehiculo(380,alto-180,0,0,0,0,"Imagen/car.png",44,98)
    all_sprite_list = pygame.sprite.Group()
    all_sprite_list.add(car)
    
    ambulancia = Vehiculo(CARRIL_DOS,-200,CARRIL_DOS,-200,0,5,"Imagen/ambulance.png",58,120)
    all_sprite_list = pygame.sprite.Group()
    all_sprite_list.add(ambulancia)       
            
    police = Vehiculo(CARRIL_UNO,-500,CARRIL_UNO,-500,0,3,"Imagen/police.png",58,124)
    all_sprite_list.add(police)
    
    taxi = Vehiculo(CARRIL_CUATRO,-300,CARRIL_CUATRO,-300,0,4,"Imagen/taxi.png",58,124)
    all_sprite_list.add(taxi)
    
    minitruck = Vehiculo(CARRIL_TRES,-300,CARRIL_TRES,-300,0,6,"Imagen/mini_truck.png",58,124)
    all_sprite_list.add(minitruck)


 ###########  FIN CREACION DE VEHICULOS  ###########

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                game_over = True

        ###### INICIO LOGICA del JUEGO #################
            #EVENTOS DEL TECLADO

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    car.speed_x = 7
                if event.key == pygame.K_LEFT:
                    car.speed_x = -7
                if event.key == pygame.K_UP:
                    valor_tick += 5
                if event.key == pygame.K_DOWN:
                    valor_tick += -10
                if event.key == pygame.K_ESCAPE:
                    pausa()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    car.speed_x = 0
                if event.key == pygame.K_LEFT:
                    car.speed_x = 0

       ########## FIN LOGICA del JUEGO #################

        ##### INICIO ANIMACIONES ###########
        rec_y += speed_rec_y
        car.car_x += car.speed_x
        if car.car_x < 162:
            car.car_x = 162
        if car.car_x > 605:
            car.car_x = 605

        # si pasaron la pantalla vuelven a aparecer arriba
        ambulancia.rect.y += ambulancia.speed_y
        if ambulancia.rect.y > alto:
            ambulancia.rect.y = -180
            ambulancia.cambiar_carril(CARRIL[random.randrange(0, 4)])
            if ambulancia.colisiones_vehiculos(police) or\
                ambulancia.colisiones_vehiculos(taxi) or\
                    ambulancia.colisiones_vehiculos(minitruck):
                        ambulancia.rect.y += -180
           
        police.rect.y += police.speed_y
        if police.rect.y > alto:
            police.rect.y = -180
            police.cambiar_carril(CARRIL[random.randrange(0, 3)])
            if police.colisiones_vehiculos(ambulancia) or\
                police.colisiones_vehiculos(taxi) or\
                    police.colisiones_vehiculos(minitruck):
                        police.rect.y += -180

        taxi.rect.y += taxi.speed_y
        if taxi.rect.y > alto:
            taxi.rect.y = -180
            taxi.cambiar_carril(CARRIL[random.randrange(1, 4)])
            if taxi.colisiones_vehiculos(police) or\
                taxi.colisiones_vehiculos(ambulancia) or\
                    taxi.colisiones_vehiculos(minitruck):
                        taxi.rect.y += -180

        minitruck.rect.y += minitruck.speed_y
        if minitruck.rect.y > alto:
            minitruck.rect.y = -180
            minitruck.cambiar_carril(CARRIL[random.randrange(2, 4)])
            if minitruck.colisiones_vehiculos(police) or\
                minitruck.colisiones_vehiculos(taxi) or\
                    minitruck.colisiones_vehiculos(ambulancia):
                        minitruck.rect.y += -180

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
        if score%500 == 0 and valor_tick < 100 :
            valor_tick += 10
        if score%5000 == 0 and valor_tick < 140:
            valor_tick += 20
        print (valor_tick)

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




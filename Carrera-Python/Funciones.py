import pygame ,  random
pygame.init() 
pygame.mixer.init()
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

 # Pantalla
alto = 595
ancho = 795
size = (ancho, alto)

#Crear ventana
screen = pygame.display.set_mode(size)

#Imagen de fondo
background = pygame.image.load("Imagen/fondo.png").convert()

#Sonidos
sonido_explosion = pygame.mixer.Sound("Sonido/explosion.wav")
sonido_salud = pygame.mixer.Sound("Sonido/laser5.ogg")
pygame.mixer.music.load("Sonido/music.ogg")
pygame.mixer.music.set_volume(0.2)

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
    mensaje_en_pantalla("1. Jugar", WHITE, 180, 150)
    mensaje_en_pantalla("2. Jugar de a Dos", WHITE, 180, 200)
    mensaje_en_pantalla("3. Instrucciones", WHITE, 180, 250)
    mensaje_en_pantalla("4. Puntaje más alto", WHITE, 180, 300)
    mensaje_en_pantalla("5. Salir", WHITE, 180, 420)
    mensaje_en_pantalla("6. Salir", WHITE, 180, 470)
    pygame.display.update()

def instrucciones():
    screen.fill(BLACK)
    mensaje_en_pantalla("Use las flachas izquierda y ", WHITE, 20, 220)
    mensaje_en_pantalla("derecha para moverse", WHITE, 20, 270)
    mensaje_en_pantalla("Presione ESC para pausar", WHITE, 20, 320)
    mensaje_en_pantalla("Si chocas pierdes vida,", WHITE, 20, 370)
    mensaje_en_pantalla("pero cada 1000 puntos de score se carga!", WHITE, 20, 420)
    pygame.display.update()
    time.sleep(5)

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
def carriles( x):
    #Lineas de separacion de carriles
    y = 10
    lista = []
    for i in range(6):
        lista.append([x, y])
        y += 100
    
    return lista
        
def dibujar_barra_vida(superficie , x , y , porcentaje):
    barra_largo = 100
    barra_alto = 10
    fill = (porcentaje / 100) * barra_largo
    borde = pygame.Rect(x , y , barra_largo, barra_alto)
    fill = pygame.Rect(x , y , fill , barra_alto)
    if porcentaje > 30:
        pygame.draw.rect(superficie, GREEN , fill)
    else:
        pygame.draw.rect(superficie, RED , fill)
    pygame.draw.rect(superficie, WHITE , borde , 2)

def reaparecer(ambulancia, police , taxi, minitruck):
    ambulancia.rect.y += ambulancia.speed_y
    if ambulancia.rect.y > alto:
        ambulancia.rect.y = -180
        ambulancia.cambiar_carril(CARRIL[random.randrange(0, 4)])
        if ambulancia.colisiones_vehiculos(police) or\
            ambulancia.colisiones_vehiculos(taxi) or\
                ambulancia.colisiones_vehiculos(minitruck):
                    ambulancia.rect.y += -200
           
    police.rect.y += police.speed_y
    police.rect.x += police.speed_x
    if police.rect.y > alto:
        police.rect.y = -180
        police.cambiar_carril(CARRIL[random.randrange(0, 3)])
        if police.colisiones_vehiculos(ambulancia) or\
            police.colisiones_vehiculos(taxi) or\
                police.colisiones_vehiculos(minitruck):
                    police.rect.y += -200

    taxi.rect.y += taxi.speed_y
    if taxi.rect.y > alto:
        taxi.rect.y = -200
        taxi.cambiar_carril(CARRIL[random.randrange(1, 4)])
        if taxi.colisiones_vehiculos(police) or\
            taxi.colisiones_vehiculos(ambulancia) or\
                taxi.colisiones_vehiculos(minitruck):
                    taxi.rect.y += -200

    minitruck.rect.y += minitruck.speed_y
    minitruck.rect.x += minitruck.speed_x
    if minitruck.rect.y > alto:
        minitruck.rect.y = -180
        minitruck.cambiar_carril(CARRIL[random.randrange(2, 4)])
        if minitruck.colisiones_vehiculos(police) or\
            minitruck.colisiones_vehiculos(taxi) or\
                minitruck.colisiones_vehiculos(ambulancia):
                    minitruck.rect.y += -200

def verificar_colisiones(car,ambulancia , taxi, police, minitruck, score,valor_tick):
    game_over = False
    if car.colisiones_vehiculos(ambulancia):
        car.vida -= 10
        time.sleep(1)
        car.car_x = 380
        if valor_tick>100:
            valor_tick=60
        if car.vida <= 0:
                game_over = True
                update_score(score)
                score = 0
    if car.colisiones_vehiculos(taxi):
        car.vida -= 20
        time.sleep(1)
        car.car_x = 380
        if valor_tick>100:
            valor_tick=60
        if car.vida <= 0:
                game_over = True
                update_score(score)
                score = 0
    if car.colisiones_vehiculos(police):
        car.vida -= 40
        time.sleep(1)
        car.car_x = 380
        if valor_tick>100:
            valor_tick=60
        if car.vida <= 0:
                game_over = True
                update_score(score)
                score = 0
    if car.colisiones_vehiculos(minitruck):
        car.vida -= 45
        time.sleep(1)
        car.car_x = 380
        if valor_tick>100:
            valor_tick=60
        if car.vida <= 0:
                game_over = True
                update_score(score)
                score = 0
    return valor_tick,game_over

def captura_evento(car, valor_tick):
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
    return valor_tick
######## FIN  Clases Vehiculos  ########






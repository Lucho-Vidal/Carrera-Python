from Funciones import *
from Clases import *
import PingPong

#Bucle del juego
score = 0
def bucle_principal():
    
    global score
    game_over = False
    valor_tick = 60
    # #Lineas de separacion de carriles
    coor_list_1 = carriles(290)#carril 1
    coor_list_2 = carriles(410)#carril 2
    coor_list_3 = carriles(530)#carril 3
    rec_y = 10
    speed_rec_y = 8
        
 ###########  CREACION DE VEHICULOS   ###########
    all_sprite_enemy = pygame.sprite.Group()
    all_sprite = pygame.sprite.Group()

    car = Jugador(380,alto-180,0,0,"Imagen/car.png",44,98)
    all_sprite.add(car) 

    ambulancia = Transito(CARRIL_DOS,-200,0,5,"Imagen/ambulance.png",58,120)
    all_sprite.add(ambulancia)   
    all_sprite_enemy.add(ambulancia)    
            
    police = Transito(CARRIL_UNO,-500,0,3,"Imagen/police.png",58,124)
    all_sprite.add(police)
    all_sprite_enemy.add(police)
    
    taxi = Transito(CARRIL_CUATRO,-300,0,4,"Imagen/taxi.png",58,124)
    all_sprite.add(taxi)
    all_sprite_enemy.add(taxi)
    
    minitruck = Transito(CARRIL_TRES,-300,0,6,"Imagen/mini_truck.png",58,124)
    all_sprite.add(minitruck)
    all_sprite_enemy.add(minitruck)
 ###########  FIN CREACION DE VEHICULOS  ###########
    pygame.mixer.music.play(loops=-1)
    while not game_over:
        ###### INICIO LOGICA del JUEGO #################
        valor_tick = captura_evento(car, valor_tick)
       ########## FIN LOGICA del JUEGO #################

        ##### INICIO ANIMACIONES ###########
        rec_y += speed_rec_y
        car.car_x += car.speed_x
        if car.car_x < 162:
            car.car_x = 162
        if car.car_x > 605:
            car.car_x = 605

        # si pasaron la pantalla vuelven a aparecer arriba
        reaparecer(ambulancia, police , taxi, minitruck)
        ##### COLISIONES #####
        resultado = verificar_colisiones(car,ambulancia , taxi, police, minitruck, score,valor_tick)
        valor_tick,game_over = resultado
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
        all_sprite_enemy.draw(screen)
        mensaje_en_pantalla(str(score), WHITE, 0 , 50)

        score += 1
        if score%500 == 0 and valor_tick < 100 :
            valor_tick += 10
        if score%5000 == 0 and valor_tick < 140:
            valor_tick += 20
        if score%1000 == 0 and car.vida < 100:
            car.vida += 10
            sonido_salud.play()
        
        dibujar_barra_vida(screen , 5 , 5 , car.vida)
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

fin_bucle = False   
while not fin_bucle:
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                fin_bucle = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                bucle_principal()
            if event.key == pygame.K_2:
                instrucciones()
            if event.key == pygame.K_3:
                puntajeAlto()
            if event.key == pygame.K_4:
                PingPong.ping_pong()
            if event.key == pygame.K_5:
                pygame.display.quit()
                fin_bucle = True
                    
                    
                        
pygame.display.quit()
from Funciones import *

fin_bucle = False   
while not fin_bucle == True:

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
                        pygame.display.quit()
                        fin_bucle = True
                    
                        
pygame.display.quit()





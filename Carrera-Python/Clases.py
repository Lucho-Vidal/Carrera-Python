from Funciones import *

######## INICIO  Clases Vehiculos  ########

class Vehiculo(pygame.sprite.Sprite):
    def __init__(self , speed_x , speed_y , ruta_imagen , ancho, alto):
        super().__init__()
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.image = pygame.image.load(ruta_imagen).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.ancho = ancho
        self.alto = alto
        self.image.set_colorkey(WHITE)
    
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
    def colisiones_vehiculos(self,vehiculo, car = False):
        colision = False
        if isinstance(self,Jugador):
            if vehiculo.rect.x <= self.car_x < vehiculo.rect.x + vehiculo.ancho +30 and \
                    self.car_y +self.alto >= vehiculo.rect.y and \
                        self.car_y <= vehiculo.rect.y + vehiculo.alto:
                        colision = True
        elif isinstance(self,Curacion):
            car.vida += 10
        else:
            if self.rect.x <= vehiculo.rect.x < self.rect.x + self.ancho + 30 and \
                        vehiculo.rect.y + vehiculo.alto >= self.rect.y and \
                            vehiculo.rect.y <= self.rect.y + self.alto:
                            colision = True
        return colision

class Jugador(Vehiculo):
    def __init__(self, car_x , car_y , speed_x , speed_y , ruta_imagen , ancho, alto):
        super().__init__( speed_x , speed_y , ruta_imagen , ancho, alto)
        self.car_x = car_x
        self.car_y = car_y
        self.rect.y = car_x
        self.rect.x = car_y
        self.vida = 100

class Transito(Vehiculo):
    def __init__(self, rect_x, rect_y , speed_x , speed_y , ruta_imagen , ancho, alto):
        super().__init__(speed_x , speed_y , ruta_imagen , ancho, alto)
        self.rect.y = rect_y
        self.rect.x = rect_x
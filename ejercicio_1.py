#CLASE DE NIVEL 3
class Vehiculo:
    def __init__ (self, marca:str, anio:int, posicion_inicial=0):
        self.marca=marca
        self.anio=anio
        self.posicion_inicial=posicion_inicial

#CLASES DE NIVEL 2
class VehiculoTerrestre(Vehiculo):
    _patentes_terrestres_registradas=set()

    ### aca abajo ni hace falta que yo ponga posicion_inicial, porque enrealidad cuando
    ### yo llamo a super().__init__ , este directamente ejecuta todo el constructor del padre 
    ### de esta clase, por ende automáticamente ve que existe posicion_inicial y que vale 0

    def __init__ (self, patente:str, marca:str, anio:int):
        super().__init__(marca, anio)
        ##por qué ahí después del igual va el self.????
        self.patente=self._validar_patente(patente)

    def _validar_patente(self, patente):
        if patente in self._patentes_terrestres_registradas:
            raise ValueError(f'La patente {patente} ya está registrada')
        ##por qué se escribe así esta línea de abajo??
        self._patentes_terrestres_registradas.add(patente)
        return patente

class VehiculoAcuatico(Vehiculo):
    _patentes_acuaticas_registradas=set()
    def __init__ (self, patente_acuatica:str, marca:str, anio:int):
        super().__init__(marca, anio)
        self.patente_acuatica=self._validar_patente_acuatica(patente_acuatica)

    def _validar_patente_acuatica(self, patente):
        if patente in self._patentes_acuaticas_registradas:
            raise ValueError(f'La patente {patente} ya está registrada')
        self._patentes_acuaticas_registradas.add(patente)
        return patente

#CLASES DE NIVEL 1
class Auto(VehiculoTerrestre):
    def __init__ (self, patente:str, marca:str, anio:int, posicion_inicial:str):
        super().__init__(patente, marca, anio)
        self.posicion_inicial=0

    def trasladarse(self, desplazamiento:int):
        self.posicion_inicial+=desplazamiento
        print(f'El movimiento por tierra fue {desplazamiento}, y la posición acutal es {self.posicion_inicial}. ')

    def __str__(self):
        return f'Este es un auto patente {self.patente}, marca {self.marca}, año {self.anio}, y su posición es {self.posicion_inicial}. '

class Camion(VehiculoTerrestre):
    def __init__ (self, patente:str, marca:str, anio:int, carga:str):
        super().__init__(patente, marca, anio)
        self.carga=carga
        self.posicion_inicial=0

    def __str__(self):
        return f'Este es un camión patente {self.patente}, marca {self.marca}, año {self.anio}, y su carga es {self.carga}. '

class Lancha(VehiculoAcuatico):
    def __init__(self, patente_acuatica:str, marca:str, anio:int, marca_motor:str):
        super().__init__(patente_acuatica, marca, anio)
        self.marca_motor=marca_motor

    def trasladarse(self, desplazamiento:int):
        self.posicion_inicial+=desplazamiento
        print(f'El movimiento por agua a motor fue {desplazamiento}, y la posición acutal es {self.posicion_inicial}. ')

    def __str__(self):
        return f'Este es una Lancha patente {self.patente_acuatica}, marca {self.marca}, año {self.anio}, y con motor marca {self.marca_motor}. '

class Velero(VehiculoAcuatico):
    def __init__(self, patente_acuatica:str, marca:str, anio:int, cantidad_velas:int):
        super().__init__(patente_acuatica, marca, anio)
        self.cantidad_velas=cantidad_velas

    def trasladarse(self, desplazamiento:int):
            self.posicion_inicial+=desplazamiento
            print(f'El movimiento por agua a vela fue {desplazamiento}, y la posición acutal es {self.posicion_inicial}. ')

    def __str__(self):
        return f'Este es un velero patente {self.patente_acuatica}, marca {self.marca}, año {self.anio}, y tiene{self.cantidad_velas} velas. '
    
class Anfibio(VehiculoTerrestre, Lancha):
    def __init__(self, patente:str, marca:str, anio:int, patente_acuatica:str, marca_motor:str):
        VehiculoTerrestre.__init__(self, patente, marca, anio)
        Lancha.__init__(self, patente_acuatica, marca, anio, marca_motor)

    def trasladarse(self, desplazamiento: int):
        self.posicion_inicial+=desplazamiento
        return f"El Anfibio con patente {self.patente} se trasladó por tierra y su nueva posición es {self.posicion_inicial}."

    def trasladarse_por_agua(self, desplazamiento: int):
        self.posicion_inicial += desplazamiento
        return f"El Anfibio con patente acuática {self.patente_acuatica} se trasladó por agua a motor y su nueva posición es {self.posicion_inicial}."
        pass

    def __str__(self):
        return f"Este es un Anfibio marca {self.marca}, año {self.anio}, con patente terrestre {self.patente} y acuática {self.patente_acuatica}, motor {self.marca_motor}."
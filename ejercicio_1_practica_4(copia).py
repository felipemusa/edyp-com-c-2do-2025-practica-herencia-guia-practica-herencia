###########################################################################################################
from collections import Counter

class Camion:
    #Al poner el guion bajo, le estás diciendo: "Esta variable es para uso 
    #interno de la clase, por favor, no la toques directamente, usa los métodos que yo te doy."
    #esto es un ATRIBUTO DE CLASE y está aca fuera para que cualquier instancia(cualquier objeto) pueda acceder a él
    _patentes_registradas=set()
    def __init__(self, patente, marca, carga, anio):
        self.patente = self._validar_patente(patente)
        self.marca = marca
        self.carga = carga
        self.anio = anio

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

    #esto es para el punto B. 
    #para el punto C haría falta solamente self.patente==otro.patente y returnear eso
    def __eq__(self, otro):
        if not isinstance(otro,Camion):
            return False
        #este return de abajo si todo coincide va a ser True, sino False
        return (self.patente==otro.patente and
            self.marca==otro.marca and
            self.carga==otro.carga and
            self.anio==otro.anio)
    
    def _validar_patente(self, patente):
        if patente in self._patentes_registradas:
            raise ValueError(f'La patente {patente} ya está registrada')
        self._patentes_registradas.add(patente)
        return patente
    
    def setter_carga(self,nueva_carga):
        self.carga=nueva_carga


###########################################################################################################
lista_camiones=[]
def registrar_camion():
    try:
        patente = input("Ingresa la patente del camión: ")
        marca = input("Ingresa la marca del camión: ")
        carga = int(input("Ingresa la carga (kg): "))
        anio = int(input("Ingresa el año de fabricación: "))

        nuevo_camion = Camion(patente, marca, carga, anio)
        
        # Si no hubo excepción, agrega el camión a la lista
        lista_camiones.append(nuevo_camion)
        print(f"¡Camión con patente {patente} registrado exitosamente!")

    except ValueError as e:
        #En tu caso, si la validación de la patente falla, el constructor de Camion lanza una 
        # excepción ValueError con un mensaje. Ese mensaje se guarda en la variable e, y luego 
        # la línea print(f"Error al registrar el camión: {e}") lo muestra al usuario.

        # Si ocurre un error, muestra el mensaje de la excepción
        print(f"Error al registrar el camión: {e}")

    except Exception as e:
        # En caso de otro error, muestra un mensaje genérico
        print(f"Ocurrió un error inesperado: {e}")

def modificar_carga():
    try:
        patente=input('Ingrese la patente del camión a modificar: ')
        camion_encontrado=None
        for camion in lista_camiones:
            if camion.patente==patente:
                camion_encontrado=camion
                break
        
        if camion_encontrado:
            nueva_carga=int(input('Ingrese la nueva carga: '))
            camion_encontrado.setter_carga(nueva_carga)
            print(f'Carga del camión con patente {patente} modificada a {nueva_carga}.')
        else:
            print(f"Error: No se encontró un camión con la patente {patente}.")
                
    except ValueError as e:
        print(f'Error. La carga debe ser un número entero {e}')
    except Exception as e:
        print(f'Ocurrión un error {e}.')

def mostrar_camiones():
    if not lista_camiones:
        print('Todavía no hay camiones creados.')
        return
    
    #key=...: Este argumento le dice a sorted() en qué criterio basarse para ordenar. Le estás diciendo: "Para cada elemento de mi lista, usa la información que me devuelva la función lambda para decidir su posición."
    # lambda camion: camion.anio: Esta es una función anónima (sin nombre) y de una sola línea. Lo que hace es:
    #   Toma un objeto al que llama camion (es un nombre temporal, podría ser x o cualquier otro).
    #   Devuelve el valor de su atributo .anio.
    camiones_ordenados=sorted(lista_camiones, key=lambda camion: camion.anio)
    for camion in camiones_ordenados:
        print('-'*25)
        print(camion)

def mostrar_marca_mas_frecuente():
    if not lista_camiones:
        print('Todavía no hay camiones creados.')
        return

    marcas=[]
    for camion in lista_camiones:
        marcas.append(camion.marca) 

    # Usa Counter para contar las marcas
    conteo_marcas = Counter(marcas)

    # Encuentra la marca más común
    marca_mas_frecuente = conteo_marcas.most_common(1)

    if marca_mas_frecuente:
        marca, cantidad = marca_mas_frecuente[0]
        print(f"La marca más registrada es '{marca}', con {cantidad} camiones.")
    else:
        print("No hay marcas para mostrar.")

###########################################################################################################

if __name__ == "__main__":
    opcion = None
    while opcion != 9:
        try:
            opcion = int(input('''
Seleccione una opción:
1. Registrar un nuevo camión.
2. Modificar la carga de un camión.
3. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
4. Mostrar por terminal la marca que más veces fue registrada.
9. Salir
> '''))
            if opcion == 1:
                registrar_camion()
            elif opcion == 2:
                modificar_carga()
            elif opcion == 3:
                mostrar_camiones()
            elif opcion == 4:
                mostrar_marca_mas_frecuente()
            elif opcion == 9:
                print("Saliendo...")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número entero.")

#líneas lancha    
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2)
print(furgon1 is furgon2)
print(furgon3 == furgon4)
print(furgon3 is furgon4)
print(furgon1 == furgon4) 
"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from math import cos
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr
assert cf
import threading

from DISClib.ADT import stack

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar catalogo.")
    print("2- Cargar información al catalogo.")
    print('3- Encontrar componentes conectados en la red y saber si dos landing points pertenecen al mismo cluster.')
    print('4- Encontrar ruta mas corta para enviar información entre dos paises.')
    print('5- Identificar infraestructura critica.')

catalog = None


def crearCatalogo():
    catalog = controller.crearCatalogo()
    return catalog

def cargarCatalogo(catalog):
    controller.cargarCatalogo(catalog)
    

def mostrarDatosCarga(catalog):
    total_landing = gr.numVertices(catalog['connections'])
    total_conexiones = gr.numEdges(catalog['connections'])
    total_paises = mp.size(catalog['countries'])
    primer_landing = lt.firstElement(catalog['lista_landings'])
    ultimo_pais =  lt.lastElement(catalog['lista_pais'])
    print('El total de landings es de: ', total_landing)
    print('El total de conexiones es de: ', total_conexiones)
    print('El total de paises es de: ', total_paises)
    print('El primer landing cargado es: \n',primer_landing )
    print('El ultimo pais cargado es: \n', ultimo_pais)


def requerimiento1(catalog, landing1, landing2):
    numero_conectados, estan_conectados = controller.requerimiento1(catalog, landing1, landing2)
    print('El numero total de clusters en la red es de ', numero_conectados)
    if estan_conectados == True:
        res = 'Los dos landing points estan en el mismo cluster'
    else:
        res = 'Los dos landing points no estan en el mismo cluster'
    print(res)




def requerimiento2(catalog, pais1, pais2):
    camino, costo_total = controller.requerimiento2(catalog, pais1, pais2)
    print('La distancia total de la ruta es de: ', costo_total, 'km')
    tamano = stack.size(camino)
    for i in range(tamano):
        elemento = stack.pop(camino)
        print('Ruta de ',elemento['vertexA'], ' a ', elemento['vertexB'], ' con distancia de ', elemento['weight'], 'km')




def requerimiento3(catalog):
    total_vertices, costo_total = controller.requerimiento3(catalog)
    print('\nLa cantidad de vertices conectados a la red de expresion minima es de: ', total_vertices)
    print('El costo total en km de la red de expancion minima es de: ', costo_total)


"""
Menu principal
"""
def thread_cycle():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("Inicializando catalogo ....")
            catalog = crearCatalogo()
            print('Catalogo creado.')
        elif int(inputs[0]) == 2:
            print("Cargando catalogo ...")
            cargarCatalogo(catalog)
            mostrarDatosCarga(catalog)
        elif int(inputs[0]) == 3:
            landing1 = input('Ingrese el nombre del primer landing point: ')
            landing2 = input('Ingrese el nombre del segundo landing point: ')
            requerimiento1(catalog, landing1, landing2)
        elif int(inputs[0]) == 4:
            pais1 = input('Ingrese el primer pais: ')
            pais2 = input('Ingrese el segundo pais: ')
            requerimiento2(catalog, pais1, pais2)
        elif int(inputs[0]) == 5:
            requerimiento3(catalog)
        else:
            sys.exit(0)
#sys.exit(0)



if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()
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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr
assert cf


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






"""
Menu principal
"""
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
        

    else:
        sys.exit(0)
sys.exit(0)

"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv

import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# Inicializacion

def crearCatalogo():
    return model.crearCatalogo()



def cargarCatalogo(catalog):
    archivo_paises = cf.data_dir + 'countries.csv'
    archivo_connections = cf.data_dir + 'connections.csv'
    archivo_landing = cf.data_dir + 'landing_points.csv'
    paises = csv.DictReader(open(archivo_paises, encoding="utf-8"),delimiter=",")
    connections = csv.DictReader(open(archivo_connections, encoding='utf-8-sig'),delimiter=",")
    landing_points = csv.DictReader(open(archivo_landing, encoding="utf-8"),delimiter=",")
    for country in paises:
        model.cargarCountries(catalog, country)
    for landing in landing_points:
        model.cargarLandingPoints(catalog,landing)
    for connection in connections:
        model.cargarConnections(catalog, connection)
    model.agregarRutasLanding(catalog)
    

# requerimiento 1
def requerimiento1(catalog, landing1, landing2):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    numero_conectados, estan_conectados = model.requerimiento1(catalog, landing1, landing2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return numero_conectados, estan_conectados, delta_time, delta_memory


#requerimiento 2
def requerimiento2(catalog, pais1, pais2):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    camino, costo_total = model.requerimiento2(catalog, pais1, pais2)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return camino, costo_total, delta_time, delta_memory


#requerimiento 3
def requerimiento3(catalog):
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    total_vertices, costo_total, ruta_larga, tamano_ruta_larga = model.requerimiento3(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return total_vertices, costo_total, ruta_larga, tamano_ruta_larga, delta_time, delta_memory




# ======================================
# Funciones para medir tiempo y memoria
# =====================================
def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from math import e
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import graph as gr
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

#importacion modulo para usar la funcion haversine
import haversine as hs


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def crearCatalogo():
    """
    se crea el catalogo:
        * landing_points es una tabla de hash que guarda las caracteristicas de los diferentes landing points
          el key es el id.
        * countries es una tabla de hash que guarda las caracteristicas de los diferentes paises presentes, el 
          key es el nombre del pais.
        * connection es un graph que guarla las relaciones entre los landin points y sus origenes y destinos. 
    """
    catalog = {'landing_points': None, 'countries': None, 'connections': None, 'lista_landings': None, 'lista_pais': None}
    catalog['landing_points'] = mp.newMap(1400,maptype='PROBING')
    catalog['countries'] = mp.newMap(300, maptype='PROBING')
    catalog['connections'] = gr.newGraph(datastructure='ADJ_LIST', directed = True, size=3300)
    catalog['lista_landings'] = lt.newList('ARRAY_LIST')
    catalog['lista_pais'] = lt.newList('ARRAY_LIST')
    return catalog

def cargarCountries(catalog, country):
    nombre = country['CountryName'].lower()
    mp.put(catalog['countries'], nombre, country)
    lt.addLast(catalog['lista_pais'], country)

def cargarLandingPoints(catalog, landing):
    id = landing['landing_point_id']
    valor = {'datos': landing, 'rutas': lt.newList('ARRAY_LIST')}
    mp.put(catalog['landing_points'], id, valor)
    lt.addLast(catalog['lista_landings'], landing)

def cargarConnections(catalog, connection):
    id_origen = connection['origin']
    id_destino = connection['destination']
    datos_origen = mp.get(catalog['landing_points'],id_origen)['value']
    datos_destino = mp.get(catalog['landing_points'],id_destino)['value']
    nombre_origen = datos_origen['datos']['id']
    nombre_destino = datos_destino['datos']['id']
    cable = connection['cable_id']
    vertice_origen = nombre_origen +'-'+ cable
    vertice_destino = nombre_destino + '-' + cable
    agregarCableLanding(datos_origen, datos_destino, cable)
    agregarvertice(catalog, vertice_origen)
    agregarvertice(catalog, vertice_destino)
    costo = encontrarCosto(datos_origen, datos_destino)
    agregarRuta(catalog, vertice_origen, vertice_destino, costo)

def encontrarCosto(datos_origen, datos_destino):
    latitud_origen = float(datos_origen['datos']['latitude'])
    latitud_destino = float(datos_destino['datos']['latitude'])
    longitud_origen = float(datos_origen['datos']['longitude'])
    longitud_destino = float(datos_destino['datos']['longitude'])
    loc1 = (latitud_origen, longitud_origen)
    loc2 = (latitud_destino, longitud_destino)
    costo = round(hs.haversine(loc1, loc2),3)
    return costo
    


def agregarCableLanding(datos_origen, datos_destino, cable):
    lista_origen = datos_origen['rutas']
    lista_destino = datos_destino['rutas']
    lt.addLast(lista_origen, cable)
    lt.addLast(lista_destino, cable)

def agregarvertice(catalog, vertice):
    #try:
    if not gr.containsVertex(catalog['connections'], vertice):
        gr.insertVertex(catalog['connections'], vertice)
    #except:
def agregarRuta(catalog, origen, destino, costo):
    edge = gr.getEdge(catalog['connections'],origen, destino)
    if edge is None:
        gr.addEdge(catalog['connections'], origen, destino, costo)

def agregarRutasLanding(catalog):
    lista_landings =  mp.keySet(catalog['landing_points'])
    for key in lt.iterator(lista_landings):
        nombre = key.split('-')
        pais = nombre[1]
        capital = mp.get(catalog['countries'], pais)['value']['CapitalName'].lower()
        vertice_capital = capital+'-'+pais
        agregarvertice(catalog['connections'], vertice_capital)
        lista_rutas = mp.get(catalog['landing_points'], key)['value']['rutas']
        anterior = None
        for landing in lt.iterator(lista_rutas):
            actual = landing
            agregarRuta(catalog, actual, vertice_capital)
            agregarRuta(catalog, vertice_capital, actual)
            if anterior is not None:
                agregarRuta(catalog,anterior, actual, 0.1)
                agregarRuta(catalog,actual, anterior, 0.1)
            anterior = actual




# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

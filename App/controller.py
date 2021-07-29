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
    numero_conectados, estan_conectados = model.requerimiento1(catalog, landing1, landing2)
    return numero_conectados, estan_conectados


#requerimiento 2
def requerimiento2(catalog, pais1, pais2):
    camino, costo_total = model.requerimiento2(catalog, pais1, pais2)
    return camino, costo_total


#requerimiento 3
def requerimiento3(catalog):
    return model.requerimiento3(catalog)
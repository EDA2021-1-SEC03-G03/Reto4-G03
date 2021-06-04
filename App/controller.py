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

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# Funciones para la carga de datos


def loadConnections(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.

    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile = cf.data_dir + "connections.csv"
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")

    for entry in input_file:

        model.addLandingConnections(analyzer, entry)

    return analyzer


def loadLandingPoints(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.

    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile = cf.data_dir + "landing_points.csv"
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")

    for lp in input_file:

        model.landingPoints(analyzer, lp)

    return analyzer


def loadCountries(analyzer):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.

    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile = cf.data_dir + "countries.csv"
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8"),
                                delimiter=",")

    for country in input_file:

        model.countries(analyzer, country)

    return analyzer


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def totalLandingPoints(analyzer):
    """
    Total de paradas de autobus
    """
    return model.totalLandingPoints(analyzer)


def totalConnections(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalConnections(analyzer)


def totalCountries(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalCountries(analyzer)


def firstInfo(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.firstInfo(analyzer)


def lastInfo(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.lastInfo(analyzer)


# REQ 1
def clusterSearch(analyzer, lp1, lp2):
    """
    Total de enlaces entre las paradas
    """
    return model.clusterSearch(analyzer, lp1, lp2)


# REQ 2
def connectionSearch(analyzer):
    """
    Los vertices con mayor cantidad de conexiones
    """
    return model.connectionSearch(analyzer)
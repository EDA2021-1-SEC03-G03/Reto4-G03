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


import config as cf
from DISClib.ADT.graph import gr
# from DISClib.ADT import list as lt
from DISClib.ADT import map as m
# from DISClib.DataStructures import mapentry as me
# from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Utils import error as error
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""


def newAnalyzer():
    try:
        analyzer = {'landingPoint': None,
                    'connections': None,
                    'country': None,
        
                   }


        analyzer['landingPoint'] = m.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareStopIds)

        analyzer['connections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# ==============================
# Construccion de modelos
# ==============================

def addLandingConnections(analyzer, service):

    try:
        origin = formatOriginVertex(service)
        destination = formatDestinationVertex(service)
        distance = service['cable_length']
        addPoint(analyzer, origin)
        addPoint(analyzer, destination)
        addConnections(analyzer, origin, destination, distance)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addLandingConnections')

# ==============================
# Funciones para agregar informacion al catalogo
# ==============================

def addPoint(analyzer, stopid):
    """
    Adiciona una estación como un vertice del grafo
    """
    try:
        if not gr.containsVertex(analyzer['connections'], stopid):
            gr.insertVertex(analyzer['connections'], stopid)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addPoint')


def addConnections(analyzer, origin, destination, distance):
    """
    Adiciona un arco entre dos estaciones
    """
    try:
        edge = gr.getEdge(analyzer['connections'], origin, destination)
        if edge is None:
            gr.addEdge(analyzer['connections'], origin, destination, distance)
        return analyzer

    except Exception as exp:
        error.reraise(exp, 'model:addConnections')



# ==============================
# Funciones para creacion de datos
# ==============================

# ==============================
# Funciones de consulta
# ==============================


def totalLandingPoints(analyzer):
    """
    Retorna el total de estaciones (vertices) del grafo
    """
    return gr.numVertices(analyzer['connections'])


def totalConnections(analyzer):
    """
    Retorna el total arcos del grafo
    """
    return gr.numEdges(analyzer['connections'])


def totalCountries(analyzer):
    """
    Retorna el total arcos del grafo
    """
    return gr.numEdges(analyzer['connections'])


def formatOriginVertex(service):
    """
    Se formatea el nombrer del vertice con el id de la estación
    seguido de la ruta.
    """
    name = service['\ufefforigin'] + '-'
    name = name + service['cable_id']
    return name

def formatDestinationVertex(service):
    """
    Se formatea el nombrer del vertice con el id de la estación
    seguido de la ruta.
    """
    name = service['destination'] + '-'
    name = name + service['cable_id']
    return name

# ==============================
# Funciones utilizadas para comparar elementos dentro de una lista
# ==============================


def compareStopIds(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1


# ==============================
# Funciones de ordenamiento
# ==============================

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
from DISClib.ADT import list as lt
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.DataStructures import linkedlistiterator as ite
from DISClib.Algorithms.Graphs import scc as sc
from DISClib.Algorithms.Graphs import dijsktra as dj
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
                    'vertex': None}

        analyzer['landingPoint'] = m.newMap(numelements=14000,
                                            maptype='PROBING',
                                            comparefunction=compareStopIds)

        analyzer['country'] = m.newMap(numelements=14000,
                                       maptype='PROBING',
                                       comparefunction=compareStopIds)

        analyzer['connections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)

        analyzer['vertex'] = lt.newList('ARRAY_LIST')

        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# ==============================
# Construccion de modelos
# ==============================

def addLandingConnections(analyzer, service):

    try:
        origin = service['\ufefforigin']
        destination = service['destination']
        distance = service['cable_length']

        addPoint(analyzer, origin)
        addPoint(analyzer, destination)
        op1 = origin not in analyzer['vertex']
        op2 = destination not in analyzer['vertex']

        if op1 or op2:
            lt.addLast(analyzer['vertex'], origin)
            lt.addLast(analyzer['vertex'], destination)

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
        gr.addEdge(analyzer['connections'], origin, destination, distance)
        return analyzer

    except Exception as exp:
        error.reraise(exp, 'model:addConnections')


def landingPoints(analyzer, lp):

    try:
        country = m.newMap(numelements=5, maptype='PROBING')
        latitud = lp['latitude']
        longitud = lp['longitude']
        coordenates = (latitud, longitud)

        m.put(country, 'Name', lp['name'])
        m.put(country, 'Id', lp['id'])
        m.put(country, 'Coordenates', coordenates)

        m.put(analyzer['landingPoint'], lp['landing_point_id'], country)

        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:landingPoints')


def countries(analyzer, country):

    try:

        capital = m.newMap(numelements=13, maptype='PROBING')
        latitud = country['CapitalLatitude']
        longitud = country['CapitalLongitude']
        coordenates = (latitud, longitud)

        m.put(capital, 'CapitalName', country['CapitalName'])
        m.put(capital, 'Coordenates', coordenates)
        m.put(capital, 'CountryCode', country['CountryCode'])
        m.put(capital, 'ContinentName', country['ContinentName'])
        m.put(capital, 'Population', country['Population'])
        m.put(capital, 'Internet users', country['Internet users'])
        m.put(analyzer['country'], country['CountryName'], capital)

        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:countries')
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
    return m.size(analyzer['country'])


def firstInfo(analyzer):
    """
    Retorna el total arcos del grafo
    """

    first = lt.firstElement(analyzer['vertex'])

    countryCity = m.get(analyzer['landingPoint'], first)
    countryDict = countryCity['value']
    coordenates = m.get(countryDict, 'Coordenates')['value']
    name = m.get(countryDict, 'Name')['value']
    vertex = (first, name, coordenates)

    return vertex


def lastInfo(analyzer):
    """
    Retorna el total arcos del grafo
    """

    last = lt.lastElement(analyzer['vertex'])

    countryCity = m.get(analyzer['landingPoint'], last)
    countryDict = countryCity['value']
    name = m.get(countryDict, 'Name')['value']
    country = name.split(', ')[2]
    print(country)

    countryInfo = m.get(analyzer['country'], country)
    countryInfo = countryInfo['value']
    population = m.get(countryInfo, 'Population')['value']
    users = m.get(countryInfo, 'Internet users')['value']

    vertex = (population, users)

    return vertex


# REQ1
def clusterSearch(analyzer, lp1, lp2):
    """
    Total de enlaces entre las paradas
    """
    op1 = lt.isPresent(analyzer["vertex"], lp1) 
    op2 = lt.isPresent(analyzer["vertex"], lp2)
    if op1 and op2:
        scc = sc.KosarajuSCC(analyzer["connections"])
        question = sc.stronglyConnected(scc, lp1, lp2)
        return scc["components"], question
    else:
        return 0


# REQ2
def connectionSearch(analyzer):
    """
    Total de enlaces entre las paradas
    """
    vertexlist = lt.newList('SINGLE_LINKED')
    vertetex = gr.vertices(analyzer['connections'])
    iterator = ite.newIterator(vertetex)
    while ite.hasNext(iterator):
        pos = ite.next(iterator)
        number = gr.degree(analyzer['connections'], pos)
        lt.addLast(vertexlist, (pos, number))
    finallist = sortreq2(vertexlist)
    return finallist


# REQ 3
def shortestRoute(analyzer, country1, country2):
    firstsearch = m.get(analyzer['country'], country1)
    secondsearch = m.get(analyzer['country'], country2)
    if firstsearch is None or secondsearch is None:
        return 0
    else:
        capital1 = me.getValue(firstsearch)
        capital2 = me.getValue(secondsearch)

        capi1 = m.get(capital1, "CapitalName")
        capi2 = m.get(capital2, "CapitalName")

        cap1 = me.getValue(capi1)
        cap2 = me.getValue(capi2)

        capis1 = m.get(analyzer["landingPoint"], cap1)
        capis2 = m.get(analyzer["landingPoint"], cap2)

        minpath = dj.Dijkstra(analyzer["connections"], capid1)

        distance = dj.distTo(minpath, capid2)
        route = dj.pathTo(minpath, capid2)

        return distance, route


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


def cmpConnections(vertex1, vertex2):
    return (vertex1[1] > vertex2[1])


# ==============================
# Funciones de ordenamiento
# ==============================


def sortreq2(lista):
    if lt.isEmpty(lista):
        lt.newList = 0
    else:
        newlist = sa.sort(lista, cmpConnections)
    return newlist

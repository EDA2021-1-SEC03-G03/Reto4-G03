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

import config
import sys
import controller
assert config


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Landing point belonging to a cluster")
    print("4- Landing point as a connection point")
    print("5- Ruta minima para enviar entre paises")
    print("6- Red de expansion minima")
    print("7- Lista de paises afectados")
    print("8- Ancho de banda maximo por pais")
    print("9- Ruta minima para enviar datos a una ip")
    print("0- Salir del sistema")


def optionTwo(cont):
    print("\nCargando información de los cables...")
    controller.loadServices(cont, servicefile)
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalStops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("Cargando información de las rutas....")
        controller.loadConnections(cont)
        controller.loadLandingPoints(cont)
        controller.loadCountries(cont)
        numVertex = controller.totalLandingPoints(cont)
        numEdges = controller.totalConnections(cont)
        numCountries = controller.totalCountries(cont)
        firstVertex = controller.info(cont)
        lastVertex = controller.info(cont)

        print('Numero de landing points: ' + str(numVertex))
        print('Numero de conexiones: ' + str(numEdges))
        print('Numero de paises: ' + str(numCountries))
        print('Primer vertice: ' + str(firstVertex))
        print('Ultimo vertice: ' + str(lastVertex))
        print('\n')


    elif int(inputs[0]) == 3:
        print("Cargando información de los archivos ....")
        pass

    elif int(inputs[0]) == 4:
        print("Cargando información de los archivos ....")
        pass

    elif int(inputs[0]) == 5:
        print("Cargando información de los archivos ....")
        pass

    elif int(inputs[0]) == 6:
        print("Cargando información de los archivos ....")
        pass

    elif int(inputs[0]) == 7:
        print("Cargando información de los archivos ....")
        pass

    elif int(inputs[0]) == 8:
        print("Cargando información de los archivos ....")
        pass

    elif int(inputs[0]) == 9:
        print("Cargando información de los archivos ....")
        pass

    else:
        sys.exit(0)
sys.exit(0)

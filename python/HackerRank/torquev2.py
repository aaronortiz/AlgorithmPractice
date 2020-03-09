#!/bin/python3

import math
import os
import random
import re
import sys

# ------------------------------------------------------------------------------
def getAllCities(roads):
    cities = {}
    for road in roads:
        cityFrom = road[0]
        cityTo = road[1]

        addRoadToCity(cities, cityFrom, cityTo)

    return cities


# ------------------------------------------------------------------------------
def addRoadToCity(cities, city1, city2):
    if not city1 in cities:
        cities[city1] = [city2]
    else:
        cities[city1].append(city2)

    if not city2 in cities:
        cities[city2] = [city1]
    else:
        cities[city2].append(city1)


# ------------------------------------------------------------------------------
def dictCount(weirdDict):
    count = 0

    for entry in weirdDict:
        count += len(weirdDict[entry])

    return count


# ------------------------------------------------------------------------------
def removeConnectedReferences(cities, city):

    # Delete back references to city if connected
    for fromCity in cities:
        if city in cities[fromCity]:
            cities[fromCity].remove(city)

    print("removed", city, "from", cities)

    return True


# ------------------------------------------------------------------------------
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, roads):

    unconnectedCities = getAllCities(roads)  # Gets list of all conections per city

    if c_road > c_lib or len(roads) == 0:
        return c_lib * n
    else:
        libRunningTotal = 0
        roadRunningTotal = 0
        libraryCities = []
        queue = []
        history = []

        # build a library in all cities with no connections, no idea on names though
        if n > len(roads):
            libRunningTotal += c_lib * (n - 1 - len(roads))

        while dictCount(unconnectedCities) > 0:

            # print("cities", unconnectedCities)

            # Build a lib in a city
            fortunateCity = list(unconnectedCities.keys())[0]
            libRunningTotal += c_lib
            libraryCities.append(fortunateCity)

            # remove all reachable cities from fortunateCity from unconnectedCities
            queue.append(fortunateCity)
            print("added", fortunateCity, "to queue")
            while len(queue) > 0:
                fromCity = queue.pop()
                history.append(fromCity)
                print("added", fromCity, "to history")
                print("from city is", fromCity)
                if fromCity in unconnectedCities:
                    toCities = unconnectedCities[fromCity]
                    for toCity in toCities:
                        if (
                            toCity in unconnectedCities
                            and not toCity in queue
                            and not toCity in history
                        ):
                            queue.append(toCity)
                            print("added", toCity, "to queue")
                            print("built", fromCity, toCity)
                            roadRunningTotal += c_road

                    del unconnectedCities[fromCity]
                    removeConnectedReferences(unconnectedCities, fromCity)

            print("lib built in", fortunateCity)

    return roadRunningTotal + libRunningTotal


if __name__ == "__main__":

    n = 9
    c_lib = 91
    c_road = 84
    roads = [
        [8, 2],
        [2, 9],
    ]

    result = roadsAndLibraries(n, c_lib, c_road, roads)
    print(result)  # Should be 805

    n = 5
    c_lib = 92
    c_road = 23
    roads = [
        [2, 1],
        [5, 3],
        [5, 1],
        [3, 4],
        [3, 1],
        [5, 4],
        [4, 1],
        [5, 2],
        [4, 2],
    ]

    result = roadsAndLibraries(n, c_lib, c_road, roads)
    print(result)  # Should be 184

    n = 8
    c_lib = 10
    c_road = 55
    roads = [
        [6, 4],
        [3, 2],
        [7, 1],
    ]

    result = roadsAndLibraries(n, c_lib, c_road, roads)
    print(result)  # Should be 80

    n = 1
    c_lib = 5
    c_road = 3
    roads = []

    result = roadsAndLibraries(n, c_lib, c_road, roads)
    print(result)  # Should be 5

    n = 2
    c_lib = 102
    c_road = 1
    roads = []

    result = roadsAndLibraries(n, c_lib, c_road, roads)
    print(result)  # Should be 204

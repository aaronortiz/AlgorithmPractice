#!/bin/python3

import math
import os
import random
import re
import sys


# ------------------------------------------------------------------------------
def sortDictByKeys(dict):
    newDict = {}
    keys = sorted(dict)
    for key in keys:
        newDict[key] = dict[key]
    return newDict


# ------------------------------------------------------------------------------
def classifyCitiesByRoadFreq(cities):
    roadsPerCity = {}
    citiesByRoadFreq = {}

    for road in cities:
        if road[0] in roadsPerCity:
            roadsPerCity[road[0]] += 1
        else:
            roadsPerCity[road[0]] = 1

        if road[1] in roadsPerCity:
            roadsPerCity[road[1]] += 1
        else:
            roadsPerCity[road[1]] = 1

    for city in roadsPerCity:
        if not roadsPerCity[city] in citiesByRoadFreq:
            citiesByRoadFreq[roadsPerCity[city]] = []
        citiesByRoadFreq[roadsPerCity[city]].append(city)

    return sortDictByKeys(citiesByRoadFreq)


# ------------------------------------------------------------------------------
def chooseCityWithMostConnections(citiesByRoadFreq):
    # dict is sorted in ascending order
    keys = list(citiesByRoadFreq.keys())
    greatestFrequency = citiesByRoadFreq[keys[-1]]
    fortunateCity = greatestFrequency.pop()
    return fortunateCity


# ------------------------------------------------------------------------------
def chooseCityWithFewestConnections(citiesByRoadFreq):
    # dict is sorted in ascending order
    for roads in citiesByRoadFreq:
        if len(citiesByRoadFreq[roads]) > 0:
            return citiesByRoadFreq[roads].pop()


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
def removeRoadFromCity(cities, city1, city2):
    if city1 in cities:
        if city2 in cities[city1]:
            cities[city1].remove(city2)

    if city2 in cities:
        if city1 in cities[city2]:
            cities[city2].remove(city1)

    return True


# ------------------------------------------------------------------------------
def removeCityAndConnections(connectedCities, unconnectedCities, city):
    return True


# ------------------------------------------------------------------------------
# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, roads):

    libRunningTotal = 0
    roadRunningTotal = 0
    unconnectedCities = getAllCities(roads)  # Gets list of all conections per city
    connectedCities = {}
    citiesByRoadFreq = classifyCitiesByRoadFreq(roads)

    print(n, c_lib, c_road, roads)
    print(unconnectedCities)

    while len(unconnectedCities) > 0:
        if c_lib < c_road:
            if roadRunningTotal + c_road >= libRunningTotal + c_lib:
                # Build a lib in city with least connections & remove city from list
                libRunningTotal += c_lib
                fortunateCity = chooseCityWithFewestConnections(citiesByRoadFreq)
                print("built lib for fortunate city", fortunateCity)
                removeCityAndConnections(
                    connectedCities, unconnectedCities, fortunateCity
                )

            else:
                # Build a road in city with most connections & remove city from list
                roadRunningTotal += c_road
                fortunateCity = chooseCityWithMostConnections(citiesByRoadFreq)
                print("built road for fortunate city", fortunateCity)

        else:
            if libRunningTotal + c_lib >= roadRunningTotal + c_road:
                # Build a road in city with most connections & remove city from list
                roadRunningTotal += c_road
                fortunateCity = chooseCityWithMostConnections(citiesByRoadFreq)
                print("built road for fortunate city", fortunateCity)
            else:
                # Build a lib in city with least connections & remove city from list
                libRunningTotal += c_lib
                fortunateCity = chooseCityWithFewestConnections(citiesByRoadFreq)
                print("built lib for fortunate city", fortunateCity)
                removeCityAndConnections(
                    connectedCities, unconnectedCities, fortunateCity
                )

        print("Road cost:", roadRunningTotal, "Lib cost:", libRunningTotal)
        print(unconnectedCities)

        return roadRunningTotal + libRunningTotal


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + "\n")

    fptr.close()

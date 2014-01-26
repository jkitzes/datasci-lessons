#!/usr/bin/env python

"""
Module containing functions to calculate mean number of sightings of a given
animal in a given sightings csv file.

Functions
---------
get_sightings - get number of sightings of focus animal in data set

"""

import sys
import matplotlib.mlab as ml
import numpy as np


def get_sightings(filename, focusanimal):
    """
    Get number of sightings of a focus animal in a data set.

    Parameters
    ----------
    filename : str
        Path to file containing sightings data
    focusanimal : str
        Name of focus animal (not case sensitive)

    Returns
    -------
    result : tuple
        Tuple containing total count of number of focus animal seen and mean
        count of individuals per sighting event.

    Notes
    -----
    Data file must be csv format with Animal and Count columns containing
    animal name and count of individuals per sighting, respectively.

    """

    # Load table
    tab = ml.csv2rec(filename)

    # Standardize capitalization of focusanimal
    focusanimal = focusanimal.capitalize()

    # Find number of records and total count of animals seen
    isfocus = (tab['animal'] == focusanimal)
    totalrecs = np.sum(isfocus)

    if totalrecs == 0:
        meancount = 0
    else:
        meancount = np.mean(tab['count'][isfocus])

    # Return num of records and animals seen
    return totalrecs, meancount


def get_sightings_loop(filename, focusanimal):

    # Load table
    tab = ml.csv2rec(filename)

    # Standardize capitalization of focusanimal
    focusanimal = focusanimal.capitalize()

    # Loop through all records, countings recs and animals
    totalrecs = 0
    totalcount = 0
    for rec in tab:
        if rec['animal'] == focusanimal:
            totalrecs += 1
            totalcount += rec['count']

    meancount = totalcount/totalrecs

    # Return num of records and animals seen
    return totalrecs, meancount

if __name__ == '__main__':
    #print sys.argv
    filename = sys.argv[1]
    focusanimal = sys.argv[2]
    print get_sightings(filename, focusanimal)

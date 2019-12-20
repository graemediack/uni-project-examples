# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:18:46 2018

@author: graeme
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import regex as re
from operator import itemgetter
import collections
import csv
import pandas as pd
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

#source = 'DorianGray.txt'
#source = 'Metamorphosis.txt'
source = 'NewScientist_JoshuaSokol_LeakingUniverse_May2017.txt'
#Read in data/text file, replacing new lines with spaces
with open(source, 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
with open('stoplist.txt', 'r') as myfile:
    stoplist=myfile.read().split('\n')

rmList = []

#create dataframe for graph metrics

indexMet = ['density','ClustCoeff','triadic_closure','diameter','aveShortPath']
graphMetrics = pd.DataFrame(index=indexMet)
indexT20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
degreeTop20 = pd.DataFrame(index=indexT20)
evectorTop20 = pd.DataFrame(index=indexT20)
btwnnessTop20 = pd.DataFrame(index=indexT20)

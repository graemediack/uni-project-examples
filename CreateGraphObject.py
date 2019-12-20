# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:22:59 2018

@author: graeme
"""
####
#Assuming CleanTextObject.py has been run
####

def create_graph(name,text,rmList=[]):
    #Remove all instances in rmList in original text
    def sub(m):
        return '' if m.group() in s else m.group()
    #convert rmList to set for use in sub
    s = set(rmList)
    #set regular expression for removing rmList
    regex1 = r'\w+'
    #set regex to remove double spaces
    regex2 = r'  '
    #apply regex substitutions
    dataTemp = re.sub(regex1, sub, text)
    dataTemp2 = re.sub(regex2,' ',dataTemp)
    #perform split into sentences
    dataTemp3 = dataTemp2.split('. ')
    #dataTemp = filter(lambda a: a != '', dataTemp)
    globals()[name] = nx.Graph()
    #create a path for each line of text
    for line in dataTemp3:
        globals()[name].add_path(line.split(' '))
    if '' in globals()[name]:
        globals()[name].remove_node('')
        print('WARNING: empty string nodes detected!')
        print('These have been removed, but this')
        print('could signify unrepresentative edges.')
    #collect a list of isolated vertices...
    isolatedVertices = list(nx.isolates(globals()[name]))
    #... and remove them. One word sentences are not relevant.
    for isol in isolatedVertices:
        globals()[name].remove_node(isol)
    #remove self loops, these occur when words are repeated for emphasis
    #such as "very, very small...", or by editing errors
    globals()[name].remove_edges_from(nx.selfloop_edges(globals()[name]))

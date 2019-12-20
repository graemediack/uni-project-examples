# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:04:03 2018

@author: graeme
"""

runfile('InitialiseLibraryAndImportText.py')
runfile('CleanTextObject.py')
runfile('CreateGraphObject.py')
runfile('PlotDegreeDist.py')
runfile('metricsdef.py')

userinput = 'start'
while userinput != '':
    print(graphMetrics.columns)
    userinput = input('Graph Name: ')
    if userinput != '':
        create_graph(userinput,data,rmList)
        plot_graph(globals()[userinput])
        metrics(globals()[userinput],userinput)
        x = 'temp'
        while x != '':
            x = input('Enter a word to pass to stoplist: ')
            if x != '':
                rmList.append(x)
            else:
                break
    else:
        break

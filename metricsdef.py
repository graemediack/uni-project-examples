# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:35:42 2018

@author: graeme
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 22:39:26 2018

@author: graeme
"""
#Function to output a number of metric of a given Graph G
def metrics(G,strG):
    densityG = nx.density(G)
    ClustCoeff = nx.average_clustering(G)
    if nx.info(G).split('\n')[1].split(' ')[1] == 'Graph':
        triadic_closure = nx.transitivity(G)
    else:
        triadic_closure = 0
        
    if not nx.is_connected(G):
        components = nx.connected_components(G)
        largest_component = max(components,key=len)
        Gsub = G.subgraph(largest_component)
        diameter = nx.diameter(Gsub)
        aveShortPath = nx.average_shortest_path_length(Gsub)
        degree_dict = dict(Gsub.degree(Gsub.nodes()))
    else:
        diameter = nx.diameter(G)
        aveShortPath = nx.average_shortest_path_length(G)
        degree_dict = dict(G.degree(G.nodes()))
        
    sorted_degree = sorted(degree_dict.items(),key=itemgetter(1),reverse=True)
    
    if nx.info(G).split('\n')[1].split(' ')[1] == 'Graph':
        eigenvector_dict = nx.eigenvector_centrality(G)
        nx.set_node_attributes(G,eigenvector_dict,'eigenvector')
        sorted_eigenvector = sorted(eigenvector_dict.items(),key=itemgetter(1),reverse=True)
    else:
        sorted_eigenvector = []
    
    betweenness_dict = nx.betweenness_centrality(G)
    nx.set_node_attributes(G,betweenness_dict,'betweenness')
    sorted_betweenness = sorted(betweenness_dict.items(),key=itemgetter(1),reverse=True)
    
    measures = [densityG,nx.average_clustering(G),triadic_closure,diameter,aveShortPath]
    degree = sorted_degree[:20]
    evector = sorted_eigenvector[:20]
    betweenness = sorted_betweenness[:20]
    graphMetrics[strG] = measures
    degreeTop20[strG] = degree
    evectorTop20[strG] = evector
    btwnnessTop20[strG] = betweenness
    print(sorted_degree[:50])
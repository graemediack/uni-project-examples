# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 22:39:26 2018

@author: graeme
"""
#function to create some informative plots

def plot_graph(G):
    
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*sorted(degreeCount.items()))
    sumcnt = sum(cnt)
    cnt = list(cnt)
    for x in range(len(cnt)):
        cnt[x] = float(cnt[x])/sumcnt
    cnt = tuple(cnt)
    
    fig, ax = plt.subplots()
    plt.loglog(deg, cnt)
    plt.ylabel("P(k)")
    plt.xlabel("degree k")
    
    # draw graph in inset
    plt.axes([0.4, 0.4, 0.5, 0.5])
    Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
    pos = nx.spring_layout(G)
    plt.axis('off')
    nx.draw_networkx_nodes(G, pos, node_size=20)
    nx.draw_networkx_edges(G, pos, alpha=0.4)
    
    plt.show()
    
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')
    #plt.title("Degree Histogram")
    plt.ylabel("P(k)")
    plt.xlabel("degree k")
    #ax.set_xticks([d + 0.4 for d in deg])
    #ax.set_xticklabels(deg)
    
    # draw graph in inset
    plt.axes([0.4, 0.4, 0.5, 0.5])
    Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
    pos = nx.spring_layout(G)
    plt.axis('off')
    nx.draw_networkx_nodes(G, pos, node_size=20)
    nx.draw_networkx_edges(G, pos, alpha=0.4)
    
    plt.show()
    
    #Identify largest k-core with nodes
    #x = 1
    #k = 0
    #while x != 0:
    #    k += 1
    #    x = len(nx.k_core(G,k))
    k = max(nx.core_number(G).values())
    print('Largest k is',k)
    #Plotting k-cores
    options = {
        'node_color': 'red',
        'node_size': 20,
        'edge_color': 'grey',
        'width': 1,
        }
    if k == 6:
        plt.subplot(321,title='1-core')
        nx.draw(nx.k_core(G,1),**options)
        plt.subplot(322,title='2-core')
        nx.draw(nx.k_core(G,2),**options)
        plt.subplot(323,title='3-core')
        nx.draw(nx.k_core(G,3),**options)
        plt.subplot(324,title='4-core')
        nx.draw(nx.k_core(G,4),**options)
        plt.subplot(325,title='5-core')
        nx.draw(nx.k_core(G,5),**options)
        plt.subplot(326,title='6-core')
        nx.draw(nx.k_core(G,6),**options)
        
        plt.show()
    elif k == 5:
        plt.subplot(321,title='1-core')
        nx.draw(nx.k_core(G,1),**options)
        plt.subplot(322,title='2-core')
        nx.draw(nx.k_core(G,2),**options)
        plt.subplot(323,title='3-core')
        nx.draw(nx.k_core(G,3),**options)
        plt.subplot(324,title='4-core')
        nx.draw(nx.k_core(G,4),**options)
        plt.subplot(325,title='5-core')
        nx.draw(nx.k_core(G,5),**options)
        
        plt.show()
        
    elif k == 4:
        plt.subplot(221,title='1-core')
        nx.draw(nx.k_core(G,1),**options)
        plt.subplot(222,title='2-core')
        nx.draw(nx.k_core(G,2),**options)
        plt.subplot(223,title='3-core')
        nx.draw(nx.k_core(G,3),**options)
        plt.subplot(224,title='4-core')
        nx.draw(nx.k_core(G,4),**options)
        
        plt.show()
    
    elif k == 3:
        plt.subplot(221,title='1-core')
        nx.draw(nx.k_core(G,1),**options)
        plt.subplot(222,title='2-core')
        nx.draw(nx.k_core(G,2),**options)
        plt.subplot(223,title='3-core')
        nx.draw(nx.k_core(G,3),**options)
        
        plt.show()

    elif k == 2:
        plt.subplot(121,title='1-core')
        nx.draw(nx.k_core(G,1),**options)
        plt.subplot(122,title='2-core')
        nx.draw(nx.k_core(G,2),**options)
        
        plt.show()

    pos=nx.spring_layout(nx.k_core(G,k))
    nx.draw(nx.k_core(G,k),pos,**options)
    nx.draw_networkx_labels(nx.k_core(G,k),pos,font_color='k')
    
    plt.show()
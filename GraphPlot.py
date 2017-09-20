import matplotlib.pyplot as plt
import networkx as nx
import settings
import GlobalGraph
##########################################
def plot_Graph(figname):
    color_black = []
    color_red = []
    for i in range(0,len(settings.nodesList)):
        
        if settings.nodesList[i].node_state == 0:
            color_black.append(settings.nodesList[i].node_name)
        else:
            color_red.append(settings.nodesList[i].node_name)

    labels={}
    for i in range(0,len(settings.nodesList)):
                   labels[i]=settings.nodesList[i].node_name
    
    pos = nx.get_node_attributes(GlobalGraph.G,'pos')
    plt.figure(figsize=(10,10))
    
    nx.draw_networkx_nodes(GlobalGraph.G,pos,
                   nodelist=color_red,
                   node_color='red',
                   node_size=300,
               alpha=0.8)
    nx.draw_networkx_nodes(GlobalGraph.G,pos,
                   nodelist=color_black,
                   node_color='black',
                   node_size=300,
               alpha=0.8)

    nx.draw_networkx_edges(GlobalGraph.G, pos)
    nx.draw_networkx_labels(GlobalGraph.G,pos,labels,font_size=16)
    
    plt.axis('off')
    plt.savefig(str(figname)+'.png')
    plt.show

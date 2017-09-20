import settings
import GlobalGraph
import networkx as nx
import random

from set_class_to_nodes import set_class_to_nodes as sctn

import set_active_state as sas

def mobility_of_node(n,step):
    
    pos = nx.get_node_attributes(GlobalGraph.G,'pos')

    # check if they "n" node is mobile nodes and if it is move it a step
    #radomly
    #After this, update the pos and the graph about the new position of the node
    #and return the updated graph.
    b = 0
    order=20
    x,y = pos[n][0],pos[n][1]
    for i in range(0,len(settings.nodesList)):
        if settings.nodesList[i].node_name == n:
            if settings.nodesList[i].mobility_class == "mobile":
                  
                
                
                while b == 0:
                    new = random.randint(1,4)
                
                    if new == 1 and x+step <= order and x+step >= -order:
                        x = x+step
                        b=1
                    elif new == 2 and x+step <= order and x+step >= -order:
                        y = y + step
                        b=1
                    elif new ==3 and x+step <= order and x+step >= -order:
                        x = x-step
                        b=1
                    elif x+step <= order and x+step >= -order:
                            y = y-step
                            b=1
                    else:
                        print("very big step!!")
                        b=1
                            
                pos[i][0]=x
                pos[i][1]=y
                #print("(Function) pos[",n,"] is:",pos[i][0],pos[i][1])
            #####################################
                nx.set_node_attributes(GlobalGraph.G, i, pos)
            
    ####################################
   
    
 

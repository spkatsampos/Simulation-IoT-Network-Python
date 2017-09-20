import networkx as nx
import GlobalGraph
import settings
#######################################################################

def find_neighbors(node):
    
    pos = nx.get_node_attributes(GlobalGraph.G,'pos')
    R=0.2
    
    for i in range(0,len(settings.nodesList)):
        if node != settings.nodesList[i].node_name and settings.nodesList[i].node_state == 1:
            #print("nodes: ",i,"-",node,"are differnet")
            eucledian_distance = ((pos[settings.nodesList[i].node_name][0]-pos[node][0])**2)+((pos[settings.nodesList[i].node_name][1]-pos[node][1])**2)
            if eucledian_distance <= R**2:
                #print("the nodes:",i,"-",node," are neigbors")
                #HERE I SHOULD INCLUDE SOME DELAY to the source (spend some ms for transmition 

                res = send_msg("Hello",node,settings.nodesList[i].node_name,R)
                if res:
                    GlobalGraph.G.add_edge(node,res)
                    #print("add the edge",node,"-",res)


######################################################################

######################################################################

######################################################################
def send_msg(message ,source,destination,R):
    pos = nx.get_node_attributes(GlobalGraph.G,'pos')
    for i in range(0,len(settings.nodesList)):
        if settings.nodesList[i].node_name == destination:
                if settings.nodesList[i].node_state == 1:
                #response to the message
               
                    return destination    


#######################################################################

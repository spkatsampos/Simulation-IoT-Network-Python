import settings
import GlobalGraph
import packets
import numpy as np
import networkx as nx
import copy
import random

def Broadcast_Packet(n):#node the node who has the buffer
    neigbors=[]
    neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)#list the neighbors of the current time
    #print("I am in FORWARD and I am the node:",settings.nodesList[n].node_name,"my neighboors:",neighbors)
    flag=0
    if settings.nodesList[n].node_buffer_packets and neighbors: #and if it has packet to its queue and there exists neighbors (active)
        fwrd_msg = copy.deepcopy(settings.nodesList[n].node_buffer_packets[0])#take the first item of the list/buffer of the node
            ##############
        #Check if the packet has passed from some of your neighbors and exclude
        #them drom the transmition.
        fwrd_msg.previous_node(settings.nodesList[n].node_name)
        fwrd_msg.add_node(settings.nodesList[n].node_name) #put the current node to the list of nodes

        #print("transmition from",settings.nodesList[n].node_name,"to: ",neighbors)
        for i in neighbors:
            if i not in fwrd_msg.node_list: 
                #print("I am the node:",i,"and I have packet to networkbuffer for me")
                fwrd_msg.nextnode = i #put the new destination           
                fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
                #print("I am:",settings.nodesList[n].node_name,"and I sent the packet to:",i)
                #print("With nextnode:",fm.nextnode,"and Timestamp:", fm.timestamp," and previousnode: ",fm.previousnode)
                settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
                flag=1
      
        '''
        #append the packet which include all the necessary fields
        #to the networkbuffer so as in the function receive
        #the nodes can understand which packets are for them
        '''
        #######################################################################
        if flag==1:# if the packet has been sent at least in one node remove it from the queue
            #print("Forward --I am the:",settings.nodesList[n].node_name," and I remove from my queue the packet:",settings.nodesList[n].node_buffer_packets[0].msg)
            settings.nodesList[n].node_buffer_packets.pop(0)#remove the item from the list.
#######################################################################################################################################################
#######################################################################################################################################################
def Multicast_Packet(n):
    neigbors=[]
    neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)

    flag=0
    if settings.nodesList[n].node_buffer_packets and neighbors: #and if it has packet to its queue and there exists neighbors (active)
        fwrd_msg = copy.deepcopy(settings.nodesList[n].node_buffer_packets[0])
        fwrd_msg.previous_node(settings.nodesList[n].node_name)
        fwrd_msg.add_node(settings.nodesList[n].node_name) #put the current node to the list of nodes


        if fwrd_msg.destination in neighbors:
            fwrd_msg.nextnode = fwrd_msg.destination #put the new destination           
            fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
            settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
            flag=1
        else:
            multicast=[]
            if len(neighbors) > 1:
                for i in range(0,int((len(neighbors)*0.5))):
                    node = random.choice(neighbors)
                    multicast.append(node)
                    neighbors.remove(node)
            else:
                multicast = neighbors[:]

            for i in multicast:
                    
                    fwrd_msg.nextnode = i #put the new destination           
                    fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
                    settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
                    flag=1
           #######################################################################
        if flag==1:# if the packet has been sent at least in one node remove it from the queue
            #print("Forward --I am the:",settings.nodesList[n].node_name," and I remove from my queue the packet:",settings.nodesList[n].node_buffer_packets[0].msg)
            settings.nodesList[n].node_buffer_packets.pop(0)#remove the item from the list.


#######################################################################################################################################################
#######################################################################################################################################################

def Multicast_Check_Packet(n):
    neigbors=[]
    neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)

    flag=0
    if settings.nodesList[n].node_buffer_packets and neighbors: #and if it has packet to its queue and there exists neighbors (active)
        fwrd_msg = copy.deepcopy(settings.nodesList[n].node_buffer_packets[0])
        fwrd_msg.previous_node(settings.nodesList[n].node_name)
        fwrd_msg.add_node(settings.nodesList[n].node_name) #put the current node to the list of nodes

        

        if fwrd_msg.destination in neighbors:
            fwrd_msg.nextnode = fwrd_msg.destination #put the new destination           
            fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
            settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
            flag=1
        else:
            multicast=[]
            if len(neighbors) > 1:
                for i in range(0,int((len(neighbors)*0.5))):
                    node = random.choice(neighbors)
                    multicast.append(node)
                    neighbors.remove(node)
            else:
                multicast = neighbors[:]


    ########################################################################
            for i in multicast:
                if i not in fwrd_msg.node_list: #If the node has already passed from the node not send    
                    fwrd_msg.nextnode = i #put the new destination           
                    fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
                    settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
                    flag=1
    #######################################################################
        if flag==1:# if the packet has been sent at least in one node remove it from the queue
            #print("Forward --I am the:",settings.nodesList[n].node_name," and I remove from my queue the packet:",settings.nodesList[n].node_buffer_packets[0].msg)
            settings.nodesList[n].node_buffer_packets.pop(0)#remove the item from the list.

    
def Op_Multicast_Packet(n,num_of_nodes):#node the node who has the buffer
    neigbors=[]
    neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)

    flag=0
    if settings.nodesList[n].node_buffer_packets and neighbors: #and if it has packet to its queue and there exists neighbors (active)
        fwrd_msg = copy.deepcopy(settings.nodesList[n].node_buffer_packets[0])
        fwrd_msg.previous_node(settings.nodesList[n].node_name)
        fwrd_msg.add_node(settings.nodesList[n].node_name) #put the current node to the list of nodes

        
        if fwrd_msg.destination in neighbors:
            fwrd_msg.nextnode = fwrd_msg.destination #put the new destination           
            fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
            settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
            flag=1
        else:
            multicast=[]
            if len(neighbors) > num_of_nodes:
                for i in range(0,num_of_nodes):
                    node = random.choice(neighbors)
                    multicast.append(node)
                    neighbors.remove(node)
            else:
                multicast = neighbors[:]


    ########################################################################
            for i in multicast:
                if i not in fwrd_msg.node_list: #If the node has already passed from the node not send    
                    fwrd_msg.nextnode = i #put the new destination           
                    fwrd_msg.set_timestamp(np.random.uniform(0, 10**(-6)))#put timestamp 
                    settings.networkbuffer.append(copy.deepcopy(fwrd_msg))#add to the network buffer the message(s)
                    flag=1
    #######################################################################
        if flag==1:# if the packet has been sent at least in one node remove it from the queue
            #print("Forward --I am the:",settings.nodesList[n].node_name," and I remove from my queue the packet:",settings.nodesList[n].node_buffer_packets[0].msg)
            settings.nodesList[n].node_buffer_packets.pop(0)#remove the item from the list.

    

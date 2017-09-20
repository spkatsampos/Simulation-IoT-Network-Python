#Produce a packet to a source...

from packets import Packets
import numpy as np
import settings
import copy

def produce_packet(source,destination,msg,seq_number):
    
    #PRODUCE A PACKET
    flag = 0
    packet=Packets(source,destination,msg,seq_number)
    #packet.add_node(source)
    #packet.set_timestamp(np.random.uniform(0.1, 10**(-20)))
    #packet.previous_node(source)
    #print(packet.source,packet.timestamp)
    #now I have a packet
    #put the message to the node's buffer...
    
    for n in range(0,len(settings.nodesList)):
        if settings.nodesList[n].node_state == 1 and settings.nodesList[n].node_name == packet.source:
            #add to the node buffer the packet.
            #print("I am the:",settings.nodesList[n].node_name," and I am waked up")
            flag = settings.nodesList[n].add_to_buffer(copy.copy(packet))
             
            if flag == -1:
                print("the packet was rejected")
           # else:
              #  print("I am the",settings.nodesList[n].node_name ,"and I put the packet into my buffer")
                #print("node name",settings.nodesList[n].node_name,"messega on buffer",settings.nodesList[n].node_buffer_packets[0].msg)
    return flag

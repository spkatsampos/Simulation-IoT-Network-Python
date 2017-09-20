import networkx as nx
import matplotlib.pyplot as plt
from set_class_to_nodes import set_class_to_nodes as sctn
import settings
import GlobalGraph
import set_active_state as sas
import GraphPlot
import NetworkAnimation
import FindNeighbors
from packets import Packets
import numpy as np
import Forward_packet as fp
import random
import produce_packet as pp
import Receive as rp
import RandomWalk as rw
import reduce_lifetime as rlt
import traffic as tf
import sortglobalbuffer as sgb
import produce_packet as pp
import copy
import os
import csv   
import d_MINCUT as dmc
'''
SETINGS
model : 1. Broadcast
        2. Multicast
        3. Multicast_Check
        4. Op_Multicast
'''
model = 4
######################################################
'''
Traffic : tfc = 20 means 20 packets per X - timeslot.
'''
tfc = 2
X_slots = 200
######################################################


##################################    
##################################
settings.init()   # Call only once / make the global variables.
GlobalGraph.init()
##################################
##################################

GlobalGraph.G = nx.read_gml('network100.gml') #load the graph

##REMOVE ALL EDFES
for k in range(0,len(settings.nodesList)):
    for l in range(0,len(settings.nodesList)):
        if  GlobalGraph.G.has_edge(k,l):
            GlobalGraph.G.remove_edge(k,l)

#HERE I have only nodes in the space

settings.nodesList = sctn.set_nodes_specifications(GlobalGraph.G) #set specifications to nodes
sas.set_active_state(90) #state of the nodes (90% active-10% inactive)
#######################################################
#######################################################



for b in range(0,5):
    newpath = 'Data\\'+str(b)
    if not os.path.exists(newpath):
        os.makedirs(newpath)


    #produce traffic at the first time slot
    
    #for X time-slots

    for i in range(0,X_slots):
        print("----------Time-Slot:",i,"------------")
        #produce traffic at every timeslot
        if i < (X_slots - 51):
            #if i%2 == 0:
                tf.traffic(tfc,i,b)
            
        
        del settings.networkbuffer[:] #Clean the network buffer


        
        ##REMOVE ALL EDFES at the start ( node doesn't have info about neighboors - no memory of graph)
        for k in range(0,len(settings.nodesList)):
            for l in range(0,len(settings.nodesList)):
                if  GlobalGraph.G.has_edge(k,l):
                    GlobalGraph.G.remove_edge(k,l)
        
        #The mobile nodes --randomwalk 
        for n in range(0,len(settings.nodesList)):
            rw.mobility_of_node(n,0.1)
            
        # I have to call neighbors in order to make the possible connections  
        
        #############################################
        #After this, I have to find neighbors for active nodes using Findneighbors
        for n in range(0,len(settings.nodesList)):
            if settings.nodesList[n].node_state == 1:
                FindNeighbors.find_neighbors(settings.nodesList[n].node_name)
        #############################################
        #REDUCE THE LIFETIME of all the packets in the buffers of nodes
        rlt.reduce_lifetime(2,i) #reduce every time slot the lifetime - 2 --> life of packet is 50 time slots.

        #To this point, (in every time slot) every node know their neighbors and thus
        # it can send a packet or receive a packet (or both)

       
        #1) Send -->
        #FORWORD HERE -- NETWORK BUFFER
        print("------------SEND PROCESS-------------")
        for w in range(0,5): # 5 - Send every active node 
            for n in range(0,len(settings.nodesList)):
                if model == 1:
                    fp.Broadcast_Packet(n)
                if model == 2:
                    fp.Multicast_Packet(n)
                if model == 3:
                    fp.Multicast_Check_Packet(n)
                if model == 4:
                    fp.Op_Multicast_Packet(n,4) #4 - number of nodes to do forward
            
    
        #short global bufffer (based on the timestapm -- correct order of sending
        settings.networkbuffer = sorted(settings.networkbuffer, key=lambda Packets: Packets.timestamp)
         

        
        #2) Receive <--
        print("------------RECEIVE PROCESS-------------")
        for n in range(0,len(settings.nodesList)):
            rp.Receive(n,i,b)
        
        


        #GraphPlot.plot_Graph("slot"+str(i))   
        #NetworkAnimation.animate()

        settings.graphlist.append(copy.deepcopy(GlobalGraph.G))
        #FINISH OF TIME SLOT - SET DIFFERENT STATE FOR THE NEXT TIME SLOT 
        sas.set_active_state(90) #state of the nodes (80% active-20% inactive)

    ########################################################################

  
    #count the proportion of successful transmissions and store it in a file 


    num_lines = sum(1 for line in open("Data\\"+str(b)+"\\Network_LogFile.txt"))
    number_of_packet = sum(1 for line in open("Data\\"+str(b)+"\\Traffic_LogFile.txt"))
    print("From the ",number_of_packet, "that was sent,arrived only:", num_lines)
    print("Proportion of successful transmitions: ",num_lines/number_of_packet )

    f = open('Statistics.txt','a+')
    f.write("From the: \t"+str(number_of_packet)+"\t that was sent,arrived only:\t"+str(num_lines)+"\t Proportion of successful transmitions:\t "+str(num_lines/number_of_packet)+"\n")
    f.close()


    import csv   
    import d_MINCUT as dmc
    import d_MAXFLOW as dmf

    fs=open("Data\\"+str(b)+"\\Traffic_LogFile.txt","r") #sent packets
    fa=open("Data\\"+str(b)+"\\Network_LogFile.txt","r") #arrived packets
    sent = csv.reader(fs, delimiter='\t', skipinitialspace=True)
    arrive = csv.reader(fa, delimiter='\t', skipinitialspace=True)
    ar=[]
    for m in arrive:
        ar.append(str(m[5])+str(m[6])+str(m[7])+str(m[8])+str(m[9])+str(m[23]))

    for msg in sent:
        ms = str(msg[0])+str(msg[1])+str(msg[2])+str(msg[3])+str(msg[4])+str(msg[6])
        
        if ms not in ar:
            s=msg[1]
            d=msg[3]
            print(s,"-",d)
            
            if s and d:
                    S,delta = dmc.mincutd(settings.graphlist, int(s),int(d))
                    J = dmf.maxflow(settings.graphlist, int(s),int(d))
                    print("There exist : ",len(J)," Disjoint paths")
                    #if len(S) == 0:#This means that source and destination do not have a path.
                    fs = open("Data\\"+str(b)+"MINCUT_d.txt",'a+')
                    fs.write("S* for: \t"+str(s)+"-"+str(d)+"\n")
                    fs.write("d: "+str(delta)+"\n")
                    fs.write(str(S)+"\n")
                    fs.write("----------------------------------\n")
                    
                    ff = open("Data\\"+str(b)+"MAXFLOW_d.txt",'a+')
                    ff.write("J for: \t"+str(s)+"-"+str(d)+"\n")
                    ff.write("There exist : "+str(len(J))+" Disjoint paths:\n")
                    ff.write(str(J)+"\n")
                    ff.write("----------------------------------\n")

                    fn = open("Data\\"+str(b)+"MAXFLOW_d_num.txt",'a+')
                    fn.write(str(len(J))+"\n")
                    
                    fl = open("Data\\"+str(b)+"MINCUT_d_num.txt",'a+')                   
                    fl.write(str(delta)+"\n")
                   
                    
                    
            
    fs.close()
    fa.close()
    ff.close()
    fn.close()
    fl.close()

    rlt.reduce_lifetime(50,i) #reduce every time slot the lifetime - 50 --> life of packet is 50 time slots. Destroy all the packets in the buffers


    ##############################################################################
        #00 - op 2 nodes
    ##############################################################################
    
    newpath = 'Data\\'+str(b)+str(b)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

            
    for i in range(0,len(settings.graphlist)):#for every timeslot/time instant of graph
        GlobalGraph.G =settings.graphlist[i]
        ##########################################################
        #set active
        for n in range(0,len(settings.graphlist[i])):
            neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)
            if neighbors:
                 settings.nodesList[n].active_state(1) 
            else:
                 settings.nodesList[n].active_state(0)
        ##########################################################
        del settings.networkbuffer[:] #Clean the network buffer
        ##########################################################
        #traffic
        f1=open("Data\\"+str(b)+"\\Traffic_LogFile.txt","r")
        c1 = csv.reader(f1, delimiter='\t', skipinitialspace=True)
        s=[]#packet source
        d=[]#packet destination
        ts=[]# timeslot that packet was transmitted
        flag=-1
        for line in c1:
            s.append(int(line[1]))
            d.append(int(line[3]))
            ts.append(int(line[5]))
       
        ############################################################
        # Send the packets the same timeslots like the previous model 
        for intex in iter(range(0,len(ts))):
            if ts[intex] == i:
                flag = pp.produce_packet(s[intex],d[intex],"---MSG -> I am \t"+str(s[intex])+"\t and I send to\t"+str(d[intex])+"\t---",random.randint(1,100))
                if flag ==1:
                   print("---MSG -> I am \t"+str(s[intex])+"\t and I send to\t"+str(d[intex]))
                

        rlt.reduce_lifetime(2,i) #reduce every time slot the lifetime - 2 --> life of packet is 50 time slots.

        #1) Forward -->
        print("------------SEND PROCESS-------------")
        for w in range(0,5): # 5 - Send every active node 
            for n in range(0,len(settings.nodesList)):
                fp.Op_Multicast_Packet(n,2)
                

        #short global bufffer (based on the timestapm -- correct order of sending
        settings.networkbuffer = sorted(settings.networkbuffer, key=lambda Packets: Packets.timestamp)
        
        #2) Receive <--
        print("------------RECEIVE PROCESS-------------")
        for n in range(0,len(settings.nodesList)):
            rp.Receive(n,i,str(b)+str(b))
##############################################################################
        #000 - Multicast check
##############################################################################
    rlt.reduce_lifetime(50,i) #reduce every time slot the lifetime - 50 --> life of packet is 50 time slots. Destroy all the packets in the buffers

    newpath = 'Data\\'+str(b)+str(b)+str(b)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

            
    for i in range(0,len(settings.graphlist)):#for every timeslot/time instant of graph
        GlobalGraph.G =settings.graphlist[i]
        ##########################################################
        #set active
        for n in range(0,len(settings.graphlist[i])):
            neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)
            if neighbors:
                 settings.nodesList[n].active_state(1) 
            else:
                 settings.nodesList[n].active_state(0)
        ##########################################################
        del settings.networkbuffer[:] #Clean the network buffer
        ##########################################################
        #traffic
        f1=open("Data\\"+str(b)+"\\Traffic_LogFile.txt","r")
        c1 = csv.reader(f1, delimiter='\t', skipinitialspace=True)
        s=[]#packet source
        d=[]#packet destination
        ts=[]# timeslot that packet was transmitted
        flag=-1
        for line in c1:
            s.append(int(line[1]))
            d.append(int(line[3]))
            ts.append(int(line[5]))
       
        ############################################################
        # Send the packets the same timeslots like the previous model 
        for intex in iter(range(0,len(ts))):
            if ts[intex] == i:
                flag = pp.produce_packet(s[intex],d[intex],"---MSG -> I am \t"+str(s[intex])+"\t and I send to\t"+str(d[intex])+"\t---",random.randint(1,100))
                if flag ==1:
                   print("---MSG -> I am \t"+str(s[intex])+"\t and I send to\t"+str(d[intex]))
                

        rlt.reduce_lifetime(2,i) #reduce every time slot the lifetime - 2 --> life of packet is 50 time slots.

        #1) Forward -->
        print("------------SEND PROCESS-------------")
        for w in range(0,5): # 5 - Send every active node 
            for n in range(0,len(settings.nodesList)):
                fp.Op_Multicast_Packet(n,3)
                

        #short global bufffer (based on the timestapm -- correct order of sending
        settings.networkbuffer = sorted(settings.networkbuffer, key=lambda Packets: Packets.timestamp)
        
        #2) Receive <--
        print("------------RECEIVE PROCESS-------------")
        for n in range(0,len(settings.nodesList)):
            rp.Receive(n,i,str(b)+str(b)+str(b))

            

####################################################################################################################################################
##############################################################################
        #0000 - op 5
##############################################################################
    rlt.reduce_lifetime(50,i) #reduce every time slot the lifetime - 50 --> life of packet is 50 time slots. Destroy all the packets in the buffers
    newpath = 'Data\\'+str(b)+str(b)+str(b)+str(b)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

            
    for i in range(0,len(settings.graphlist)):#for every timeslot/time instant of graph
        GlobalGraph.G =settings.graphlist[i]
        ##########################################################
        #set active
        for n in range(0,len(settings.graphlist[i])):
            neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)
            if neighbors:
                 settings.nodesList[n].active_state(1) 
            else:
                 settings.nodesList[n].active_state(0)
        ##########################################################
        del settings.networkbuffer[:] #Clean the network buffer
        ##########################################################
        #traffic
        f1=open("Data\\"+str(b)+"\\Traffic_LogFile.txt","r")
        c1 = csv.reader(f1, delimiter='\t', skipinitialspace=True)
        s=[]#packet source
        d=[]#packet destination
        ts=[]# timeslot that packet was transmitted
        flag=-1
        for line in c1:
            s.append(int(line[1]))
            d.append(int(line[3]))
            ts.append(int(line[5]))
       
        ############################################################
        # Send the packets the same timeslots like the previous model 
        for intex in iter(range(0,len(ts))):
            if ts[intex] == i:
                flag = pp.produce_packet(s[intex],d[intex],"---MSG -> I am \t"+str(s[intex])+"\t and I send to\t"+str(d[intex])+"\t---",random.randint(1,100))
                if flag ==1:
                   print("---MSG -> I am \t"+str(s[intex])+"\t and I send to\t"+str(d[intex]))
                

        rlt.reduce_lifetime(2,i) #reduce every time slot the lifetime - 2 --> life of packet is 50 time slots.

        #1) Forward -->
        print("------------SEND PROCESS-------------")
        for w in range(0,5): # 5 - Send every active node 
            for n in range(0,len(settings.nodesList)):
                fp.Op_Multicast_Packet(n,5)
                

        #short global bufffer (based on the timestapm -- correct order of sending
        settings.networkbuffer = sorted(settings.networkbuffer, key=lambda Packets: Packets.timestamp)
        
        #2) Receive <--
        print("------------RECEIVE PROCESS-------------")
        for n in range(0,len(settings.nodesList)):
            rp.Receive(n,i,str(b)+str(b)+str(b)+str(b))

            
    del settings.graphlist[:]
################################################################################
'''
num_lines = sum(1 for line in open("Data\\"+str(b)+str(b)+"\\Network_LogFile.txt"))
number_of_packet = sum(1 for line in open("Data\\"+str(b)+str(b)+"\\Traffic_LogFile.txt"))
print("From the ",number_of_packet, "that was sent,arrived only:", num_lines)
print("Proportion of successful transmitions: ",num_lines/number_of_packet )

f = open("Data\\"+str(b)+str(b)+"Statistics.txt",'a+')
f.write("From the: \t"+str(number_of_packet)+"\t that was sent,arrived only:\t"+str(num_lines)+"\t Proportion of successful transmitions:\t "+str(num_lines/number_of_packet)+"\n")
f.close()

del settings.graphlist[:]
'''












                 

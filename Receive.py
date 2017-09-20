import settings
import GlobalGraph
import packets
import copy
import time
import os

def Receive(n,timeslot,folder):
    neigbors=[]
    neighbors = GlobalGraph.G.neighbors(settings.nodesList[n].node_name)#list the neighbors of the current time
    flag=0
    local_obj_packet_list=[]
    
    if settings.nodesList[n].node_state == 1: #if the node is active
        #print("###I am the:",settings.nodesList[n].node_name," and I am wake up to receive!###")
                
        #print("I am in RECEIVE and the node:",settings.nodesList[n].node_name,"is active")                
        ##############################################################################################
        ##############################################################################################
        #limit=0
        for obj_packet in settings.networkbuffer: #Listen the "channel" - all packets
            #if limit < 20:
            #print("---Object in network buffer")
            ##########################################################################################
                if obj_packet.destination == settings.nodesList[n].node_name and obj_packet.previousnode in neighbors:#if i am the destination and if the previous node is my neighbor
                    #print("I am Destination of a packet!!!")
                    #Check if it is in my memory
                    if settings.nodesList[n].node_memory:
                        count = 0
                        for p in settings.nodesList[n].node_memory:
                            if obj_packet == p:
                                #print("The node:<",settings.nodesList[n].node_name,"> has already received this packet --> Reject")
                                
                                f = open("Data\\"+str(folder)+"\\Network_LogFile_OtherPaths.txt",'a+')
                                f.write("\n"+str(obj_packet.msg)+"\t"+str(timeslot+1)+"\t"+str(obj_packet.node_list)+"\n")
                                f.close()
                                #settings.networkbuffer.remove(obj_packet)
                                #limit = limit+1
                                count = 1
                            
                        if count == 0: #if not exists in the memory
                            #print("I appended a packet in local_obj_packet_list")
                            local_obj_packet_list.append(copy.deepcopy(obj_packet)) #put the packet for me to a list
                            #limit = limit+1
                                #settings.networkbuffer.remove(obj_packet)
                  #If the packet has destination me -- put it in the local list to check for other - simutaneously with others etc
                  #  I will not put the packet to the buffer so it does not check if it exists in the buffer
                    else:
                        local_obj_packet_list.append(copy.deepcopy(obj_packet))
                        #limit = limit+1
                        #settings.networkbuffer.remove(obj_packet)
                      

                ###############################################################################################       
                else:
                    if obj_packet.nextnode == settings.nodesList[n].node_name and obj_packet.previousnode in neighbors:
                        #print("I am in RECEIVE / I am the node:<",settings.nodesList[n].node_name,"> and I have a packet to check and store in my queue and forward it")
                        ###########################################################################################
                                                        
                        ###############################################################################################
                        #check if I have it already to my buffer.
                        if settings.nodesList[n].node_buffer_packets:
                            for nbp in settings.nodesList[n].node_buffer_packets:
                                if obj_packet != nbp:
                                    local_obj_packet_list.append(copy.deepcopy(obj_packet))
                                    #limit = limit+1
                                    #settings.networkbuffer.remove(obj_packet)
                                    
                         # if the buffer is empty
                        else:
                            local_obj_packet_list.append(copy.deepcopy(obj_packet))#if the local buffe of node is empty - it means that I have to receive the packet
                            #limit = limit+1
                            #settings.networkbuffer.remove(obj_packet)
                
                #END --FOR EVERY PACKET OF THE NETWORKBUFFER

                        
        ################################################################################################
        ################################################################################################
        ################################################################################################
        ################################################################################################
     

        #INSIDE THE IF ACTIVE       
        #local_obj_packet_list_temp = local_obj_packet_list[:] #copy of the list
        templist=[]
        for i in local_obj_packet_list:
            if i not in templist:
                templist.append(copy.deepcopy(i))
            #else:
                #f = open('Error_LogFile','a+')
                #f.write("\n---Remove the packet <"+str(i.msg)+"> Because I Receive it from more nodes---")
          
        #TIMESTAMP
               
        for i in iter(range(0, len(templist))):
            for j in iter(range(0, len(templist))):
                if i!=j:
                    if templist[i].timestamp == templist[j].timestamp:
                        templist.remove(templist[j])
                        f = open("Data\\"+str(folder)+"\\Error_LogFile_Collision.txt",'a+')
                        f.write("\n---Remove the packet <"+str(p.msg)+"> due to  Collision &&&&&&&&&&&&&&&&&&")
                        f.close()
                        print("Timestamp remove")
		
       # print("===local_obj_packet_list size:",len(templist))
        if templist:
            flag = 3
            #print("The local_obj_packet_list has:",len(templist)," packets to store in my buffer")
            ##########################################################################################################################################
            for p in templist: #for all the elements of the local list that includes the packets that is for me
                if p.LifeTime<=0: #check the lifetime
                    flag=2
                    
                else: #if the lifetime is ok-->
                    
                    if p.destination == settings.nodesList[n].node_name:
                        #print("######I am the node:",settings.nodesList[n].node_name,"and I received the packet <<",p.msg,">> from the [",p.previousnode,"] successfully######")
                        f = open("Data\\"+str(folder)+"\\Network_LogFile.txt",'a+')
                        f.write(str(settings.nodesList[n].node_name)+"\t\t\t\t\t"+str(p.msg)+"\t\t\t\t\t"+str(len(p.node_list))+"\t\t\t\t"+str(timeslot+1)+"\t\t\t\t"+str(p.node_list)+"\t"+str(p.seq_number)+"\n")
                        f.close()
                        settings.nodesList[n].add_to_memory(copy.deepcopy(p))
                        #local_obj_packet_list.remove(p)
                        #time.sleep(1)
                    
                    elif p not in settings.nodesList[n].node_buffer_packets: #check if the packet exist in the buffer of node and if it is not...put it 
                        flag = settings.nodesList[n].add_to_buffer(copy.deepcopy(p))
                    else:
                        #print("RECEIVE -- remove ONE packet because I have it into my buffer")
                        flag=4

                #if flag == 1:
                    #f = open('Error_LogFile','a+')
                    #f.write("\n---RECEIVE -- A packet was written in the buffer of the node [",settings.nodesList[n].node_name,"]")
                if flag == 2:
                    f = open("Data\\"+str(folder)+"\\Error_LogFile.txt",'a+')
                    f.write("\n---Remove the packet <"+str(p.msg)+">  \tExpired packet")
                    f.close()
                if flag == 0:
                    f = open("Data\\"+str(folder)+"\\Error_LogFile.txt",'a+')
                    f.write("\n---Remove the packet <"+str(p.msg)+"> \tdue to  Buffer overflow of the node ",settings.nodesList[n].node_name,"---")
                    f.close()
                    #print("RECEIVE -- The flag say that I have no space in my node's buffer for this packet")
                if flag == 4:
                    f = open("Data\\"+str(folder)+"\\Error_LogFile.txt",'a+')
                    f.write("\n---Remove the packet <"+str(p.msg)+">, \tit Exists in the buffer---")
                    f.close()
                
        del templist
    del local_obj_packet_list
    
    

                        
                        
                        
                                                        
                        
                        
                        

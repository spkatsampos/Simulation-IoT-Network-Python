import packets
import settings

def reduce_lifetime(t,timeslot):# t-> time to reduce 

    for i in range(0,len(settings.nodesList)):
        if settings.nodesList[i].node_buffer_packets:
            for packet in settings.nodesList[i].node_buffer_packets:
                packet.LifeTime = packet.LifeTime - t

    
#check if inside the buffer some packets is expired - if yes -remove them
    for i in range(0,len(settings.nodesList)):
        if settings.nodesList[i].node_buffer_packets:
            for packet in settings.nodesList[i].node_buffer_packets:
                if packet.LifeTime < 1:
                    settings.nodesList[i].node_buffer_packets.remove(packet)
                    f = open('Error_LogFile.txt','a+')
                    f.write("\n---Remove the packet - \t<"+str(packet.msg)+">\t - due to LifeTime--- in timeslot:"+str(timeslot))
            
                

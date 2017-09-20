import packets
import settings
import produce_packet as pp
import random

def traffic(n,t,folder):# n -> how many packets 
    flag = 0
    no = 50
    f = open("Data\\"+str(folder)+"\\Traffic_LogFile.txt",'a+')
    f1 = open("Data\\"+str(folder)+"\\BufferOverflow.txt",'a+')
    #f2 = open("Data\\"+str(folder)+"\\Pairs.txt",'a+')
    #f.write("\n---Time Slot"+str(t)+"---")
    for i in range(0,n):
        nodes = list(range(no))
        source = random.choice(nodes)
        del nodes[nodes.index(source)] #remove from the list the source
        destination = random.choice(nodes)
        seq = random.choice([1,2,3,4,5,6,7,8,9])#???
        flag = pp.produce_packet(source,destination,"---MSG -> I am \t"+str(source)+"\t and I send to\t"+str(destination)+"\t---",seq)
        if flag == -1:
            f1.write("---MSG -> I am \t"+str(source)+"\t and I send to\t"+str(destination)+"\t--- Reject - Buffer Overflow in Traffic function\n")
        
        if flag == 1:
            f.write("---MSG -> I am \t"+str(source)+"\t and I send to\t"+str(destination)+"\t---\t"+str(t)+"\t"+str(seq)+"\n")
            #f2.write(str(source)+"---\t"+str(destination)+"\n")

    f.close()
    f1.close()

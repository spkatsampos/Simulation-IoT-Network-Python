file="Data"
folders=[]#["BF","MFR","MFCR","OMFCR"]
for i in folders:
    f = open(str(file)+"_"+str(i)+'_Statistics.txt','a+')
    f.write("Method :  "+i+"\n")
    for j in range(0,2):
        num_lines = sum(1 for line in open(str(file)+"\\"+str(i)+"\\"+str(j)+'\\Network_LogFile.txt'))
        number_of_packet = sum(1 for line in open(str(file)+"\\"+"OMFCR\\"+str(j)+"\\Traffic_LogFile.txt"))
        print("model: ",i)
        print("From the ",number_of_packet, "that was sent,arrived only:", num_lines)
        print("Proportion of successful transmitions: ",num_lines/number_of_packet )
        f.write("From the: \t"+str(number_of_packet)+"\t that was sent,arrived only:\t"+str(num_lines)+"\t Proportion of successful transmitions:\t "+str(num_lines/number_of_packet)+"\n")
    f.close()
                                                  



import math
import start
import blockreciever
import control
import sys 
def standard_dev(lists):
    avg = float(sum(lists))/len(lists)
    #print(avg)
    dev = []
    for x in lists:
        dev.append(x - avg)
        #print(dev)
    sqr = []
    
    for x in dev:
        sqr.append(x * x)
        
    #print(sqr)
    mean = sum(sqr)/len(sqr)
    #print(mean)
    standard_deviation = math.sqrt(sum(sqr)/(len(sqr)-1))    
    return standard_deviation


def getandprintstats(array_of_frames, array_of_thoroughput, array_of_seeds, array_of_input ):

    T = 5
    #Thoroughputstddev is probably correct
    
    Framestddev = standard_dev(array_of_frames)
    #Framestddev = numpy.std(arrayofframes)
    Thoroughputstddev = standard_dev(array_of_thoroughput)
    #Thoroughputstddev = numpy.stdev(arrayofthoroughput)   
    
    #standard deviation
    #standard deviation end
    
    
    Framesum=0
    
    
    for numofframes in (array_of_frames):
        Framesum = Framesum+numofframes
    
    Frameavg = Framesum/(len(array_of_frames))

    Thoroughputsum = 0
    for athoroughput in (array_of_thoroughput):
        Thoroughputsum = Thoroughputsum + athoroughput
    
    Thoroughputavg = Thoroughputsum/(len(array_of_thoroughput))

    Framec1 = float((Frameavg)-(2.776*(Framestddev/(math.sqrt(T)))))
    Framec2 = float((Frameavg)+(2.776*(Framestddev/(math.sqrt(T)))))

    Thoroughc1 = float((Thoroughputavg)-(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    Thoroughc2 = float((Thoroughputavg)+(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    
    #Thoroughc1 = float((Thoroughputavg)+(2.776*(Framestddev/(math.sqrt(len(T))))))
    #Thoroughc2 = (Thoroughputavg) + (2.776(float(Thoroughputstddev)/(math.sqrt(len(T)))))
  # Framestdev =  statistics.stdev(arrayofframes)

   #Throughputstdev =  statistics.stddev(arrayofthroughput)
    print(array_of_input)
    print("Frame stats:"+str(Frameavg)+" "+"("+ str(Framec1)+ "," + str(Framec2)+")")
    print("Thoroughput stats: "+str(Thoroughputavg)+" "+"("+ str(Thoroughc1)+ "," + str(Thoroughc2)+")")
    #sys.exit()

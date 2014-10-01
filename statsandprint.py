import numpy
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


def getandprintstats(arrayofframes, arrayofthoroughput, arrayofseeds, arrayofinput ):

    T = arrayofinput[5]
    Framestddev = standard_dev(arrayofframes)
    #Framestddev = numpy.std(arrayofframes)
    Thoroughputstddev = standard_dev(arrayofthoroughput)
    #Thoroughputstddev = numpy.stdev(arrayofthoroughput)   
    
    #standard deviation
    
    
    #standard deviation end
    
    
    Framesum=0
    
    
    for numofframes in (arrayofframes):
        Framesum = Framesum+numofframes
    
    Frameavg = Framesum/(len(arrayofframes))

    Thoroughputsum = 0
    for athoroughput in (arrayofthoroughput):
        Thoroughputsum = Thoroughputsum + athoroughput
    
    Thoroughputavg = Thoroughputsum/(len(arrayofthoroughput))

    Framec1 = float((Frameavg)-(2.776*(Framestddev/(math.sqrt(len(T))))))
    Framec2 = float((Frameavg)+(2.776*(Framestddev/(math.sqrt(len(T))))))

    Thoroughc1 = float((Thoroughputavg)-(2.776*(Thoroughputstddev/(math.sqrt(len(T))))))
    Thoroughc2 = float((Thoroughputavg)+(2.776*(Thoroughputstddev/(math.sqrt(len(T))))))
    
    #Thoroughc1 = float((Thoroughputavg)+(2.776*(Framestddev/(math.sqrt(len(T))))))
    #Thoroughc2 = (Thoroughputavg) + (2.776(float(Thoroughputstddev)/(math.sqrt(len(T)))))
  # Framestdev =  statistics.stdev(arrayofframes)

   #Throughputstdev =  statistics.stddev(arrayofthroughput)
    print(arrayofinput)
    print(str(Frameavg)+" "+"("+ str(Framec1)+ "," + str(Framec2)+")")
    print(str(Thoroughputavg)+" "+"("+ str(Thoroughc1)+ "," + str(Thoroughc2)+")")
    #sys.exit()

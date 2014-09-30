import numpy
import math
import start
import blockreciever
import control


def getandprintstats(arrayofframes, arrayofthoroughput, arrayofseeds, arrayofinput ):

    T = arrayofinput[5]
    #Framestddev = statistics.stdev(arrayofframes)
    Framestddev = numpy.std(arrayofframes)
    #Thoroughputstddev = statistics.stdev(arrayofthoroughput)
    #Thoroughputstddev = numpy.stdev(arrayofthoroughput)   
    
    standard_dev= math.sqrt(average(
    Framesum=0
    
    for numofframes in range(arrayofframes):
        Framesum = Framesum+numofframes
    
    Frameavg = Framesum/(len(arrayofframes))

    Thoroughputsum = 0
    for athoroughput in range(arrayofthoroughput):
        Thoroughput = Thoroughput + athoroughput
    
    Thoroughputavg = Thoroughputsum/(len(arrayofthoroughput))

    Framec1 = (Frameavg)-(2.776*(Framestddev/(math.sqrt(T))))
    Framec2 = (Frameavg)+(2.776*(Framestddev/(math.sqrt(T))))

    Thoroughc1 = (Thoroughputavg) - (2.776(Thoroughputstddev/(math.sqrt(T))))
    Thoroughc2 = (Thoroughputavg) + (2.776(Thoroughputstddev/(math.sqrt(T))))
  # Framestdev =  statistics.stdev(arrayofframes)

   #Throughputstdev =  statistics.stddev(arrayofthroughput)
    print(sys.argv)
    print(Frameavg+" "+"("+Framec1+","+Framec2+")")
    print(Thoroughputavg+" "+"("+Thoroughc1+","+ Thoroughc2+")")


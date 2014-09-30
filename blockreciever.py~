import time
import random
import start
import statsandprint
import control

def recievessnddetect(numberofbits, error, feedbacktime, seed, doparity):

    #return 1 if no need to transmit
    #returns 0 if needs to be retransmitted
    #the number of bits should already have beenpartitioned here
    instaerror = float(error)
    instaerrorcount = 0
    instadelay = int(feedbacktime)
    
    numberofpacketerror = 0

    paritycounter = 0
    checkflagcounter = 1
    while((checkflagcouunter == 1) && (doparity != 0)):
        #find the parity bits needed
        if(numberofbits >= 2**paritycounter):
            paritycounter++
        else:
            checkflagcounter = 0
    

    rnd = random.Random(seed)
    for x in range(0,numberofbits+paritycountchecker):
    #seed
        
        p = rnd.uniform(0,1)
        #p = random.uniform(0,1)
        if p > instaerror:
            numberofpacketerror = numberofpacketerror + 1

    time.sleep(instadelay)
if instaerror > 1:
    return 0

else:
    return paritycounter



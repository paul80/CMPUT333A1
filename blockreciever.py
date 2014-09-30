import time
import random
import start
import statsandprint
import control

def recievessnddetect(numberofbits, error, feedbacktime, seed, doparity):

    instaerror = float(error)
    instaerrorcount = 0
    instadelay = int(feedbacktime)
    
    numberofpacketerror = 0

    paritycounter = 0
    checkflagcounter = 1
    while((checkflagcouunter == 1) and (doparity != 0)):
        #find the parity bits needed
        if(numberofbits >= 2**paritycounter):
            paritycounter=paritycounter + 1
        else:
            checkflagcounter = 0
            doparity = 0
    

    rnd = random.Random(seed)
    for x in range(0,numberofbits+paritycountchecker):        
        p = rnd.uniform(0,1)
        #p = random.uniform(0,1)
        if p > instaerror:
            numberofpacketerror = numberofpacketerror + 1

    time.sleep(instadelay)
    
    if numberofpacketerror > 1:
    #returns 0 to retransmit the whole frame when this block fails
        return 0

    else:
    #block sent successfully
        return paritycounter



import time
import random
import start
import blockreciever
import statsandprint

#import start
#import recievesendchecker

def organizercontroll(A,K,F,e,seed):

    
    #return a test instance 
    #youve already checked from the caller that 0 == (F modulo K)
    sizeofpacket = int(F)
    numberofblock = int(K)
    biterrorprobability = float(e)
    instadelay = int(R*(10**(-7)))

    framecounter = 0
    successfulframecount = 0
    
    startinstancetime = time.time()

    #here we separate the frame into K blocks
    #if one of the blocks fails re-transmit the whole frame
    framesentfailed = 0
    while(framesentfailed == 0):
        blockfail = 0
        #do a blockfail ifstatement below
        for instanceblock in range(0,K):
            if(K == 0):
                successfullysend = recievesenddetect(F, biterrorprobability, instadelay, seed, 0)
                framecounter = framecounter + 1
                if (succesfullysend != 0):
                    successfulframecount = successfulframecount + 1
                else:
                    blockfail = 1
            else:
                sucessfullysend = recievesenddetect((F/K), biterrorprobability,instadelay,seed,1)
                framecounter = framecounter + 1
                if(successfulsend != 0):
                    successfulframecount = successfulframecout + 1
                else:
                    blockfail = 1
        if (blockfail == 0):
            framesentfailed = 1

    #ok we have an instance of a test
    #we start returning values
    endinstancetime= time.time()
    theinstancetime = endinstancetime - startinstancetime
    thoroughputinstance = ((K/F)+successfulsend)/(theinstancetime)
    return framecounter, successfulframecount, thoroughputinstance,seed

#a , b = somefunction()
#somefunction {return [a], [b]}
                    

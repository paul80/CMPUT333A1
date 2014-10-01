import time
import random
import start
import blockreciever
import statsandprint


def organizercontroll(A,K,F,e,seed):

    sizeofpacket = int(F)
    numberofblock = int(K)
    biterrorprobability = float(e)
    
    #the bit time is converted into seconds
    instadelay = int(A*(10**(-7)))

    framecounter = 0
    successfulframecount = 0
    
    startinstancetime = time.time()

    #here we separate the frame into K blocks
    #if one of the blocks fails re-transmit the whole frame
    framesentfailed = 0
    while(framesentfailed == 0): 
        #blockfail checks if any of the blocks failed
        blockfail = 0
        #iterate through all of the blocks
        for instanceblock in range(0,numberofblock):
            if(K == 0):
                successfullysend = blockreciever.recieve_send_detect(F, biterrorprobability, instadelay, seed, 0)
                framecounter = framecounter + 1
                if (succesfullysend != 0):
                    successfulframecount = successfulframecount + 1
                else:
                    #if any of the block fails the whole frame is resent
                    blockfail = 1
            else:
                #print(framesentfailed)
                successfullysend = blockreciever.recieve_send_detect((F/K), biterrorprobability,instadelay,seed,1)
                framecounter = framecounter + 1
                #print("successfullysend"+str(successfullysend)) == 0
                if(successfullysend != 0):
                    successfulframecount = successfulframecount + 1
                else:
                    #if any of the block fails the whole frame is resent                    
                    blockfail = 1
        #print("outsideforloop" )
        #print(blockfail) == 1
        #print(successfulframecount)==0
        if (blockfail == 0):
            #if all of the blocks are succefully sent exit the while loop
            framesentfailed = 1

    #ok we have an instance of a test
    #we start returning values
    endinstancetime= time.time()
    theinstancetime = endinstancetime - startinstancetime
    if (K==0):
        K=1
    #thoroughputinstance = ((K/F)*successfullysend)/(theinstancetime)
    thoroughputinstance = F*5/(theinstancetime)
    
    return framecounter, successfulframecount, thoroughputinstance,seed

#a , b = somefunction()
#somefunction {return [a], [b]}
                    

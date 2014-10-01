import time
import random
import start
import blockreciever
import statsandprint


def organizercontroll(A,K,F,e,R):

    global blockfail
    #ADD SEED LATER
    sizeofpacket = int(F)
    numberofblock = int(K)
    biterrorprobability = float(e)
    correct_frames=0
    
    #the bit time is converted into seconds
    instadelay = int(A*(10**(-7)))

    framecounter = 0
    
    successfulframecount = 0
    
    total_frames=0  #includes retransmissions/failed frames
    correct_frames=0
    startinstancetime = time.time()

    #here we separate the frame into K blocks
    #if one of the blocks fails re-transmit the whole frame
    
    count=R%F
    #frames is number of times to go through for loop R/F, amount of frames to send
    frames=R//F
    
    #print(R,F,frames)
    if (count!=0):
        frames+=1
    #print(frames)
    for i in range(frames):
        
        #framesentfailed=1
        #blockfail checks if any of the blocks failed
        blockfail = 0
        #iterate through all of the blocks of a frame
        for instanceblock in range(0,numberofblock):
            if(K == 0):
                successfullysend = blockreciever.recieve_send_detect(F, biterrorprobability, instadelay, R, 0)
                framecounter = framecounter + 1
                if (succesfullysend == 1):
                    successfulframecount = successfulframecount + 1
                else:
                    #if any of the block fails the whole frame is resent so blockfail is set to 1
                    blockfail = 1
            else:
                #print(framesentfailed)
                successfullysend = blockreciever.recieve_send_detect((F/K), biterrorprobability,instadelay,R,1)
                framecounter = framecounter + 1
                #print("successfullysend"+str(successfullysend)) == 0
                if(successfullysend != 0):
                    successfulframecount = successfulframecount + 1
                else:
                    #if any of the block fails the whole frame is resent                    
                    blockfail = 1
                    
        total_frames+=1
        #print("outsideforloop" )
        #print(blockfail) == 1
        #print(successfulframecount)==0
        if (blockfail == 0):
            #if all of the blocks are succefully sent exit the while loop and increment total frames by 1
            #framesentfailed = 0
            correct_frames+=1




    #ok we have an instance of a test
    #we start returning values
    endinstancetime= time.time()
    theinstancetime = endinstancetime - startinstancetime
    if (K==0):
        K=1
    #thoroughputinstance = ((K/F)*successfullysend)/(theinstancetime)
    thoroughputinstance = (F*correct_frames)/(theinstancetime)
   # print(frames)
    print(correct_frames, frames, correct_frames/frames)
    return total_frames, correct_frames/frames, thoroughputinstance,R


                    

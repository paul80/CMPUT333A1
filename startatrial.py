import sys
import argparse
import blockreciever
import control
import start
import statsandprint

#framecountercontainer = []
#succesfulframecontainer = []
#thoroughputcontainter = []
#seedinstancecounter = []


def instancetrial(syslist, seed):
    framecountercontainer = []
    succesfulframecontainer = []
    thoroughputcontainer = []

    bitssofar = 0
    #stopbit = int(syslist[5])
    #while(bitssofar < stopbit):

    #bitssofar = bitssofar + int(syslist[2]) 
    framecounter, succesfulframecount, thoroughputinstance, seed = control.organizercontroll(int(syslist[2]), int(syslist[3]), int(syslist[4]), float(syslist[4]), seed)

    #framecountercontainer.append(framecounter)
    #succesfulframecontainer.append(succesfulframecount)
    #thoroughputcontainer.append(thoroughputinstance)

    #countbits for thoroughput
    #getandprintstats()
    #printstuff


    

import sys
import argparse
import blockreciever
import control
import statsandprint
import startatrial

#start program here

def main():
    #prints what we want from the user
    print ("enter A K e R t respectively without commas separated by spaces +\n")
    print("A is feedback time in bit times")
    print("K is blocks\n")
    print("F is size of frame and K must be divisible by it\n")
    print("e is error in float \n")
    print("R is length of simulations +\n")
    print("t is trials +\n")
    print("any wrong input will ask you to reenter the inputs")
    
    y = 0
    x = 0
    while( y ==0):
        while (x ==0):
            parser = argparse.ArgumentParser()
            parser.add_argument("start", nargs = 6 )
            if ((len(sys.argv)==7)and((int(sys.argv[3])%(int(sys.argv[2])))==0)):
                print(sys.argv[1] +sys.argv[2]+sys.argv[3] +sys.argv[4] +sys.arg[5] +sys.arg[6])
                print('is this correct? ')
                print('enter 1 for true and 0 to re- enter new input')
                
                parser1 = argparse.ArgumentParser() 
                parser1.add_argument('start',  type=int,  nargs=1 )
                if(int(sys.argv[1]))==1:
                #exits while loop that asks for user input
                    x=1
                else:
                #stays in while loop that asks for user input
                    ('+\n redirecting... \n')
            else:
                #stays in while loop that asks for user input
                print("your arguments does not match our criteria please try again \n")

        #inside a while loop that starts a sample with 5 tests
        #these containers are for information regarding the output needed
        framecountercontainer=[]
        succesfulframecontainer = []
        throughputcontainer=[]
        seedinstancecontainer=[]
            
        #this is a sample iterating through instances of tests
        for testinstance in range(0, int(sys.arg[6])):
            seed = int(sys.argv[6+testinstance+1])
            framecounter, succesfulframecount, thoroughputinstance, seed = starttrial.instancetrial(sys.argv, seed)
            
            
            #adds information to the containers
            framecountercontainer.append(framecounter)
            succefulframecontainer.append(succesfulframecount)
            thoroughputcontainer.append(thoroughputinstance)
            seedinstancecontainer.append(seed)

        #prints stats needed
        statsandprint.getandprintstats(frameinstancecontainer, thoroughputcontainer, seedinstancecontainer, sys.argv)

        print('\n would you like to do a new test? \n')
        print('enter 0 for no and 1 for yes')
        #to string
        if(int(sys.argv[1]))==1:
            y = 0
        else:
            y = 1

        

        #youve indented these lines above
        #call divider here
        #start time here
        #convert bit time to seconds


if __name__ == "__main__":
    main()
import sys
import argparse
import blockreciever
import control
import statsandprint
import startatrial

if __name__ = __main__:

    print ("enter A K e R t respectively without commas separated by spaces +\n")
    print("A is feedback time in bit times")
    print("K is blocks +\n")
    print("F is size of frame +\n")
    print("e is error in float \n")
    print("R is length of simulations +\n")
    print("t is trials +\n")

    #F (modulo K) == 0 here
    while( y ==0):
        while (x ==0):
            parser = argparse.ArgumentParser()
            parser.add_argument("start", nargs = 6 )
            if ((len(sys.argv)==7)and((int(sys.argv[3])%(int(sys.argv[2])))==0)):
                #print(int(sys.argv[1]))
                #print(int(sys.argv[2]))
                #print(int(sys.argv[3]))
                #print(float(sys.argv[4]))
                #print(int(sys.arg[5]))
                #print(int(sys.arg[6]))                
                print(sys.arg)
                print('is this correct? ')
                print('enter 1 for true and 0 to re- enter new input')
                
                parser1 = argparse.ArgumentParser() 
                parser1.add_argument('start',  type=int,  nargs=1 )
                #or parser.parse_args(['start'])
                #args.start
                if(int(sys.argv[1]))==1:
                    x=1
                else:
                    ('+\n redirecting... \n')
            else:
                print("your arguments does not match our criteria please try again \n")

            #this is a sample containing 5 tests
            #so 5 tests
            framecountercontainer=[]
            succesfulframecontainer = []
            throughputcontainer=[]
            seedinstancecontainer=[]
            
            #this is a test
            for testinstance in range(0, int(sys.arg[6])):
                seed = int(sys.argv[6+testinstance+1])
                framecounter, succesfulframecount, thoroughputinstance, seed = starttrial.instancetrial(sys.argv, seed)
            
            
#                framecounter, succesfulframecount, throughputinstance, seed = control.organizercontroll(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
                framecountercontainer.append(framecounter)
                succefulframecontainer.append(succesfulframecount)
                thoroughputcontainer.append(thoroughputinstance)
                seedinstancecontainer.append(seed)

            getandprintstats(frameinstancecontainer, thoroughputcontainer, seedinstancecontainer, sys.argv)

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




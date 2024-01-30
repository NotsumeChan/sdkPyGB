import sys
import os
from output import *

#add flags to set if network is necessary
#if network add db


def main()-> None:
    arg = sys.argv

    match arg[0]:
        case "create":
            if arg[1] == "-N":
                #create a new project with network
                pass
            #create a new project
            pass

        case "build":
            #create a new exe (hopefully use numba to compile the code)
            pass

        case "run":
            folders = os.listdir()
            for a in folders:
                if arg[1] == a:
                    #run especific game
                    Run(a)

        case "clean":
            if arg[1] == "-A":
                #delete all games
                pass
            elif arg[1][0] != "-":
                #delete especific game
                pass 
            pass

        case "help":
            #show commands list
            pass

if "__main__" == __name__:
    main()
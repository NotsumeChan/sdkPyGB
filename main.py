import sys
import os
from output import *

#add flags to set if network is necessary
#if network add db


def main()-> None:
    arg = sys.argv
    arg = arg + [""] * (4 - len(arg))

    match arg[1]:
        case "create":
            if arg[3] == "-N":
                print(f"create {arg[2]} with network")
                #create game
                return
            print(f"create {arg[2]}")


        case "build":
            print(f"building {arg[2]}...")
            #build the game
            print("build complete")

        case "run":
            folders = os.listdir(os.getcwd() + "/games")
            for a in folders:
                if arg[2] == a:
                    print(f"building {arg[2]}...")
                    #build the game
                    print("build complete")
                    print(f"running {arg[2]}...")
                    Run(a)
                    break
            else:
                print("game not found")

        case "clean":
            if arg[2] == "-A":
                #delete all games
                pass
            elif arg[2][0] != "-":
                #delete especific game
                pass 
            pass

        case "help":
            print("""
create <name> [-N] : create a new game
build <name>       : build the game
run <name>         : run the game
clean <name>       : delete the game, if -A or no name is given, delete all games
help               : print help
""")
            pass

if "__main__" == __name__:
    main()
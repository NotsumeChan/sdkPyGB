from os import getcwd, listdir, remove
from shutil import copytree
from sys import argv

from output import *

#add flags to set if network is necessary
#if network add db

def main()-> None:
    arg = argv
    arg = arg + [""] * (4 - len(arg))
    current = getcwd()
    match arg[1]:
        case "create":
            if arg[3] == "-N":
                print("Network is not implemented yet")
                #print(f"crating {arg[2]} with network")
                #create game
            try:
                
                copytree(current + "/games/" + "Example", current + "/games/" + arg[2])
            except:
                print(f"game {arg[2]} already exists")
            
            print(f"create {arg[2]}")

        case "build":
            print("Not implemented yet")
            print(f"building {arg[2]}...")
            #build the game
            print("buil d complete")

        case "run":
            print("Not implemented yet")
            folders = listdir(current + "/games")
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
                #delete all games except Example adn Tutorial
                for a in listdir(current + "/games"):
                    if a not in ("Example","Tutorial"):
                        print(f"deleting {a}...")
                        remove(current + "/games/" + a)

            for a in listdir(current + "/games"):
                if arg[2].lower() == a.lower():
                    print(f"deleting {a}...")
                    remove(current + "/games/" + a)
                    break

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
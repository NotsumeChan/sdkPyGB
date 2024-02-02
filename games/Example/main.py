#libraries
import sys
import pygame    as py
from   time      import time
#---------

#local files
from Instancias import *
#-----------

#Home Screen
from screens.homeScreen   import HomeScreen


def main() -> None:
    Delta = time()
    HomeScreen(Delta)
    

if __name__ == "__main__":
    py.mixer.init()
    py.init()
    main()
    py.quit()
    py.mixer.quit()
    sys.exit()

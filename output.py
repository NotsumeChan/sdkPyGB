import os


def CreateProyect(name: str, flag : str | None) -> None:
    #make a new instance of game folder with the correct name and files
    os.mkdir(name)
    with open(f"{name}/main.py", "w") as f:
        #supose to create the new dir with the necessary files for new proyect
        pass
        
def Clean(name : str | None) -> None:
    #delete the game folder or all game folders
    pass

def Build(name : str | None) -> None:
    #builds/compiles(if possible) the especific game (if only 1 game exist it will be the default)
    pass

def Run(name : str | None) -> None:
    #runs the especific game (if only 1 game exist it will be the default)
    pass

def Create(flag : str) -> None:
    #creates new files dependents of the flag
    pass

def Help() -> None:
    #prints the commands list
    pass


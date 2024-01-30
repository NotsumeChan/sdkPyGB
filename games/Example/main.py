#libraries
import os
import sys
import pygame    as py
from   time      import time
from   functools import cache
#---------

#local files
from Instancias import *
from Config     import FrameRate, Screen
from Network    import *
#-----------

def main() -> None:
    Delta = time()
    MainScreen.FrameRate(FrameRate/2)
    while MainScreen.running:
        #get delta
        Delta = MainScreen.deltaT(Delta)
        #clean screen
        MainScreen.ResetScreen()
        # Get the mouse position
        mouse_pos = py.mouse.get_pos()
        
        #event handler
        for event in py.event.get():
            MainScreen.EventHandler(event)
            if event.type == py.MOUSEBUTTONDOWN:
                for i in MainButtons:
                    if MainButtons[i].IsHover(mouse_pos):
                        if i == "SinglePlayer":
                            Game(Delta)
                        elif i == "MultiPlayer":
                            Lobby(Delta)
                        elif i == "Config":
                            Config(Delta)
                        elif i == "Exit":
                            MainScreen.running = False
        #window breaker
        if MainScreen.running == False:
            continue

        # Draw a white rectangle at the mouse position
        py.draw.rect(MainScreen.canvas, (255, 255, 255), (mouse_pos[0]-25, mouse_pos[1]-25, 50, 50))
        if py.mouse.get_pressed()[0]:
            Config(Delta)
        
        #screen updater
        MainScreen.Update()
    MainScreen.running = True
    

def Config(Delta) -> None:
    ConfigScreen.FrameRate(FrameRate/2)
    while ConfigScreen.running:
        #get delta
        Delta = ConfigScreen.deltaT(Delta)
        #clean screen
        ConfigScreen.ResetScreen()
        #get keys pressed
        Keys = py.key.get_pressed()
        # Get the mouse position
        mouse_pos = py.mouse.get_pos()
        
        #event handler
        for event in py.event.get():
            ConfigScreen.EventHandler(event)
            if event.type == py.MOUSEBUTTONDOWN:
                for i in ConfigButtons:
                    if ConfigButtons[i].IsHover(mouse_pos):
                        if i == "Lobby":
                            Lobby(Delta)
                        elif i == "Game":
                            Game(Delta)
                        elif i == "Config":
                            Config(Delta)
                        elif i == "Exit":
                            MainScreen.running = False
        
        #window breaker
        if ConfigScreen.running == False:
            break

        # Draw a white rectangle at the mouse position
        py.draw.rect(ConfigScreen.canvas, (255, 0, 0), (mouse_pos[0]-50, mouse_pos[1]-50, 100, 100))
        #screen updater
        ConfigScreen.Update()
    ConfigScreen.running = True

def Lobby(Delta) -> None:
    LobbyScreen.FrameRate(FrameRate)
    while LobbyScreen.running:
        #clean screen
        LobbyScreen.ResetScreen()
        #get delta
        Delta = LobbyScreen.deltaT(Delta)
        #get keys pressed
        Keys = py.key.get_pressed()
        # Get the mouse position
        mouse_pos = py.mouse.get_pos()
        
        #event handler
        for event in py.event.get():
            LobbyScreen.EventHandler(event)
        
        #window breaker
        if LobbyScreen.running == False:
            break

        # Draw a white rectangle at the mouse position
        py.draw.rect(LobbyScreen.canvas, (255, 0, 0), (mouse_pos[0]-50, mouse_pos[1]-50, 100, 100))
        if py.mouse.get_pressed()[0]:
            continue
        #screen updater
        LobbyScreen.Update()
    LobbyScreen.running = True

def Game(Delta) -> None:
    GameScreen.FrameRate(FrameRate)
    while GameScreen.running:
        #clean screen
        GameScreen.ResetScreen()
        #get delta
        Delta = GameScreen.deltaT(Delta)
        #get keys pressed
        Keys = py.key.get_pressed()
        # Get the mouse position
        mouse_pos = py.mouse.get_pos()
        
        #event handler
        for event in py.event.get():
            GameScreen.EventHandler(event)
    
        #window breaker
        if GameScreen.running == False:
            break

        # Draw a white rectangle at the mouse position
        py.draw.rect(GameScreen.canvas, (255, 0, 0), (mouse_pos[0]-50, mouse_pos[1]-50, 100, 100))
        if py.mouse.get_pressed()[0]:
            continue
        #screen updater
        GameScreen.Update()
    GameScreen.running = True



if __name__ == "__main__":
    py.init()
    main()
    py.quit()
    sys.exit()

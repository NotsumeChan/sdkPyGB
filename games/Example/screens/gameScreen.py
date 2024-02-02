#module imports
import pygame as py
from Classes import *

#screen define
GameScreen   = Classes.Screen(PickResolution[0], PickResolution[1])

#Buttons of the screen
GameButtons = {}

#Audio of the screen
GameAudio   = {}

#function
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
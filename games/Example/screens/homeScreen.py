#module imports
import pygame as py
from Classes import *

#screen define
MainScreen   = Classes.Screen(PickResolution[0], PickResolution[1]) 

#Buttons of the screen
MainButtons = {}

#Audio of the screen
MainAudio   = {}

def HomeScreen(Delta) -> None:
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

        #window breaker
        if not MainScreen.running:
            continue

        # Draw a white rectangle at the mouse position
        py.draw.rect(MainScreen.canvas, (255, 255, 255), (mouse_pos[0]-25, mouse_pos[1]-25, 50, 50))
        
        #screen updater
        MainScreen.Update()
    MainScreen.running = True
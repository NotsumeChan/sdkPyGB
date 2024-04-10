import os
import sys
import pygame     as py
import moderngl   as mg
from   array      import array
from   Instancias import *
from   Shaders    import Fragment as f
from   Shaders    import Vertex   as v

Basic : tuple[int, int] = (640,480)
Hd    : tuple[int, int] = (1280,720)
Fhd   : tuple[int, int] = (1920,1080)

PickResolution : tuple = Hd

py.init() 
Resolution : tuple = py.display.Info() #Resolucion de la pantalla actual
py.quit()
FrameRate : int = 60

Screen = py.display.set_mode(Hd, py.OPENGL | py.DOUBLEBUF) #Ventana
py.display.set_caption("BroomBlitz") #Titulo de la ventana

ctx = mg.create_context() #Contexto de OpenGL
QuadBuffer = ctx.buffer(data=array('f', [
    # position (x, y), uv coords (x, y)
    -1.0, 1.0, 0.0, 0.0,  # topleft
    1.0, 1.0, 1.0, 0.0,   # topright
    -1.0, -1.0, 0.0, 1.0, # bottomleft
    1.0, -1.0, 1.0, 1.0,  # bottomright
]))


Program = ctx.program(vertex_shader=v.value, fragment_shader=f.value) #Programa de shaders
RenderObj = ctx.vertex_array(Program, [(QuadBuffer, '2f 2f', 'vert', 'texcoord')]) #Objeto a renderizar

#Leer desde "Local.config" para obtener configuraciones locales

#Agregar Opciones Graficas

#Agregar Opciones de Audio

#Teclado/input
InputType = {"k":"keyboard", "c" : "controller", "t" : "touch"}

touch : dict = {} #ni idea de como hacer esto

Keyboard : dict = {"Foward": "K_w", "Left" : "K_a", "Right" : "K_d",  "Backward" : "K_s"} #agregar las keys de pygame para validaciond e inputs

py.joystick.init()
if py.joystick.get_count() > 0:
    Controller : dict =  None #agregar los botones del mando de pygame para validacion de inputs
py.joystick.quit()

Input = Keyboard #input actual

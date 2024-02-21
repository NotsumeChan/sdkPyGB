import os
import sys
import pygame    as py
from   time      import time
from   functools import cache
from   Config   import *
import moderngl as mg
import configparser as confpar

class Screen():
    def __init__(self, w: int, h: int) -> None:
        self.running : bool = True
        self.w : int = w
        self.h : int = h
        self.canvas = py.Surface((self.w, self.h))
        self.clock = py.time.Clock()

    def EventHandler(self, event) -> None:
        if event.type == py.QUIT:
            self.running = False
            py.quit()
            sys.exit()
        if event.type == py.VIDEORESIZE:
            self.Resize(event.w, event.h)

    def ResetScreen(self) -> None:
        self.canvas.fill((0,0,0))

    def Update(self) -> None:
        tex = ctx.texture(self.canvas.get_size(), 4)
        tex.filter = (mg.NEAREST, mg.NEAREST)
        tex.swizzle = 'BGRA'
        tex.write(self.canvas.get_view('1'))

        tex.use(0)
        Program['tex'] = 0
        RenderObj.render(mode=mg.TRIANGLE_STRIP)

        py.display.flip()
        tex.release()

    def FrameRate(self, fps) -> None:
        self.clock.tick(fps)

    def deltaT(self, old) -> float:
        return time() - old

class User():
    def __init__(self) -> None:
        self.icon = None
        self.id : int = ""
        self.nickname : str = ""
        self.email : str = ""
        self.password : str = ""
        self.Characters : list[int] = [] #contiene los id de los personajes que posee el usuario

    def LogIn(self) -> None:
        pass

    def LogOut(self) -> None:
        pass

    def SignUp(self) -> None:
        pass
    
    def SaveConfig(self) -> None:
        pass

    def LoadConfig(self, archivo) -> None:
        with open(archivo, "r") as file:
            config = dict(file.read())
        # Convertir a un diccionario
        for key in config:
            pass

        

class Player():
    __slots__ = ("icon", "sprites", "w", "h", "x", "y")
    def __init__(self, x: int, y: int, img : str) -> None:
        self.icon : py.Surface  = None
        self.sprites : dict = {} #will change to make dic with all sprites
        self.w : int = self.icon.get_width() if self.icon else 0
        self.h : int = self.icon.get_height() if self.icon else 0
        self.x : int = round(x+ (self.w/2))
        self.y : int = round(y+ (self.h/2))

    @cache # in case of sprite stacking or something like that
    def Rotate(self, angle: int) -> None:
        pass
    
    def LoadIcon(self, img : str) -> None:
        if os.path.isfile(f"Assets/Characters/{img}"):
            self.icon = py.image.load(f"Assets/Characters/{img}").convert()
        raise Exception("File or route not found")

    def FillSprites(self, CharName: str) -> None:
        #still need to valide the existence of the file
        for filename in os.listdir("Assets/Characters"):
            if filename == "":
                return
            elif filename.startswith(CharName):
                sprite_name = filename.split("_")[1][:-3]
                sprite_image = py.image.load(f"Assets/Characters/{filename}").convert()
                self.sprites[sprite_name] = sprite_image
        
    def Draw(self, canvas) -> None: #change to draw sprite
        py.draw.rect(canvas, self.color, (self.x, self.y, self.w, self.h))

    def Update(self) -> None: #make movement correctly
        pass

class Button():
    def __init__(self, x: int, y: int, img : str) -> None:
        self.img = py.image.load(f"Assets/Buttons/{img}").convert()
        self.w : int = self.img.get_width()
        self.h : int = self.img.get_height()
        self.x : int = round(x+ (self.w/2))
        self.y : int = round(y+ (self.h/2))

    def Draw(self, canvas) -> None:#change to draw sprite
        py.draw.rect(canvas, self.color, (self.x , self.y, self.w, self.h))
        canvas.blit( (self.x, self.y))

    def IsHover(self, mouse_pos) -> bool:
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h:
                return True
        return False
    
    def IsClick(self, mouse_pos) -> bool:
        return True if self.IsHover(mouse_pos) and py.mouse.get_pressed()[0] and self.reset == 10 else False

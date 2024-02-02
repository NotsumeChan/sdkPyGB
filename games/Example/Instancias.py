import Classes
import pygame as py
from Config import PickResolution


#Listas de Personajes
Personajes : dict = {}
#-------

#llenar listas de personajes (cordenadas iniciales, icon name)
Personajes["Ollie"]   = Classes.Player(0,0, "IconOllie.png")
Personajes["Diana"]   = Classes.Player(0,0, "IconDiana.png")
Personajes["Theo"]    = Classes.Player(0,0, "IconTheo.png")
Personajes["Karneus"] = Classes.Player(0,0, "IconKarneus.png")
Personajes["Ollie"].FillSprites("Ollie")
Personajes["Diana"].FillSprites("Diana")
Personajes["Theo"].FillSprites("Theo")
Personajes["Karneus"].FillSprites("Karneus")
#-------

#Custom Colors
Colors = {}
Colors["White"] = (255,255,255)
Colors["Black"] = (0  ,0  ,0  )
Colors["Red"]   = (255,0  ,0  )
Colors["Green"] = (0  ,255,0  )
Colors["Blue"]  = (0  ,0  ,255)
Colors["Yellow"]= (255,255,0  )
Colors["Cyan"]  = (0  ,255,255)
Colors["Purple"]= (255,0  ,255)
Colors["Grey"]  = (128,128,128)
Colors["Orange"]= (255,128,0  )
Colors["Brown"] = (128,64 ,0  )
Colors["Pink"]  = (255,0  ,128)
#-------
import Classes
import pygame as py
from Config import PickResolution

#Pantallas (cada pantalla tiene resolucion individual)
MainScreen   = Classes.Screen(PickResolution[0], PickResolution[1]) 
ConfigScreen = Classes.Screen(PickResolution[0], PickResolution[1])
LobbyScreen  = Classes.Screen(PickResolution[0], PickResolution[1])
GameScreen   = Classes.Screen(PickResolution[0], PickResolution[1])
#---------

#Listas de Botones
MainButtons   = {}
ConfigButtons = {}
LobbyButtons  = {}
GameButtons   = {}
#-------

#LLenar listas de botones (chord x, chord y, img name)

#nombre de los botores es referencial, no hay assets aun

#main buttons
#MainButtons["SingleP"] = (Classes.Button(10,10, "SinglePlayer.png"))
#MainButtons["MultiP"] = (Classes.Button(20,10, "MultiPlayer.png"))
#MainButtons["Gacha"] = (Classes.Button(30,10, "Gacha.png"))
#MainButtons["Store"] = (Classes.Button(40,10, "Store.png"))
#MainButtons["Config"] = (Classes.Button(50,10, "Config.png"))
#MainButtons["Exit"] = (Classes.Button(60,10, "Exit.png"))
#config buttons
#ConfigButtons.append(Classes.Button(10,10, "Video.png"))
#ConfigButtons.append(Classes.Button(10,10, "Back.png"))
#lobby buttons
#LobbyButtons.append(Classes.Button(10,10, "Back.png"))
#game buttons
#GameButtons.append(Classes.Button(10,10, "Stop.png"))
#-------

#Listas  audio
MainAudio   = {}
ConfigAudio = {}
LobbyAudio  = {}
GameAudio   = {}
#-------

#llenar listas de audio (nombre, volumen)
#main audio

#config audio

#lobby audio

#game audio
py.mixer.init()
GameAudio["RaceStart"] = (py.mixer.Sound("Assets/Sounds/RaceStart.wav"))

py.mixer.quit()
#-------

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

#Teclado/input
InputType = {"k":"keyboard", "c" : "controller", "t" : "touch"}
touch : dict = {} #ni idea de como hacer esto
Keyboard : dict = {"Foward": "K_w", "Left" : "K_a", "Right" : "K_d",  "Backward" : "K_s"} #agregar las keys de pygame para validaciond e inputs
Controller : dict =  None #agregar los botones del mando de pygame para validacion de inputs
py.joystick.init()
if py.joystick.get_count() > 0:
    Controller =  {}
py.joystick.quit()
Input = Keyboard #input actual
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
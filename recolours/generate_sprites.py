from __future__ import print_function
import sys
import math
from PIL import Image
from PIL import ImageEnhance
import glob

### A script to generate mods from unpacked content
### To run, open a terminal/command line from within this folder and type "python generate_sprites.py"

## Make sure start_path points to wherever you've saved "Content (unpacked)"
# the unpacked Stardew Valley files as created by StardewXnbHack https://stardewvalleywiki.com/Modding:Editing_XNB_files#Unpack_game_files 

## Mod links:
# Blue UI: https://www.nexusmods.com/stardewvalley/mods/13348
# Starry Blue UI https://www.nexusmods.com/stardewvalley/mods/13694
# Weird Recolour: https://www.nexusmods.com/stardewvalley/mods/13365

## Feel free to reuse this code to make your own mods, but if you publish it publicly please credit me, sqbr (and of course Concerned Ape if you use his art!)
################
  
## general data functions  
def list_directory(directory,pattern):
    #lists every element of a directory matching the pattern
    return [path.split("/").pop() for path in glob.glob(directory+pattern)]
  
def sort(l):
    # a terrible sorting algorithm
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
                  
        # Swap the found minimum element with 
        # the first element        
        l[i], l[min_idx] = l[min_idx], l[i]   
    return l     
    
def remove_list(list1,list2):
    #list1 minus any elements of list2
    new_list = []
    for l in list1:
        if not l in list2:
            new_list.append(l)
    return new_list            
    
def in_dictionary(dictionary, folder, name):
    #checked whether folder/name is listed
    if folder in dictionary.keys():
        if name in dictionary[folder]:
            return True
    return False    
    
## Image functions: full images

def invertA(X):
    #invert the colour X
    return 255-X   
    
def invert_alpha(img):
    #Returns image with inverted alpha of img, img is in RGBA format
    alpha = Image.eval(img.getchannel("A"),invertA ) #a black and white image
    return Image.merge("RGBA", (alpha,alpha,alpha,alpha))

## Image functions: individual pixels, HSV

def in_range_rot(X, floor,ceil):
    #returns if X is between floor and ceil, including modulo effects
    if floor < ceil:
        return ((X>floor) and (X<ceil))
    else:
        return ((X>floor) or (X<ceil))    
    
def rotate(h, x):
    #rotate hue h by X
    return (h+x) % 256     
    
## Image functions: individual pixels, RGB
    
def true_invert(oldR,oldG,oldB):
    #create a new rgba colour that is inverted 
    newR = (oldG+oldB)/2
    newG = (oldR+oldB)/2
    newB = (oldR+oldG)/2
    return [newR,newG,newB] 
        
def blue_invert(oldR,oldG,oldB):
    #create a new rgba colour that is inverted but doesn't have lower blue
    newR = (oldG+oldB)/2
    newG = (oldR+oldB)/2
    newB = max(oldB, (oldR+oldG)/2) 
    return [newR,newG,newB] 
    
def rotate_hue60(oldR,oldG,oldB, C):
    #not sure this literally rotates by angle arcsin(C) +60 but something like that
    newR = C*oldG + (1-C)*oldB
    newG = C*oldB + (1-C)*oldR
    newB = C*oldR + (1-C)*oldG
    return [newR,newG,newB]  

def rotate_hue(oldR,oldG,oldB, C):
    #not sure this literally rotates by angle -arcsin(C) but something like that
    newR = C*oldG + (1-C)*oldR
    newG = C*oldB + (1-C)*oldG
    newB = C*oldR + (1-C)*oldB
    return [newR,newG,newB]              
     
def rotate_hue_flip(oldR,oldG,oldB, C):
    #not sure this literally rotates by angle -arcsin(C) but something like that
    newR = C*oldB + (1-C)*oldR
    newG = C*oldR + (1-C)*oldG
    newB = C*oldG + (1-C)*oldB
    return [newR,newG,newB]             
    
def desaturate(oldR,oldG,oldB, C):
    #C is how much to desaturate between 0 and 1
    average = (oldR+oldG+oldB)/3
    
    newR = (1-C)*oldR + C*average
    newG = (1-C)*oldG + C*average
    newB = (1-C)*oldB + C*average
    return [newR,newG,newB]   

def saturation(p):
    M = max(p)
    m = min(p)
    d = (M - m)/255
    L = (M + m)/510 
    if L ==0:
        return 0
    else:    
        X = 1 - abs(2*L-1)
        if X == 0:
            return 0
        return d/X 

def match_saturation(originalC, newC):
    # returns a colour with the same hue and luminance as newC but the same saturation as originalC
    L = saturation(originalC) #luminance
    if L < 5:
        return newC #so dark there'll be rounding errors or divide by zero issues 
    else: 
        D = saturation(newC)
        if D == 0:
           return newC 
        else:     
            X = L/D  #ratio
            return (X*newC[0], X*newC[1], X*newC[2])     

def luminance(p):
    return (0.299*p[0] + 0.587*p[1] + 0.114*p[2])              
       
def hue(p):
    #returns an angle between 0 and 360
    R = p[0]
    G = p[1]
    B = p[2]
    if R==G and R==B:
        return 0
    elif (R>=G) and G >=B:
        return 60*(G-B)/float(R-B)
    elif G>R and R>= B:
        return 60*(2-(R-B)/float(G-B))
    elif G>=B and B> R:
        return 60*(2+(B-R)/float(G-R))
    elif B>G and G> R:
        return 60*(4-(G-R)/float(B-R))   
    elif B>R and R>= G:
        return 60*(4+(R-G)/float(B-G))   
    else:
        return 60*(6-(B-G)/float(R-G))  

def HSL_to_RGB(h,s,l):

    C = (255-abs(2*l-255)*s)
    m = l-0.5*C
    if h <60:
        X = C*h/60.0
        R = C
        G = X
        B = 0
    elif h<120:
        X = C*(120-h)/60.0
        R = X
        G = C
        B = 0
    elif h<180:
        X = C*(h-120)/60.0
        R = 0
        G = C
        B = X
    elif h<240:
        X = C*(240-h)/60.0
        R = 0
        G = X
        B = C  
    elif h<300:
        X = C*(h-240)/60.0
        R = X
        G = 0
        B = C
    else:
        X = C*(360-h)/60.0
        R = C
        G = 0
        B = X
    return (R+m, G+m, B+m)

def true_rotate_hue(colour, angle):
    #not sure this literally rotates by angle -arcsin(C) but something like that
    h = hue(colour)
    s = saturation(colour)
    l = luminance(colour)
    return HSL_to_RGB((h+angle)%360,1,100)        


def match_luminance(originalC, newC):
    #makes colour with the same sat and hue as newC but the same percieved luminance as originalC
    L = luminance(originalC) #luminance
    if L < 5:
        return newC #so dark there'll be rounding errors or divide by zero issues 
    else: 
        D = luminance(newC)
        if D == 0:
           return (255, 255, 255) 
        else:     
            X = L/D  #ratio
            return (X*newC[0], X*newC[1],X*newC[2])

def change_luminance(originalC, newC):
    #makes colour with the same sat and hue as newC but the same percieved luminance as originalC
    # except more dramatic
    L = luminance(originalC) #luminance
    if L < 5:
        return newC #so dark there'll be rounding errors or divide by zero issues 
    else: 
        D = luminance(newC)
        if D == 0:
           return (255, 255, 255) 
        else:     
            X = (1-math.cos(math.pi*L/256.0))*128/D  #ratio
            return (X*newC[0], X*newC[1],X*newC[2])            
              
def colour_UI(pixel):
    #desaturates and makes yellow into blue/purple
    p=pixel
    oldR = pixel[0]
    oldG = pixel[1]
    oldB = pixel[2]
    C = 0.3
    newR = C*oldG + (1-C)*oldB
    newG = C*oldR + (1-C)*oldB
    newB = C*oldG + (1-C)*oldR

    p = desaturate(newR,newG,newB, 0.3)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])

def colour_UIbase(pixel):
    #desaturates and makes yellow into purple
    p=pixel
    oldR = pixel[0]
    oldG = pixel[1]
    oldB = pixel[2]
    C = 0.3
    newR = C*oldG + (1-C)*oldB
    newG = C*oldR + (1-C)*oldB
    newB = C*oldG + (1-C)*oldR
    (pinkR,pinkG,pinkB) = true_rotate_hue( (newR,newG,newB),15)
    newR = (pinkR+newR)/2.0
    newG = (pinkG+newG)/2.0
    newB = (pinkB+newB)/2.0
    p = desaturate(newR,newG,newB, 0.6)
    #p = desaturate(oldR,oldG,oldB, 0.5)
    p = change_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])    
    
def colour_UIframe(pixel):
    #desaturates and makes yellow into blue
    p=pixel
    oldR = pixel[0]
    oldG = pixel[1]
    oldB = pixel[2]
    C = 0.3
    newR = C*oldG + (1-C)*oldB
    newG = C*oldR + (1-C)*oldB
    newB = C*oldG + (1-C)*oldR
    (pinkR,pinkG,pinkB) = true_rotate_hue( (newR,newG,newB),5)
    newR = (pinkR+newR)/2.0
    newG = (pinkG+newG)/2.0
    newB = (pinkB+newB)/2.0
    p = desaturate(newR,newG,newB, 0.6)
    p = match_luminance(pixel, p)
    X = 0.85
    p = (p[0]*X, p[1]*X,p[2]*X)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])
        
def colour_ground(pixel):
    #desaturates and makes yellow into blue/purple
    p=pixel
    p = blue_invert(p[0],p[1],p[2])
    p = desaturate(p[0],p[1],p[2], 0.3)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])
    
def colour_plants(pixel):
    #desaturates and makes yellow into blue/purple
    p=pixel
    C1 = 0.2
    C2 = 0.5
    edge = 300

    H = hue(pixel)
    if H<=60:
        C = C2*H/60 + C1*(60-H)/60
    elif H>=edge:
        #C = C1*(H-edge)/60 + C2*(H/(360.0-edge)-edge/(360.0-edge))/60
        C = C1*(H-edge)/60.0 + C2*(1-((H-edge)/60.0))
    else:    
        C = C2
    p = rotate_hue_flip(p[0],p[1],p[2], C)

    p = desaturate(p[0],p[1],p[2], 0.15)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])    
    
def colour_wood(pixel):
    #desaturates and makes yellow into blue/purple
    p=pixel
    p = rotate_hue(p[0],p[1],p[2], 0.35)
    p = desaturate(p[0],p[1],p[2], 0.15)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])   

def colour_fall(pixel):
    #desaturates and makes yellow into blue/purple
    p=pixel
    C1 = 0
    C2 = 0.5
    edge = 200

    H = hue(pixel)
    if H<=60:
        C = C2*H/60 + C1*(60-H)/60
    elif H>=edge:
        #C = C1*(H-edge)/60 + C2*(H/(360.0-edge)-edge/(360.0-edge))/60
        C = 0
    else:    
        C = C2
    p = rotate_hue_flip(p[0],p[1],p[2], C)

    p = desaturate(p[0],p[1],p[2], 0.15)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])    

def colour_flowers(pixel):
    #desaturates and makes yellow into blue/purple 
    p=pixel 
    p = desaturate(p[0],p[1],p[2], 0.15)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])   

def colour_other(pixel):
    #makes less yellow
    p=pixel
    oldR= p[0]
    oldG = p[1]
    oldB = p[2]
    C=0.3
    newR = oldR
    newG =oldG
    newB = oldB
    newB = max(oldB, C*(max(oldR,oldG)-oldB)+(1-C)*oldB)

    p=(newR,newG,newB)
    p = desaturate(p[0],p[1],p[2], 0.2)
    p = match_saturation(pixel, p)
    p = match_luminance(pixel, p)
    return (int(p[0]),int(p[1]),int(p[2]),pixel[3])            
    
def colour_this(pixel):
    #RGBA mode
    if mode =="UI":
        return colour_UI(pixel)
    elif mode =="UIbase":
        return colour_UIbase(pixel)   
    elif mode =="UIframe":
        return colour_UIframe(pixel)        
    elif mode == "ground":
        return colour_ground(pixel)   
    elif mode == "plants":
        return colour_plants(pixel)  
    elif mode == "wood":
        return colour_wood(pixel)  
    elif mode == "fall":
        return colour_fall(pixel)      
    elif mode == "flowers":
        return colour_flowers(pixel)        
    else:
        return colour_other(pixel)         
                  
        
# HSV        
def hue_this(pixel):
    #HSV mode
    if mode == "wood":
        return (rotate(pixel[0],-40), int(0.7*pixel[1]),pixel[2]) 
    elif mode == "plants": 
        return (rotate(pixel[0],60), int(0.7*pixel[1]),pixel[2])          
    else:
        return pixel         
    
## General data       
   
start_path = "../../Content (unpacked)/"

folders_all =   list_directory(start_path,"*")
#['Maps', 'LooseSprites', 'Buildings', 'Strings', 'Minigames', 'VolcanoLayouts', 'TerrainFeatures', 'Portraits', 'TileSheets', 'Animals', 'Characters', 'Fonts', 'Effects', 'Data']
folders2_all = ["Characters/Farmer","Characters/Monsters", "LooseSprites/Lighting", "Maps/Mines"] #nested folders
files_all = {}
for f in folders_all:
    files_all[f]=list_directory(start_path+f+'/',"*.png") 
      
#print(sort(files_all['Buildings']))    

files_translated = { #files with translated versions
     "LooseSprites": ['JojaCDForm.png', 'Cursors.png', 'Billboard.png', 'ControllerMaps.png', 'JunimoNote.png', ],
     "Minigames": ['TitleButtons.png'],
     "Fonts":['SmallFont.png','SpriteFont.png'],
     "Maps": ["towninterior.png"]
}

translations = ["zh-CN","ja-JP","it-IT","es-ES","de-DE","ko-KR","fr-FR","ru-RU","tr-TR","hu-HU","pt-BR",]

files_onIsland = { #add  a check for if you're on the island
    'LooseSprites': ['LightRays.png','Movies.png','ParrotPlatform.png','PlayerStatusList.png','SandDuggy.png','SeaMonster.png','SpecialOrdersBoard.png','birds.png','daybg.png','nightbg.png','parrots.png','shadow.png','swimShadow.png'],
    "Maps": [ 'FarmhouseTiles.png', 'Festivals.png', 'GreenHouseInterior.png','Island_FieldOffice_Tilesheet.png', 'Island_Hut_tilesheet.png', 'LeoTreeHouse_Tilesheet.png', 'TownIndoors.png','WoodBuildings.png', 'boatTunnelTiles.png', 'bugLandTiles.png', 'busPeople.png', 'cave.png', 'cavedarker.png','coopTiles.png', 'fall_beach.png', 'fall_monsterGraveTiles.png', 'fall_outdoorsTileSheet.png', 'fall_outdoorsTileSheet2.png', 'fall_town.png','fall_island_tilesheet_1.png', 'farmhouse_tiles.png', 'island_tilesheet_1.png', 'island_tilesheet_2.png','nightSceneMaruTrees.png', 'night_market_tilesheet_objects.png', 'paths.png', 'spring_BusStop.png', 'spring_beach.png', 'spring_island_tilesheet_1.png','spring_monsterGraveTiles.png','spring_outdoorsTileSheet2.png', 'spring_town.png', 'springobjects.png', 'summer_beach.png', 'summer_island_tilesheet_1.png','summer_monsterGraveTiles.png', 'summer_outdoorsTileSheet.png', 'summer_town.png', 'townInterior.png', 'winter_beach.png', 'winter_island_tilesheet_1.png', 'winter_monsterGraveTiles.png', 'winter_outdoorsTileSheet.png', 'winter_outdoorsTileSheet2.png', 'winter_town.png', 'witchSwampTiles.png'],
    "TileSheets":['Floors.png','crops.png','animations.png','bushes.png','SecretNotesImages.png','debris.png'],
    'TerrainFeatures': ['Flooring.png', 'Flooring_winter.png', 'tree_palm.png', 'tree_palm2.png','hoeDirt.png', 'hoeDirtDark.png','hoeDirtSnow.png'],
    'Buildings': ['Barn.png', 'Big Barn.png', 'Big Coop.png', 'Big Shed.png', 'Coop.png', 'Deluxe Barn.png', 'Deluxe Coop.png','Desert Obelisk.png', 'Earth Obelisk.png', 'Fish Pond.png', 'Gold Clock.png', 'Greenhouse.png', 'Junimo Hut.png', 'Log Cabin.png', 'Mill.png', 'Plank Cabin.png', 'Shed.png', 'Shipping Bin.png', 'Silo.png', 'Slime Hutch.png', 'Stable.png', 'Stone Cabin.png', 'Water Obelisk.png', 'Well.png', 'houses.png'],
}

#Data used by each mode. 

#The modes are used to create 3 mods, in layers. Each layer has it's own sub-mod and associated mode. 

# "Blue UI": UI 

# "Starry Blue UI": UIbase, UIframe

# "Weird Recolour": ground, wood, plants, flowers, fall

# Unused modes: character, other

folders = {} #folders where every file is in the mod 
folders2 = {} #sub-folders where every file is in the mod 
files = {} #individual files in the mod
files_not = {} #files to exclude
masks = {} #files with associated masks
unmasks ={} #other modes to be used as exclusion masks
overlays ={} #files with associated overlays
colour_mode = {} #whether to use RGBA or HSV
end_path = {} #where to save the mod

def initialise(m):
    # set all the values for the current mode
    global folders,folders2,files,masks,unmasks,overlays,colour_mode,end_path

    folders[mode] = []
    folders2[mode] = []
    files[mode] = {} 
    files_not[mode] = {} 
    masks[mode] = {}
    unmasks[mode] =[]
    overlays[mode] = {}
    colour_mode[mode] = "RGBA"
    end_path[mode] = ""

## UI
mode = "UI"
initialise(mode)
colour_mode[mode] = "RGBA"
end_path[mode] = "[CP] Blue UI/"

files[mode] = { 
    "LooseSprites":['chatBox.png', 'textBox.png','skillTitles.png','Cursors.png','Cursors_1_6.png', 'DialogBoxGreen.png', 'ControllerMaps.png', 'yellowLettersLogo.png', 'letterBG.png', 'tailoring.png', 'boardGameBorder.png', 'font_bold.png', 'SpecialOrdersBoard.png','logo.png', 'JunimoNote.png', 'LanguageButtons.png', 'Cursors2.png', 'Billboard.png','daybg.png','nightbg.png','map.png','map_summer.png','map_fall.png','map_winter.png'],
    "Minigames": ['TitleButtons.png'],
    "Maps": ['MenuTiles.png', 'MenuTilesUncolored.png'],
    
}

masks[mode] = { #Masked images
    "LooseSprites":['Cursors.png','Cursors_1_6.png','Cursors2.png','tailoring.png','JunimoNote.png','font_bold.png','daybg.png','nightbg.png','Billboard.png','map.png','map_summer.png','map_fall.png','map_winter.png'],
    "Minigames": ['TitleButtons.png'],
    "Maps": ['MenuTiles.png']
}

overlays[mode] = {
    "Minigames": ['TitleButtons.png'],
}   

## UIbase
mode = "UIbase"
initialise(mode)
colour_mode[mode] = "RGBA"
end_path[mode] = "sub-mods/[CP] UI base/"

files[mode] = { 
    "LooseSprites":['chatBox.png', 'textBox.png','Cursors.png','Cursors_1_6.png', 'DialogBoxGreen.png', 'ControllerMaps.png', 'yellowLettersLogo.png', 'letterBG.png', 'tailoring.png', 'boardGameBorder.png', 'font_bold.png','logo.png', 'JunimoNote.png', 'LanguageButtons.png', 'Cursors2.png', 'Billboard.png','daybg.png','nightbg.png','SpecialOrdersBoard.png',],
    "Minigames": ['TitleButtons.png'],
    "Maps": ['MenuTiles.png', 'MenuTilesUncolored.png'],
    
}

masks[mode] = { #Masked images
    "LooseSprites":['Cursors.png','Cursors2.png','Cursors_1_6.png','textBox.png','tailoring.png','JunimoNote.png','letterBG.png','font_bold.png','daybg.png','nightbg.png','Billboard.png','SpecialOrdersBoard.png',],
    "Minigames": ['TitleButtons.png'],
    "Maps": ['MenuTiles.png']
}

overlays[mode] = {
    "Minigames": ['TitleButtons.png'],
    "LooseSprites":['Cursors.png',]
}  

## UIframe
mode = "UIframe"
initialise(mode)
colour_mode[mode] = "RGBA"
end_path[mode] = "sub-mods/[CP] UI frame/"

files[mode] = { 
    "LooseSprites":['textBox.png','Cursors.png','Cursors_1_6.png', 'DialogBoxGreen.png', 'boardGameBorder.png','SpecialOrdersBoard.png','LanguageButtons.png', 'Cursors2.png', 'Billboard.png','daybg.png','nightbg.png',],
    "Minigames": ['TitleButtons.png'],
    "Maps": ['MenuTiles.png', 'MenuTilesUncolored.png'],
    
}

masks[mode] = { #Masked images
    "LooseSprites":['Cursors.png','Cursors_1_6.png','Cursors2.png','daybg.png','DialogBoxGreen.png','LanguageButtons.png','nightbg.png','Billboard.png','SpecialOrdersBoard.png','textBox.png',],
    "Minigames": ['TitleButtons.png'],
    "Maps": ['MenuTiles.png']
}

overlays[mode] = {
    "Minigames": ['TitleButtons.png'],
    "LooseSprites":['Billboard.png','Cursors.png','SpecialOrdersBoard.png'],
}   
 
## Character. Not used.  

folders_character = ["Characters","Portraits"]
folders2_character = ["Characters/Farmer"]
files_character = {
    "LooseSprites": ['robinAtWork.png']
}

##ground
mode = "ground"
initialise(mode)
end_path[mode] = "sub-mods/[CP] Goth Ground/"

files[mode] = { 
    'LooseSprites':['Cursors.png','daybg.png','map.png','nightbg.png','shadow.png','swimShadow.png'],
    "Maps": [ 'Festivals.png', 'boatTunnelTiles.png', 'fall_beach.png', 'fall_monsterGraveTiles.png', 'fall_outdoorsTileSheet.png', 'fall_outdoorsTileSheet2.png', 'fall_town.png', 'nightSceneMaru.png',   'spring_BusStop.png', 'spring_beach.png', 'spring_monsterGraveTiles.png',  'spring_outdoorsTileSheet.png','spring_outdoorsTileSheet2.png', 'spring_town.png', 'summer_beach.png', 'summer_monsterGraveTiles.png',  'summer_outdoorsTileSheet.png', 'summer_outdoorsTileSheet2.png','summer_town.png', 'townInterior.png', 'winter_beach.png',  'winter_monsterGraveTiles.png', 'winter_outdoorsTileSheet.png', 'winter_outdoorsTileSheet2.png', 'winter_town.png','summer_island_tilesheet_1.png','spring_island_tilesheet_1.png','winter_island_tilesheet_1.png','fall_island_tilesheet_1.png'],
    'TerrainFeatures': ['Flooring.png', 'Flooring_winter.png', 'grass.png', 'hoeDirt.png', 'hoeDirtDark.png', 'hoeDirtSnow.png'],
    'Minigames': ['Intro.png','boatJourneyMap.png'],
}
masks[mode] = { #these files show up in multiple mods
    "LooseSprites":['Cursors.png','daybg.png','map.png','nightbg.png',],
    "Maps": ['Festivals.png','boatTunnelTiles.png', 'fall_beach.png', 'fall_monsterGraveTiles.png', 'fall_outdoorsTileSheet.png', 'fall_outdoorsTileSheet2.png', 'fall_town.png', 'nightSceneMaru.png',   'spring_BusStop.png', 'spring_beach.png', 'spring_monsterGraveTiles.png',  'spring_outdoorsTileSheet.png','spring_outdoorsTileSheet2.png', 'spring_town.png', 'summer_beach.png', 'summer_monsterGraveTiles.png',  'summer_outdoorsTileSheet.png','summer_outdoorsTileSheet2.png','summer_town.png','townInterior.png', 'winter_beach.png',  'winter_monsterGraveTiles.png', 'winter_outdoorsTileSheet.png', 'winter_outdoorsTileSheet2.png', 'winter_town.png','summer_island_tilesheet_1.png','spring_island_tilesheet_1.png','winter_island_tilesheet_1.png','fall_island_tilesheet_1.png'],
    'TerrainFeatures': ['Flooring.png', 'Flooring_winter.png',],
    'Minigames': ['Intro.png','boatJourneyMap.png',"UI"],
}

overlays[mode] = {"Maps": ['townInterior.png',]}
unmasks[mode] =[]#"UI"]

## plants
mode = "plants"
initialise(mode)
end_path[mode] = "sub-mods/[CP] Goth Plants/"

files[mode] = { 
    "LooseSprites":['Cursors_1_6.png', 'Cursors.png','map.png','tailoring.png', 'Cursors2.png','stardewPanorama.png',],
    "Maps": [ 'HarveyBalloonTiles.png','spring_beach.png', 'winter_beach.png','fall_beach.png', 'summer_beach.png','winter_town.png', 'spring_town.png','fall_town.png','summer_town.png','springobjects.png', 'fall_outdoorsTileSheet.png','spring_outdoorsTileSheet.png','summer_outdoorsTileSheet.png','spring_outdoorsTileSheet2.png','summer_outdoorsTileSheet2.png','fall_outdoorsTileSheet2.png','townInterior.png','winter_outdoorsTileSheet.png',],
    'TerrainFeatures': [ 'tree1_fall.png', 'tree1_spring.png', 'tree1_summer.png', 'tree2_fall.png', 'tree2_spring.png', 'tree2_summer.png', 'tree3_fall.png', 'tree3_winter.png','tree3_spring.png', 'tree8_fall.png', 'tree8_spring.png', 'tree8_summer.png', ],
    "TileSheets":['bushes.png'],
    'Minigames': ['Clouds.png',],
}
masks[mode] = { #these files show up in multiple mods
    "LooseSprites":['Cursors.png','Cursors_1_6.png','map.png','tailoring.png','Cursors2.png','stardewPanorama.png',],
    "Maps": ['HarveyBalloonTiles.png','spring_beach.png', 'winter_beach.png','fall_beach.png', 'summer_beach.png','winter_town.png', 'spring_town.png','fall_town.png','summer_town.png','springobjects.png','fall_outdoorsTileSheet.png','spring_outdoorsTileSheet.png','summer_outdoorsTileSheet.png','spring_outdoorsTileSheet2.png','summer_outdoorsTileSheet2.png','fall_outdoorsTileSheet2.png','townInterior.png','winter_outdoorsTileSheet.png',],
    'Minigames': ['Clouds.png',],
}
unmasks[mode] =["ground","wood"]#,"UI"]

overlays[mode] = {    
    "Maps": ['springobjects.png','townInterior.png'],
}

## Wood

mode = "wood"
initialise(mode)
end_path[mode] = "sub-mods/[CP] Goth Wood/"

files[mode] = { 
    "LooseSprites":['Cursors.png','tailoring.png',"map.png"],
    "Maps": ['spring_beach.png', 'winter_beach.png','fall_beach.png', 'summer_beach.png','winter_town.png', 'spring_town.png','fall_town.png','summer_town.png','springobjects.png','fall_outdoorsTileSheet.png','spring_outdoorsTileSheet.png','summer_outdoorsTileSheet.png','spring_outdoorsTileSheet2.png','summer_outdoorsTileSheet2.png','fall_outdoorsTileSheet2.png','winter_outdoorsTileSheet2.png','townInterior.png','winter_outdoorsTileSheet.png',],
    'TerrainFeatures': ['tree1_fall.png', 'tree1_spring.png', 'tree1_summer.png', 'tree1_winter.png', 'tree2_fall.png', 'tree2_spring.png', 'tree2_summer.png', 'tree2_winter.png', 'tree3_fall.png', 'tree3_spring.png', 'tree3_winter.png', 'tree8_fall.png', 'tree8_spring.png', 'tree8_summer.png' ],
    "TileSheets":['bushes.png'],
    'Minigames': ['Clouds.png',],
}
#note tree3 is a pine
masks[mode] = { #these files show up in multiple mods
    "LooseSprites":['Cursors.png','tailoring.png',"map.png"],
    "Maps": [ 'HarveyBalloonTiles.png','spring_beach.png', 'winter_beach.png','fall_beach.png', 'summer_beach.png','winter_town.png', 'spring_town.png','fall_town.png','summer_town.png','springobjects.png','fall_outdoorsTileSheet.png','spring_outdoorsTileSheet.png','summer_outdoorsTileSheet.png','spring_outdoorsTileSheet2.png','summer_outdoorsTileSheet2.png','fall_outdoorsTileSheet2.png','winter_outdoorsTileSheet2.png','townInterior.png','winter_outdoorsTileSheet.png',],
    'TerrainFeatures': ['tree1_fall.png', 'tree1_spring.png', 'tree1_summer.png', 'tree2_fall.png', 'tree2_spring.png', 'tree2_summer.png','tree3_fall.png', 'tree3_spring.png', 'tree3_winter.png', 'tree8_fall.png', 'tree8_spring.png', 'tree8_summer.png'],
    "TileSheets":['bushes.png'],
    'Minigames': ['Clouds.png',],
}
unmasks[mode] =["ground"]#,"UI"]
overlays[mode] = {    
    "Maps": ['springobjects.png']
}
   
## fall. Red things, mostly autumn leaves.  

mode = "fall"
initialise(mode)
end_path[mode] = "sub-mods/[CP] Goth Fall/"

files[mode] = { 
    "Maps": ['fall_outdoorsTileSheet.png',"fall_town.png","fall_beach.png"],
    "TileSheets":['bushes.png'],
    'TerrainFeatures': ['mushroom_tree.png', 'tree1_fall.png','tree2_fall.png','tree8_fall.png', ],
}
masks[mode] = { 
    "Maps": ['fall_outdoorsTileSheet.png',"fall_town.png","fall_beach.png"],
    "TileSheets":['bushes.png'],
}
unmasks[mode] =["ground","wood"]

## flowers
mode = "flowers"
initialise(mode)
end_path[mode] = "sub-mods/[CP] Goth Flowers/"

files[mode] = { 
    "Maps": ['spring_town.png','summer_town.png',"fall_town.png", 'springobjects.png', 'fall_outdoorsTileSheet.png','spring_outdoorsTileSheet.png','summer_outdoorsTileSheet.png'],
    "TileSheets":['bushes.png'],
}
masks[mode] = { 
    "Maps": ['spring_town.png','summer_town.png',"fall_town.png",'springobjects.png','fall_outdoorsTileSheet.png','spring_outdoorsTileSheet.png','summer_outdoorsTileSheet.png'],
    "TileSheets":['bushes.png'],
}
unmasks[mode] =["ground","wood"]

##other. Not used. 
mode = "other"
initialise(mode)
end_path[mode] = "sub-mods/[CP] Goth Other/"

folders[mode] = ['Maps', 'LooseSprites', 'Minigames', 'TerrainFeatures', 'Portraits', 'TileSheets', 'Animals', 'Characters',]

folders2[mode] = ["LooseSprites/Lighting","Characters/Farmer","Characters/Monsters", "Maps/Mines"]
files[mode] = { 
    'Buildings': ['Barn.png', 'Big Barn.png', 'Big Coop.png', 'Big Shed.png', 'Coop.png', 'Deluxe Barn.png', 'Deluxe Coop.png','Desert Obelisk.png', 'Earth Obelisk.png', 'Fish Pond.png', 'Gold Clock.png', 'Greenhouse.png', 'Junimo Hut.png', 'Log Cabin.png', 'Mill.png', 'Plank Cabin.png', 'Shed.png', 'Shipping Bin.png', 'Silo.png', 'Slime Hutch.png', 'Stable.png', 'Stone Cabin.png', 'Water Obelisk.png', 'Well.png', 'houses.png'],
}

files_not[mode]={
    "LooseSprites": ['ParrotPlatform.png','parrots.png','EmilyDreamscapeTiles.png'],
    'TerrainFeatures': ['mushroom_tree.png', 'tree1_fall.png', 'tree1_spring.png', 'tree1_summer.png', 'tree1_winter.png', 'tree2_fall.png', 'tree2_spring.png', 'tree2_summer.png', 'tree2_winter.png', 'tree3_fall.png', 'tree3_spring.png', 'tree3_winter.png', 'tree8_fall.png', 'tree8_spring.png', 'tree8_summer.png' ],

}
unmasks[mode] =["ground","wood","UI","plants"]


##Recolour

# Creating the "Weird Recolour" mod

mode ="recolour"
initialise(mode)
have_image ={}
end_path[mode] = "[CP] Weird Recolour/"

##UIRecolour

# Creating the "Starry Blue UI" mod

mode ="UIrecolour"
initialise(mode)
have_image ={}
end_path[mode] = "[CP] Starry Blue UI/"

UI_list = ["UI","UIbase","UIframe","UIrecolour"]

## Data processing   

def area_string(x,y,w,h):
    #the string to add when cutting and pasting a rectangle
    pos_string ="{ \"X\": "+str(x)+", \"Y\": "+str(y)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }" 
    return "         \"FromArea\": "+pos_string+",\"ToArea\":  "+pos_string+",\n"

def create_code(folder, sprite_name):
    #create the section of code in content.json for sprite_name 
    code =""
    split_name = sprite_name.split(".")
    short_name = split_name[0]
    codeend = "         \"PatchMode\": \"Overlay\"\n      },\n\n" # the bit at the end of each block
    code+="      {\n"
    code+="         \"Action\": \"EditImage\",\n"
    code+="         \"Target\": \""+folder + "/"+ short_name+"\",\n"
    if in_dictionary(files_translated, folder,sprite_name) and mode in UI_list: #uses different versions depending on language
        code+="         \"FromFile\": \"assets/{{Target}}_{{language}}.png\",\n"
    else:
        code+="         \"FromFile\": \"assets/{{Target}}.png\",\n"
    # if short_name =="Cursors" and mode =="UIrecolour": # cut into pieces for custom cursors. Broken.  
    #     finalcode =code
    #     finalcode += area_string(0,0,150,25)
    #     finalcode+="         \"When\":{\"EditCursor\": \"true\"},\n"   
    #     finalcode += codeend
    #     finalcode +=code
    #     finalcode += area_string(150,0,554,25)
    #     finalcode += codeend
    #     finalcode +=code
    #     finalcode += area_string(0,25,704,2231)
    #     finalcode += codeend
    #     return finalcode 
    if in_dictionary(files_onIsland, folder,sprite_name) and not (mode in UI_list):
             code+="         \"When\":{\n"
             code+="             \"LocationContext\": \"Default\"\n"
             code+="         },\n"   
             code+="         \"Update\": \"OnLocationChange\",\n" 
    code+=codeend  
    return code
   
def process_items(items,folder,content):
    #process every element of the list items, which is contained within folder, write code to content
    for sprite_name in items:
        if not in_dictionary(files_not[mode],folder,sprite_name):
            split_name = sprite_name.split(".")
            if len(split_name)==2: #not translated, translated versions processed separately
                content.write(create_code(folder, sprite_name)) 
                if in_dictionary(files_translated, folder,sprite_name) and mode in UI_list: #has translations
                    split_name = sprite_name.split(".")
                    short_name = split_name[0]
                    for t in translations:
                        process_image(folder,short_name+"."+t+".png")
                process_image(folder,sprite_name)
       
def process_folder():
    #process all the images with the current mode's color settings
    if True: #not mode == "UI":
        content = open(end_path[mode]+"content.json","w")
        content.write("{\n")
        content.write("   \"Format\": \"1.27.0\",\n")
        content.write("   \"Changes\": [\n")
    for folder in folders[mode]: #simple folder
        items =list_directory(start_path+folder+'/',"*.png")  #blah.thing.png
        process_items(items,folder,content)      
    for folder in folders2[mode]: #nested folder
        items = list_directory(start_path+folder+'/',"*.png")  #blah.thing.png
        process_items(items,folder,content)
    for folder in files[mode]: #individually listed items
        items = files[mode].get(folder)
        process_items(items,folder,content)
                    
                
    if True: #not mode == "UI":
        content.write("   ]\n")  
        content.write("}\n")           
   
def process_image(folder,sprite_name):
    #process an individual image for the current mode's color settings
    global mode
    split_name = sprite_name.split(".")
    short_name = split_name[0]
    if len(split_name)==2: #not translated
        image_string= start_path + folder + "/"+ short_name +".png"
    else: #translated
        image_string= start_path + folder + "/"+ short_name +"."+split_name[1]+".png"    
    print(folder+"/"+sprite_name)
    img = Image.open(image_string) 
    blank = Image.new("RGBA", (img.width, img.height), (255, 255, 255, 0))
    if colour_mode[mode] == "RGBA": 
        imgA = img.convert("RGBA")         
        Adata = imgA.load()       
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if Adata[x, y][3] !=0:
                     Adata[x, y] = colour_this(Adata[x, y])           
    else:
       imgA = img.convert("HSV") #colours   
       imgM = img.convert("RGBA") #mask  
       Adata = imgA.load()          
       for y in range(img.size[1]):
            for x in range(img.size[0]):
                Adata[x, y] = hue_this(Adata[x, y])         
       imgA =Image.composite(imgA, imgM, imgM)                              
    if in_dictionary(masks[mode], folder,short_name +".png"): #has a mask
        image_string = "./Masks/"+mode +"/"+folder+"/"+ short_name +".png"
        imgM = Image.open(image_string)
        imgA =Image.composite(imgA, blank, imgM)
    for un_mode in unmasks[mode]: #every image type we remove from this one
        if in_dictionary(masks[un_mode], folder,short_name +".png"): #has a mask to invert
            image_string = "./Masks/"+un_mode +"/"+folder+"/"+ short_name +".png"
            imgM = Image.open(image_string)    
            imgM = invert_alpha(imgM)
            imgA =Image.composite(imgA, blank, imgM)    
    if in_dictionary(overlays[mode], folder,short_name +".png"): #has extra images to put on top. Apply after all masks!
        if sprite_name=="TitleButtons.zh-CN.png" and mode =="UIframe":
            image_string = "./Overlays/"+mode +"/"+folder+"/"+ short_name +"_zh.png"
        else:  
            print("Overlaying "+sprite_name) 
            image_string = "./Overlays/"+mode +"/"+folder+"/"+ short_name +".png"
        imgM = Image.open(image_string)
        imgA =Image.alpha_composite(imgA, imgM)     
    
    if len(split_name)==2: #not translated
        if in_dictionary(files_translated, folder,sprite_name) and mode in UI_list: #add a file for english
            save_string = end_path[mode] + "assets/"+folder + "/"+ short_name +"_en.png" 
            imgA.save(save_string)     
        save_string = end_path[mode] + "assets/"+folder + "/"+ short_name +".png" 
        imgA.save(save_string)     
    else: #translated
        lang = split_name[1] #language name
        save_string = end_path[mode] + "assets/"+folder + "/"+ short_name +"_"+lang[0:2] +".png" 
        imgA.save(save_string)  
        
def process_rainbow():
    #A test of the current mode's colour settings on a rainbow image
    image_string= "./misc/rainbow.png"
    img = Image.open(image_string) 
    if colour_mode[mode] == "RGBA": 
        imgA = img.convert("RGBA")         
        Adata = imgA.load()       
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if Adata[x, y][3] !=0:
                     Adata[x, y] = colour_this(Adata[x, y])           
    else:
       imgA = img.convert("HSV") #colours   
       imgM = img.convert("RGBA") #mask  
       Adata = imgA.load()          
       for y in range(img.size[1]):
            for x in range(img.size[0]):
                Adata[x, y] = hue_this(Adata[x, y])         
       imgA =Image.composite(imgA, imgM, imgM)                              
    image_string = "./misc/rainbow_mask.png"
    imgM = Image.open(image_string)
    imgA =Image.alpha_composite(imgA, imgM)     
    
    save_string ="./misc/rainbow_processed.png"
    imgA.save(save_string)     
                      
    
def process_items_recolour(items,folder):
    #process every element of the list items, which is contained within folder, write code to content
    global mode
    for sprite_name in items:
        if not in_dictionary(files_not[mode],folder,sprite_name):
            split_name = sprite_name.split(".")
            if in_dictionary(files_translated, folder,sprite_name) and mode in UI_list: #has translations
                    split_name = sprite_name.split(".")
                    short_name = split_name[0]
                    for t in translations:
                        process_image_recolour(folder,short_name+"_"+t[0:2]+".png")
            process_image_recolour(folder,sprite_name)
        
def process_image_recolour(folder,sprite_name):
    #create an image for a full recolour 
    global mode, final_mode, have_image
    image_string= end_path[mode] +"assets/"+ folder + "/"+ sprite_name   
    print(folder+"/"+sprite_name)
    img = Image.open(image_string) 
    split_name = sprite_name.split(".")
    short_name = split_name[0] 
    if len(split_name) ==2 and in_dictionary(files_translated, folder,sprite_name) and mode in UI_list: #add a file for english
        save_string = end_path[final_mode] + "assets/"+folder + "/"+ short_name +"_en.png"   
    else:
        save_string = end_path[final_mode] + "assets/"+folder + "/"+ sprite_name  
    if folder in have_image.keys():
        if sprite_name in have_image[folder]: #we already have an image of this name
            img_base = Image.open(save_string)
            img =Image.alpha_composite(img_base, img)   
        else:
            have_image[folder] =have_image[folder]+[sprite_name]        
    else: #have_image doesn't have this folder 
        have_image[folder] = [sprite_name]   
        
    img.save(save_string)           
                   
        
def process_folder_recolour(mode_list):
    #create an entire recolour, layering together all the sub-images
    global mode, final_mode, have_image
    content = open(end_path[final_mode]+"content.json","w")
    print("writing to "+end_path[final_mode])
    content.write("{\n")
    content.write("   \"Format\": \"2.0.0\",\n")
    if final_mode =="UIrecolour":
        content.write("    \"ConfigSchema\":{\n")
        content.write("    \"EditCursor\": { \"AllowValues\": \"true, false\",\"Default\": \"true\"},\n")
        content.write("    },\n")   
    content.write("   \"Changes\": [\n")
    for mode in mode_list:
        for folder in folders[mode]: #simple folder
            print("1")
            items =list_directory(start_path+folder+'/',"*.png")  #all images in plants folder
            process_items_recolour(items,folder)             
        for folder in folders2[mode]: #nested folder
            print("2")
            print("folder "+folder)
            items =list_directory(start_path+folder+'/',"*.png")  #blah.thing.png
            process_items_recolour(items,folder)
        for folder in files[mode]: #individually listed items
            print("3")
            items = files[mode].get(folder)
            process_items_recolour(items,folder)
    mode = final_mode
    for folder in have_image.keys():
        for sprite_name in have_image[folder]:
            split_name = sprite_name.split("_")
            #underscores usually mean a translation but there's a few exceptions
            if (len(split_name) ==1) or (final_mode != "UIrecolour") or (sprite_name in ["font_bold.png", "Cursors_1_6.png", "map_summer.png","map_fall.png","map_winter.png"]):
                content.write(create_code(folder, sprite_name))  

    if final_mode == "UIrecolour":
        pos_string ="{ \"X\": 0, \"Y\": 0, \"Width\": 400, \"Height\": 184 }" 
        code = "      {\n"
        code+="         \"Action\": \"EditImage\",\n"
        code+="         \"Target\": \"Minigames/TitleButtons\",\n"
        code+="         \"FromFile\": \"assets/{{Target}}_{{language}}.png\",\n"
        code+="         \"FromArea\": "+pos_string+",\"ToArea\":  "+pos_string+",\n"
        code+= "      }\n"
        content.write(code) 
    content.write("   ]\n")  
    content.write("}\n")     

##Some code to test out the "plants" colour scheme on a rainbow. The result is stored in misc/rainbow_processed.png

#mode = "plants"
#process_rainbow()

##Code to create the Blue UI mod
mode = "UI"
process_folder()

##Create the submods for Weird Recolour

# mode = "ground"
# process_folder()
# mode = "plants"
# process_folder()
# mode = "fall"
# process_folder()
# mode = "wood"
# process_folder()
# mode = "flowers"
# process_folder()

##Putting everything together for the Weird Recolour mod
#final_mode = "recolour"
#process_folder_recolour(["ground","wood","plants","fall","flowers"])

##Create the submods for Starry Blue UI mod
mode = "UIbase"
process_folder()
mode = "UIframe"
process_folder()

##Put together Starry Blue UI
final_mode = "UIrecolour"
process_folder_recolour(["UIbase","UIframe"])

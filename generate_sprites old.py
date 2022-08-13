from __future__ import print_function
import sys
from PIL import Image
from PIL import ImageEnhance
import glob

### A script to generate a mod from unpacked content
### To run, open a terminal/command line from within this folder and type "python generate_sprites.py"
################
   
start_path = "./Content(unpacked)/"
end_path = "./[CP] Goth Recolour/"

def create_code(folder, sprite_name):
    #create the section of code overwriting sprite_name
    code =""
    split_name = sprite_name.split(".")
    short_name = split_name[0]
    if len(split_name)==2: #not translated
        code+="      {\n"
        code+="         \"Action\": \"EditImage\",\n"
        code+="         \"Target\": \""+folder + "/"+ short_name+"\",\n"
        code+="         \"FromFile\": \"assets/{{Target}}.png\"\n"
        code+="      },\n\n"
    else: #translated 
        code+=""   
    return code
   
def process_folder():
    content = open(end_path+"content.json","w")
    content.write("{\n")
    content.write("   \"Format\": \"1.27.0\",\n")
    content.write("   \"Changes\": [\n")

    folders = ["Animals","Buildings","LooseSprites","Maps","Minigames","TerrainFeatures","TileSheets","VolcanoLayouts"]
    for folder in folders:
        paths = [path.split("/")[3] for path in glob.glob(start_path+folder+"/*.png")] #blah.thing.png
        for sprite_name in paths:
            #process_image(folder,sprite_name)
            content.write(create_code(folder, sprite_name))       
    #dealing with nested folders
    folders = ["LooseSprites/Lighting", "Maps/Mines"]#["Characters/Farmer", "LooseSprites/Lighting", "Maps/Mines"]
    for folder in folders:
        paths = [path.split("/")[4] for path in glob.glob(start_path+folder+"/*.png")] #blah.thing.png
        for sprite_name in paths:
            #process_image(folder,sprite_name)
            content.write(create_code(folder, sprite_name))  
    content.write("   ]\n")  
    content.write("}\n")       
           
def process_image(sprite_type,sprite_name):
    image_string= start_path + sprite_type + "/"+ sprite_name +".png"
    img = Image.open(image_string)
    imgA = img.convert("RGBA")
    Adata = imgA.load()     
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if Adata[x, y][3] !=0:
                oldR = Adata[x, y][0]
                oldG = Adata[x, y][1]
                oldB = Adata[x, y][2]
                oldV=max(oldR, oldG, oldB)
                newR = (oldG+oldB)/2
                newG = (oldR+oldB)/2
                newB = max(oldB, (oldR+oldG)/2)
                
                Adata[x, y] = (newR,newG,newB,Adata[x, y][3])
    save_string = end_path + "assets/"+sprite_type + "/"+ sprite_name  +".png"       
    imgA.save(save_string) 
    
process_folder()
#process_image("TerrainFeatures","tree1_spring.png")
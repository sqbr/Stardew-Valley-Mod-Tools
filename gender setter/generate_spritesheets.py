from __future__ import print_function
import sys
import math
from PIL import Image
from PIL import ImageEnhance
import glob

### A script to generate opposite gender sprite sheets
### To run, open a terminal/command line from within this folder and type "python generate_spritesheets.py"
################
  
## general data functions  
def list_directory(directory,pattern):
    #lists every element of a directory matching the pattern
    return [path.split("/").pop() for path in glob.glob(directory+pattern)]
  
def sort(l):
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
    
## General data    

spouse_list = ["Abigail","Alex","Elliott","Emily","Haley","Harvey","Leah","Maru","Penny","Sam","Sebastian","Shane"]
orig_gender_dict = {"ProfessorSnail": "Male","Abigail":"Female","Alex":"Male","Birdie":"Female","Bouncer":"Male","Caroline":"Female","Charlie":"Female","Clint":"Male","Demetrius":"Male","Dwarf":"Male","Elliott":"Male","Emily":"Female","Evelyn":"Female","George":"Male","Gil":"Male","Governor":"Male","Grandpa":"Male","Gunther":"Male","Gus":"Male","Haley":"Female","Harvey":"Male","Henchman":"Male","Jas":"Female","Jodi":"Female","Kent":"Male","Krobus":"Male","Leah":"Female","Leo":"Male","Lewis":"Male","Linus":"Male","Marcello":"Male","Marlon":"Male","Marnie":"Female","Maru":"Female","MisterQi":"Male","Morris":"Male","OldMariner":"Male","Pam":"Female","Penny":"Female","Pierre":"Male","Robin":"Female","Sam":"Male","Sandy":"Female","Sebastian":"Male","Shane":"Male","Vincent":"Male","Willy":"Male","Wizard":"Male",}

name_list1= ["Abigail","Alex","Birdie","Caroline","Charlie","Clint","Demetrius","Dwarf", "Elliott","Emily","Evelyn","George","Gil","Governor","Grandpa","Gunther","Gus","Haley","Harvey","Henchman","Jas","Jodi","Kent","Leah","Leo","Lewis","Linus","Krobus", "Marcello","Marlon","Marnie","Maru","MrQi","Morris","OldMariner","Pam","Penny","Pierre",]
name_list2= ["Robin","Sam","Sandy","Sebastian","Shane","Vincent","Willy","Wizard",]
name_list = name_list1 + ["ProfessorSnail","ParrotBoy","SafariGuy"]+name_list2
possible_names = []
for name in name_list:
    for e in ["", "_Darker", "_Wheelchair","_Islander", "_IslanderChild"]:
        possible_names.append(name+e+".png")

start_path = "../../Gender Setter/[CP] Gender Setter/assets/Characters/"
end_path = "../../Gender Setter/[CP] Gender Setter/Variants/Characters/"
## Data processing  

def genderswap(gender):
    if gender =="Male":
        return "Female"
    elif gender =="Female":
        return "Male"   
    else:
        return gender    
       
def process_folder():
    for name in spouse_list:
        o_gender = orig_gender_dict[name]
        process_image(name,o_gender)
    for name in ["Elliott"]:
        o_gender = orig_gender_dict[name]
        process_image(name+"_Darker",o_gender)    
    for name in ["Leah"]:
        o_gender = orig_gender_dict[name]
        process_image(name+"_Wheelchair",o_gender)        

def process_image(name,o_gender):
    img = Image.open(start_path+name+".png")

    box1 = (0,288,47,319)
    cut1 = img.crop(box1)
    box2 = (0,384,47,415)
    cut2 = img.crop(box2)

    img.paste(cut1,box2)
    img.paste(cut2,box1)

    if o_gender=="Male":
        save_string = name+"_f"
    else:
        save_string = name+"_m"   
    img.save(end_path+save_string+".png")  

def make_screenshots():
    images =sort(list_directory("./assets/Characters/","*.png"))  #all images in Characters
    #24 beach, 76 non-beach
    print("images "+str(len(images)))   
    beach_items = []
    non_beach = []
    for i in images:
        if i.count("Beach")>0:
            beach_items.append(i)
        else:
            if i in possible_names and i.count("Grandpa")==0:
                non_beach.append(i)                
    width = 12
    height = 2
    screenshot = Image.new("RGBA", (16*width, 32*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > (len(beach_items)-1):
                break
            current_image = beach_items[current] 
            img= Image.open(start_path+current_image)
            char = img.crop((0,0,16,32))
            screenshot.paste(char,(16*i,32*j,16*(i+1),32*(j+1))) 
    screenshot.save("./images/beach_sprites.png")         
    width = 13
    height = 4
    screenshot = Image.new("RGBA", (16*width, 32*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > (len(non_beach)-1):
                break
            current_image = non_beach[current] 
            img= Image.open(start_path+current_image)
            if current_image in ["Krobus.png","Dwarf.png"]:
                h = 24
            else:
                h = 32  
            char = img.crop((0,0,16,h))
            screenshot.paste(char,(16*i,32*j+(32-h),16*(i+1),32*(j+1))) 
    screenshot.save("./images/sprites.png")    

    path = "./assets/Portraits/"
    images =sort(list_directory(path,"*.png"))
    print("images "+str(len(images)))    
    non_beach = []
    beach_items = []
    for i in images:
        if i.count("Beach")>0:
            beach_items.append(i)
        else:
            if i in possible_names:
                non_beach.append(i)   
    width = 7
    height = 3
    screenshot = Image.new("RGBA", (64*width, 64*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > (len(beach_items)-1):
                break
            current_image = beach_items[current] 
            img= Image.open(path+current_image)
            char = img.crop((0,0,64,64))
            screenshot.paste(char,(64*i,64*j,64*(i+1),64*(j+1))) 
    screenshot.save("./images/beach_portraits.png")    
            
    width = 14
    height = 4
    screenshot = Image.new("RGBA", (64*width, 64*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > (len(non_beach)-1):
                break
            current_image = non_beach[current] 
            img= Image.open(path+current_image)
            char = img.crop((0,0,64,64))
            screenshot.paste(char,(64*i,64*j,64*(i+1),64*(j+1))) 
    screenshot.save("./images/portraits.png")    

    path = "./assets/Androgynous/"
    images =sort(list_directory(path,"*.png"))
    print("images "+str(len(images)))    
    non_beach = []
    beach_items = []
    for i in images:
        if i.count("Beach")>0:
            beach_items.append(i)
        else:
            if i in possible_names:
                non_beach.append(i)   
    width = 6
    height = 4
    screenshot = Image.new("RGBA", (256*width, 256*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > (len(beach_items)-1):
                break
            current_image = beach_items[current] 
            img= Image.open(path+current_image)
            char = img.crop((0,0,256,256))
            screenshot.paste(char,(256*i,256*j,256*(i+1),256*(j+1))) 
    screenshot.save("./images/beach_HD.png")    
            
    width = 6
    height = 4
    screenshot = Image.new("RGBA", (256*width, 256*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > (len(non_beach)-1):
                break
            current_image = non_beach[current] 
            img= Image.open(path+current_image)
            char = img.crop((0,0,256,256))
            screenshot.paste(char,(256*i,256*j,256*(i+1),256*(j+1))) 
    screenshot.save("./images/HD.png")    

        
#process_image("Abigail")
make_screenshots()
#process_folder()

 
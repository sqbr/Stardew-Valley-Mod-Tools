from __future__ import print_function
from fileinput import filename
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

name_list1= ["Abigail","Alex","Birdie","Bouncer", "Caroline","Clint","Demetrius","Dwarf", "Elliott","Emily","Evelyn","George","Governor","Gunther","Gus","Haley","Harvey","Henchman","Jas","Jodi","Kent","Leah","Lewis","Linus","Krobus", "Marcello","Marlon","Marnie","Maru","MrQi","Morris","Mariner","Pam","Penny","Pierre",]
name_list2= ["Robin","Sam","Sandy","Sebastian","Shane","Vincent","Willy","Wizard",]
name_list = name_list1 + ["ParrotBoy","SafariGuy"]+name_list2
beach_bodies = ["Abigail","Alex","Caroline","Clint","Elliott","Emily","Haley","Harvey","Jodi","Leah","Marnie","Maru","Pam","Penny","Pierre","Robin","Sam","Sebastian","Shane"]

darker_chars = ["Marnie","Jas","Elliott","Grandpa","Sandy","Caroline","ParrotBoy","Birdie","SafariGuy"]
wheelchair_chars = ["Leah"]
islander_chars = ["Birdie","SafariGuy","ParrotBoy"]

start_path = "../../Gender Setter/[CP] Gender Setter/assets/"
end_path = "../../Gender Setter/[CP] Gender Setter/Variants/Characters/"

no_portrait_list = ["Bear","LeahEx","Marcello","Mariner","KrobusRaven","ClothesTherapyCharacters","Shane_JojaMart","Toddler","Toddler_girl_dark","Toddler_dark","Toddler_girl","Baby","WeddingOutfits","Baby_dark","SeaMonsterKrobus","Gourmand",]

portrait_list = ["Gil","Maru_Hospital", "Krobus_Trenchcoat","Grandpa"]

for name in name_list:
    if name not in no_portrait_list:
        portrait_list.append(name)
        
other_portraits = ["AnsweringMachine", ]          
## Data processing  

def genderswap(gender):
    if gender =="Male":
        return "Female"
    elif gender =="Female":
        return "Male"   
    else:
        return gender    
       
def process_folder():
    #outdated
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
    img = Image.open(start_path+"Characters/"+name+".png")

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

def make_screenshot(width, height, filepath, isBeach, image_type):

    if image_type == "HD":
        image_height = 256
        image_width = 256
    elif image_type == "sprites":
        image_height = 32
        image_width = 16    
    else:
        image_height = 64
        image_width = 64 

    if isBeach:
        filelist = beach_bodies
    elif image_type == "sprites":
        filelist = name_list
    else:
        filelist = portrait_list         


    screenshot = Image.new("RGBA", (image_width*width, image_height*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > len(filelist) - 1:
                break
            current_image = filelist[current] 
            if isBeach:
                current_image+="_Beach"
            img= Image.open(filepath+current_image+".png")
            h = image_height
            if image_type == "sprites":
                if (current_image in ["Krobus","Dwarf"]):
                    h = 24
            corner = img.crop((0,0,image_width,h))
            screenshot.paste(corner,(image_width*i,image_height*j+(image_height-h),image_width*(i+1),image_height*(j+1))) 
    save_name = "./images/"
    save_name+= image_type
    if isBeach:
       save_name+= "_beach"   
    save_name += ".png"           
    screenshot.save(save_name)   

def make_comparison_screenshot(filepath, image_type):
    
    if image_type == "HD":
        image_height = 256
        image_width = 256
    elif image_type == "sprites":
        image_height = 32
        image_width = 16  
    else:
        image_height = 64
        image_width = 64 

    image_lists = [darker_chars,islander_chars]
    all_variants = darker_chars
    variant_list = ["Darker","Islander"]
    if image_type == "sprites":
        image_lists = [darker_chars,islander_chars, wheelchair_chars]
        variant_list += ["Wheelchair"] 
        all_variants = darker_chars+ wheelchair_chars
    #print(str(all_variants))

    suffix = ""

    for n in range(2):#beach or non beach
        screenshot = Image.new("RGBA", (image_width*4, image_height*len(all_variants)+1))

        for j in range(len(all_variants)):
            i = 0
            current_image = all_variants[j]  
            #print(current_image)
            image_string =filepath+current_image 
            img= Image.open(image_string+suffix+".png")  
            corner = img.crop((0,0,image_width,image_height)) 
            screenshot.paste(corner,(image_width*i,image_height*j,image_width*(i+1),image_height*(j+1))) 
            for v in range(len(variant_list)): #which variant
                #print("V: "+str(v)+" vlist " + str(image_lists[v]))
                if current_image in image_lists[v]:
                    i+=1
                    img= Image.open(filepath+"Variants/"+variant_list[v]+"/"+current_image+suffix+".png")  
                    corner = img.crop((0,0,image_width,image_height)) 
                    screenshot.paste(corner,(image_width*i,image_height*j,image_width*(i+1),image_height*(j+1))) 
                
        save_name = "./images/" 
        save_name += "compare_"  
        save_name+= image_type
        save_name += ["","_beach"][n]
        save_name += ".png"           
        screenshot.save(save_name) 

        #setup for next loop, over beach images
        all_variants = list(set(all_variants) & set(beach_bodies))
        #print(str(all_variants)) 
        suffix = "_Beach"



def set_folders(path): 
    images =sort(list_directory(path,"*.png"))  #all images in path
    print("images "+str(len(images)))   
    beach_items = []
    non_beach = []
    for i in images:
        if i.count("Beach")>0:
            beach_items.append(i)
        else:
            non_beach.append(i)   
    return [beach_items,non_beach]                  


def make_screenshots():
    path = "../../Gender Setter/[CP] Gender Setter/assets/Portraits/"
    
    make_screenshot(width =7, height =3, filepath = path, isBeach = True, image_type = "portraits")        
            
    make_screenshot(width =14, height =4, filepath = path, isBeach = False, image_type = "portraits")        

    make_comparison_screenshot(filepath = path, image_type = "portraits")   

    path = "../../[CP] Configurable HD Portraits/assets/Portraits/Androgynous/"

    make_screenshot(width =6, height =5, filepath = path, isBeach = True, image_type = "HD")        
            
    make_screenshot(width =14, height =4, filepath = path, isBeach = False, image_type = "HD")   

    make_comparison_screenshot(filepath = path, image_type = "HD")   
        
    path = "../../Gender Setter/[CP] Gender Setter/assets/Characters/"

    make_screenshot(width =12, height =2, filepath = path, isBeach = True, image_type = "sprites")        
            
    make_screenshot(width =13, height =4, filepath = path, isBeach = False, image_type = "sprites")        
      
    make_comparison_screenshot(filepath = path, image_type = "sprites")   

def copy_image(name, start, end):
    img= Image.open(start+name+".png") 
    img.save(end+name+".png")      

def location(variant, type):
    #location of the image we're using 
    v_string = ""
    if variant != "":
        v_string = "Variants/" + variant + "/"
        if isHD:
            if variant in ["Darker","Islander","Wheelchair"]:
                v_string = "Androgynous/Variants/"+ variant + "/"
            elif variant =="Androgynous":
                 v_string = "Androgynous/"         
    if type == "sprite":
        return "assets/Characters/"+v_string 
    else:    
       return "assets/Portraits/"+v_string     

def copy_image_line(name, type,variant):
    if type =="sprite" and name=="Gil":
        return
    start= "../../Gender Setter/[CP] Gender Setter/"
    if isHD:
        if type =="portrait":
            start= "../../Gender Setter HD/[CP] Gender Setter/"
        end= "../../[CP] Configurable HD Portraits/"
    else:  
        end= "../../[CP] Androgynous Villagers/"  
    if type =="sprite" and isHD:
        full_start = start+"assets/Characters/"
        if variant !="Androgynous":
            full_start += "Variants/"+variant + "/"
    else:       
        full_start = start+location(variant, type)
    copy_image(name, full_start, end+location(variant, type))
    if name in beach_bodies:
        copy_image(name+"_Beach", full_start, end+location(variant, type))

def transfer_images():
    for name in other_portraits:
        if not isHD:
            copy_image_line(name, "portrait", "")     
    for name in portrait_list:
        if isHD:
            copy_image_line(name, "sprite", "Androgynous")
            copy_image_line(name, "portrait", "Androgynous")   
        else:    
            copy_image_line(name, "sprite", "")   
            copy_image_line(name, "portrait", "")   
        if name in darker_chars:
            copy_image_line(name, "portrait", "Darker") 
            copy_image_line(name, "sprite", "Darker")      
        if name in wheelchair_chars:
            copy_image_line(name, "sprite", "Wheelchair") 
        if name in islander_chars:
            copy_image_line(name, "portrait", "Islander")  
            copy_image_line(name, "sprite", "Islander")               
    for name in no_portrait_list:   
        if isHD: 
            copy_image_line(name, "sprite", "Androgynous")
        else:
            copy_image_line(name, "sprite", "")        
        

#process_image("Abigail")
make_screenshots()

for isHD in [True,False]:
    transfer_images()
#process_folder()

 
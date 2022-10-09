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

def make_screenshot(width, height, filename,  filepath, filelist, isBeach, image_type):

    if image_type == "HD":
        image_height = 256
        image_width = 256
    elif image_type == "sprites":
        image_height = 32
        image_width = 16    
    else:
        image_height = 64
        image_width = 64 

    screenshot = Image.new("RGBA", (image_width*width, image_height*height))
    for i in range(width):
        for j in range(height):
            current = j*width+i
            if current > len(filelist) - 1:
                break
            current_image = filelist[current] 
            img= Image.open(filepath+current_image)
            h = image_height
            if image_type == "sprites":
                if (current_image in ["Krobus.png","Dwarf.png"]):
                    h = 24
            corner = img.crop((0,0,image_width,h))
            screenshot.paste(corner,(image_width*i,image_height*j+(image_height-h),image_width*(i+1),image_height*(j+1))) 
    save_name = "./images/"
    if isBeach:
       save_name+= "beach_"   
    save_name += filename
    save_name+= image_type
    save_name += ".png"           
    screenshot.save(save_name)   

def make_comparison_screenshot(filename,  filepath, image_type):

    darker_images = set_folders(filepath+"Variants/Darker/")
    wheelchair_images = set_folders(filepath+"Variants/Wheelchair")
    islander_images = set_folders(filepath+"Variants/Islander")
    
    if image_type == "HD":
        image_height = 256
        image_width = 256
    elif image_type == "sprites":
        image_height = 32
        image_width = 16  
        wheelchair_images = [["Leah_Beach.png"],["Leah.png"]]  
    else:
        image_height = 64
        image_width = 64 

    image_lists = [list(set(darker_images[0]+ wheelchair_images[0] + islander_images[0])), list(set(darker_images[1]+ wheelchair_images[1] + islander_images[1]))]                

    for n in range(1):
        current_list = image_lists[n]
        screenshot = Image.new("RGBA", (image_width*4, image_height*len(current_list)+1))

        for j in range(len(current_list)-1):
            i = 0
            current_image = current_list[j]  
            img= Image.open(filepath+current_image)  
            corner = img.crop((0,0,image_width,image_height)) 
            screenshot.paste(corner,(image_width*i,image_height*j,image_width*(i+1),image_height*(j+1))) 
            for variant in ["Darker","Islander","Wheelchair"]:
                if current_image in set_folders(filepath+"Variants/"+variant+"/")[n]:
                    i+=1
                    img= Image.open(filepath+"Variants/"+variant+"/"+current_image)  
                    corner = img.crop((0,0,image_width,image_height)) 
                    screenshot.paste(corner,(image_width*i,image_height*j,image_width*(i+1),image_height*(j+1))) 
                
        save_name = "./images/" 
        save_name += "compare_"  
        save_name += ["beach_",""][n]
        save_name += filename
        save_name+= image_type
        save_name += ".png"           
        screenshot.save(save_name) 
        suffix = "" 



def set_folders(path): 
    images =sort(list_directory(path,"*.png"))  #all images in path
    print("images "+str(len(images)))   
    beach_items = []
    non_beach = []
    for i in images:
        if i.count("Beach")>0:
            beach_items.append(i)
        else:
            if i in possible_names:
                non_beach.append(i)   
    return [beach_items,non_beach]                  


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

    make_screenshot(width =12, height =2, filename = "", filepath = start_path, filelist = beach_items, isBeach = True, image_type = "sprites")        
            
    make_screenshot(width =13, height =4, filename = "", filepath = start_path, filelist = non_beach, isBeach = False, image_type = "sprites")        
 

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

    make_screenshot(width =7, height =3, filename = "", filepath = path, filelist = beach_items, isBeach = True, image_type = "portraits")        
            
    make_screenshot(width =14, height =4, filename = "", filepath = path, filelist = non_beach, isBeach = False, image_type = "portraits")        


    path = "./assets/Androgynous/"
    [beach_items,non_beach] = set_folders(path)

    make_screenshot(width =6, height =5, filename = "", filepath = path, filelist = beach_items, isBeach = True, image_type = "HD")        
            
    make_screenshot(width =14, height =4, filename = "", filepath = path, filelist = non_beach, isBeach = False, image_type = "HD")   

    make_comparison_screenshot(filename = "", filepath = path, image_type = "HD")   
        
    path = "./assets/Characters/Androgynous/"   
    [beach_items,non_beach] = set_folders(path) 

    make_screenshot(width =12, height =2, filename = "", filepath = path, filelist = beach_items, isBeach = True, image_type = "sprites")        
            
    make_screenshot(width =13, height =4, filename = "", filepath = path, filelist = non_beach, isBeach = False, image_type = "sprites")        
      
    make_comparison_screenshot(filename = "", filepath = path, image_type = "sprites")   
        
#process_image("Abigail")
make_screenshots()
#process_folder()

 
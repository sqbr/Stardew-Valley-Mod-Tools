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
   
start_path = "../../Genderiser/assets/Characters/"

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
    img.save(start_path+save_string+".png")  
        
#process_image("Abigail")
process_folder()

 
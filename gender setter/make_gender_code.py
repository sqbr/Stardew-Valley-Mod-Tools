from __future__ import print_function
import math
import glob
import random
from re import S
from xml.etree.ElementTree import TreeBuilder

### A script to generate a mod from unpacked content
### To run, open a terminal/command line from within this folder and type "python make_gender_code.py"
###############

def end_path():
    if isHD:
        if isGS:
            return "../../Gender Setter HD/[CP] Gender Setter/"
        else:
            return "../../[CP] Configurable HD Portraits/"   
    else:
        if isGS:
            return "../../Gender Setter/[CP] Gender Setter/"
        else:
            return "../../[CP] Androgynous Villagers/" 

  
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

def make_p_dict(pronoun, dict1,dict2):
    for k in dict2.keys():
        dict1[k] = dict2[k]
    dict1["They"] = pronoun.lower()    
    for w in ["They","Them","Their"]:    
        dict1[w+"U"] = dict1[w].capitalize()
    return dict1    

    
## General data       
   
## Original data

name_list1= ["Abigail","Alex","Birdie","Bouncer","Caroline","Charlie","Clint","Demetrius","Dwarf","Elliott","Emily","Evelyn","George","Gil","Governor","Grandpa","Gunther","Gus","Haley","Harvey","Henchman","Jas","Jodi","Kent","Krobus","Leah","Leo","Lewis","Linus","Marcello","Marlon","Marnie","Maru","MisterQi","Morris","OldMariner","Pam","Penny","Pierre",]
name_list2= ["Robin","Sam","Sandy","Sebastian","Shane","Vincent","Willy","Wizard",]

name_list = name_list1 + ["ProfessorSnail"]+name_list2 #for pronouns etc

sprite_list = sorted(name_list + ["Bear"])
sprite_list.remove("Gil")

beach_bodies = ["Abigail","Alex","Caroline","Clint","Elliott","Emily","Haley","Harvey","Jodi","Leah","Marnie","Maru","Pam","Penny","Pierre","Robin","Sam","Sebastian","Shane"]
spouse_list = ["Abigail","Alex","Elliott","Emily","Haley","Harvey","Leah","Maru","Penny","Sam","Sebastian","Shane"]

no_portrait_list = ["Marcello","OldMariner"]
other_portraits = ["Bear", "AnsweringMachine"]

portrait_list = ["AnsweringMachine"]

for name in sprite_list:
    if name not in no_portrait_list and name !="Charlie":
        portrait_list.append(name)

portrait_list = sorted(portrait_list)
extras = {"Maru":"Maru_Hospital", "Krobus": "Krobus_Trenchcoat"}
possession_dict= {"ProfessorSnail": "'s","Abigail":"'s","Alex":"'s","Birdie":"'s","Bouncer":"'s","Caroline":"'s","Charlie":"'s","Clint":"'s","Demetrius":"'","Dwarf":"'s","Elliott":"'s","Emily":"'s","Evelyn":"'s","George":"'s","Gil":"'s","Governor":"'s","Grandpa":"'s","Gunther":"'s","Gus":"'","Haley":"'s","Harvey":"'s","Henchman":"'s","Jas":"'","Jodi":"'s","Kent":"'s","Krobus":"'","Leah":"'s","Leo":"'s","Lewis":"'","Linus":"'","Marcello":"'s","Marlon":"'s","Marnie":"'s","Maru":"'s","MisterQi":"'s","Morris":"'","OldMariner":"'s","Pam":"'s","Penny":"'s","Pierre":"'s","Robin":"'s","Sam":"'s","Sandy":"'s","Sebastian":"'s","Shane":"'s","Vincent":"'s","Willy":"'s","Wizard":"'",}
orig_gender_dict = {"ProfessorSnail": "Male","Abigail":"Female","Alex":"Male","Birdie":"Female","Bouncer":"Male","Caroline":"Female","Charlie":"Female","Clint":"Male","Demetrius":"Male","Dwarf":"Male","Elliott":"Male","Emily":"Female","Evelyn":"Female","George":"Male","Gil":"Male","Governor":"Male","Grandpa":"Male","Gunther":"Male","Gus":"Male","Haley":"Female","Harvey":"Male","Henchman":"Male","Jas":"Female","Jodi":"Female","Kent":"Male","Krobus":"Male","Leah":"Female","Leo":"Male","Lewis":"Male","Linus":"Male","Marcello":"Male","Marlon":"Male","Marnie":"Female","Maru":"Female","MisterQi":"Male","Morris":"Male","OldMariner":"Male","Pam":"Female","Penny":"Female","Pierre":"Male","Robin":"Female","Sam":"Male","Sandy":"Female","Sebastian":"Male","Shane":"Male","Vincent":"Male","Willy":"Male","Wizard":"Male",}
orig_pronoun_dict ={
    "Male": "He",
    "Female": "She",
}



birthday_dict = {"Abigail": "fall 13",
  "Alex": "summer 13",
  "Caroline": "winter 7",
  "Clint": "winter 26",
  "Demetrius": "summer 19",
  "Dwarf": "summer 22",
  "Elliott": "fall 5",
  "Emily": "spring 27",
  "Evelyn": "winter 20",
  "George": "fall 24",
  "Gus": "summer 8",
  "Haley": "spring 14",
  "Harvey": "winter 14",
  "Jas": "summer 4",
  "Jodi": "fall 11",
  "Kent": "spring 4",
  "Krobus": "winter 1",
  "Leah": "winter 23",
  "Leo": "summer 26",
  "Lewis": "spring 7",
  "Linus": "winter 3",
  #"Marlon": "winter 19",
  "Marnie": "fall 18",
  "Maru": "summer 10",
  "Pam": "spring 18",
  "Penny": "fall 2",
  "Pierre": "spring 26",
  "Robin": "fall 21",
  "Sam": "summer 17",
  "Sandy": "fall 15",
  "Sebastian": "winter 10",
  "Shane": "spring 20",
  "Vincent": "spring 10",
  "Willy": "summer 24",
  "Wizard": "winter 17"}

variables_dict = {"Child2": "Godchild", "Child3": "nibling", 
    "GenderUC":"They","GenderLC":"They","PronounUC1":"_Them","PronounLC1":"Them","PronounUC2":"_Their","PronounLC2":"Their","PronounLC3":"Theirs",
    "GenderLC2":"Adult","GenderLC3":"Guy","GenderLC4":"Kid","Child":"Child","Sibling":"Sibling","Relation":"_Auncle","ParentUC":"Parent","ParentLC":"Parent","MarriedUC":"Spouse","MarriedLC":"Spouse","Marital":"Mx","Elder":"_Grandparent",}

nb_names_dict = {"Abigail":"Ashley","Alex":"Alex","Birdie":"Birdie","Bouncer":"Bouncer","Caroline":"Cary","Charlie":"Charley","Clint":"Coby","Demetrius":"Dubaku","Dwarf":"Smoluanu","Elliott":"Eden","Emily":"Elery","Evelyn":"Evelyn","George":"Georgie","Gil":"Gili","Governor":"Governor","Grandpa":"Grandie","Gunther":"Greer","Gus":"Gabi","Haley":"Hadyn","Harvey":"Harper","Henchman":"Guard","Jas":"Jay","Jodi":"Joey","Kent":"Kim","Krobus":"Krobus","Leah":"Leigh","Leo":"Lee","Lewis":"Lou","Linus":"Lucky","Marcello":"Modeste","Marlon":"Merlyn","Marnie":"Martie","Maru":"Maru","MisterQi":"Qi","Morris":"Moran","OldMariner":"Old Mariner","Pam":"Pat","Penny":"Pip","Pierre":"Paget","ProfessorSnail":"Professor Snail","Robin":"Robin","Sam":"Sam","Sandy":"Sandy","Sebastian":"September","Shane":"Shae","Vincent":"Vinnie","Willy":"Willie","Wizard":"Morgan",}

variants_dict = {"Harvey": ["Shaved"],"Emily": ["LongSleeved"], "Pam": ["Young"], "Linus": ["Coat"],"Wizard": ["Young"]}
genderswap_list = ["Alex","Elliott","Harvey","Sam", "Shane","Sebastian","Wizard","Willy"]
   

birthday_code = True
custom_possession = False

## New data
genders = ["Male","Female","Neutral"]
pronouns = ["He","She","They","They (singular)","It","Xe","Fae","E"]
singular_words = { 
    "Are":"is",
    "Were":"was",
    "Have":"has",
    "Re":"'s",
    "Ve":"'s",
    "S":"s",
    "Es":"es"}
plural_words = {
    "Are":"are",
    "Were":"were",
    "Have":"have",
    "Re":"'re",
    "Ve":"'ve",
    "S":"",
    "Es":""}
pronoun_words = {
    "She": make_p_dict("She",{"Them":"her","Their":"her","Theirs":"hers","Themself":"herself"} ,singular_words),
    "He": make_p_dict("He", {"Them":"him","Their":"his","Theirs":"his","Themself":"himself"}, singular_words),
    "They": make_p_dict("They", {"Them":"them", "Their":"their","Theirs":"theirs","Themself":"themself"}, plural_words),
    "They (singular)": make_p_dict("They", {"Them":"them", "Their":"their","Theirs":"theirs","Themself":"themself"},  singular_words),
    "It": make_p_dict("It", {"Them":"it","Their":"its","Theirs":"its","Themself":"itself"}, singular_words),
    "Xe": make_p_dict("Xe", {"Them":"xem","Their":"xyr","Theirs":"xyrs","Themself":"xemself"}, singular_words),
    "Fae": make_p_dict("Fae", {"Them":"faer","Their":"faer","Theirs":"faers","Themself":"faerself"}, singular_words),
    "E": make_p_dict("E", {"Them":"em","Their":"eir","Theirs":"eirs","Themself":"emself"}, singular_words),
    "Ze": make_p_dict("Ze", {"Them":"hir","Their":"hir","Theirs":"hirs","Themself":"hirself"}, singular_words),
}

gender_words = {
    "Female": {"Adult":"woman","Guy":"girl","Kid":"girl","Child":"daughter","Sibling":"sister","Nibling":"niece","Auncle":"aunt","AuncleU":"Aunt","Parent":"mother","ParentName":"mom","ParentU":"Mom","Spouse":"wife","SpouseU":"Wife","Mx":"Mrs.","Grandparent":"Granny"},
    "Male": {"Adult":"man","Guy":"guy","Kid":"boy","Child":"son","Sibling":"brother","Nibling":"nephew","Auncle":"uncle","AuncleU":"Uncle","Parent":"father","ParentName":"dad","ParentU":"Dad","Spouse":"husband","SpouseU":"Husband","Mx":"Mr.","Grandparent":"Grandpa"},
    "Neutral": {"Adult":"person","Guy":"person","Kid":"kid","Child":"child","Sibling":"sibling","Nibling":"nibling","Auncle":"auncle","AuncleU":"Auncle","Parent":"parent","ParentU":"Parent","ParentName":"parent","Spouse":"spouse","SpouseU":"Spouse","Mx":"Mx.","Grandparent":"Grandie"},

}

neutralexceptions_dict = {"VincentGuy":"kid","EvelynGrandparent": "Grandie {{EvelynName}}", "GeorgeGrandparent": "Grandie {{GeorgeName}}"}
for name in ["Pierre", "Caroline", "Kent","Jodi","Robin","Demetrius","Evelyn",]:
    neutralexceptions_dict[name+"ParentName"] = "parent "+"{{"+name+"Name}}"

gender_exceptions = { 
    "Female": {"LewisMx": "Ms.", "MorrisMx": "Ms.","PennyMx": "Miss","BirdieGuy": "lady","GovernorAdult": "girl"},
    "Male": {"PennyMx": "Mister", "BirdieGuy": "man", "GovernorAdult": "guy"},
    "Neutral": neutralexceptions_dict
    }

darker_chars = ["Marnie","Jas","Elliott","Grandpa","Sandy","Caroline","Leo","Birdie","ProfessorSnail"]
wheelchair_chars = ["Leah"]
islander_chars = ["Birdie","ProfessorSnail","Leo"]

all_variants = darker_chars + wheelchair_chars + islander_chars 
## Data processing   

def realname(name):
    #real name original of character, removes spaces and aliases
    if name =="MisterQi":
        return "Mister Qi"
    elif name =="OldMariner": 
            return "Old Mariner"   
    elif name =="Wizard":
        return "Magnus"
    else:
        return name   

def possession(name):
    #whetehr to use name's or name'
    if name[len(name)-1] =='s':
        return "'"
    else:
        return "'s"            

def spritename(name):
    #name of sprite art file for character
    if name =="MisterQi":
        return "MrQi"
    elif name =="OldMariner": 
        return "Mariner"  
    elif name == "ProfessorSnail":
        return "SafariGuy"    
    elif name == "Leo":
        return "Parrotboy"             
    elif name in ["Charlie","Gil"]:
        return "None"
    else:
        return name  

def portraitname(name):
    #name of portrait art file for character
    if name == "Gil":
        return name
    else:
        return spritename(name)        

def artname(name, type):
    if type =="sprite":
        return spritename(name)   
    else:
        return portraitname(name)

def genderswap(gender):
    if gender =="Male":
        return "Female"
    elif gender =="Female":
        return "Male"   
    else:
        return gender                        

def create_config(current_gender):
    #create config file. Current_gender is what gender to write the characters as, write_variant is a boolean saying whether to write to one of the variant configs
    path = end_path()+"config.json"
    if isGS:
        if current_gender == "Neutral":
            path = end_path()+"/Variants/config all non-binary.json"
        elif current_gender == "Male":
            path = end_path()+"/Variants/config all male.json"  
        elif current_gender == "Female":
            path = end_path()+"/Variants/config all female.json"               
    content = open(path,"w")
    content.write("{\n")
    if isHD:
        content.write("  \"Genderbent Bachelors\": \"Classic\",\n")   
    if current_gender == "None":
        edit_bool = "false"
    else:
        edit_bool = "true"   
    if isGS:
        content.write("  \"MiscTextEdits\": \""+edit_bool+"\",\n")  
    content.write("  \"MiscImageEdits\": \""+edit_bool+"\",\n")
    content.write("\n")
    if isGS:
        if current_gender in ["Neutral","Test"] :
            content.write("  \"FarmerGender\": \"Neutral\",\n")    
            content.write("  \"FarmerPronoun\": \"They\",\n")  
        else:
            content.write("  \"FarmerGender\": \"false\",\n")    
            content.write("  \"FarmerPronoun\": \"They\",\n")   
    content.write("\n")        
    for name in name_list:

        o_gender = orig_gender_dict[name]

        changing_char = False 
        gender = o_gender   
        pronoun = orig_pronoun_dict[o_gender] 
        if isHD:
                changesprite =  orig_gender_dict[name]
        else:
                changesprite = "false"
        new_name = name
        
        if current_gender =="Neutral":
            gender = "Neutral"
            pronoun = "They" 
            new_name =  nb_names_dict[name]  
            if isHD:
                changesprite = "Androgynous"
            else:
               changing_char = True       
        elif current_gender =="Test":
            gender = "Neutral"
            pronoun = random.choice(pronouns)  
            new_name =  nb_names_dict[name]  
            if name in darker_chars:
                changesprite = "Darker"
            elif name in wheelchair_chars:
                changesprite = "Wheelchair"       
            elif name in islander_chars:
                changesprite = "Islander"
            else:
                changesprite = "true" 
            if isHD:
                if changesprite=="true":
                   changesprite = "Androgynous"     
                else:    
                    changesprite = "Androgynous "+ changesprite  
        elif current_gender in ["Male","Female"]: 
            gender = current_gender
            pronoun = orig_pronoun_dict[current_gender]
            if (current_gender !=  o_gender):
                new_name =  nb_names_dict[name]   
                if isHD:
                    if  name in genderswap_list:
                        changesprite = current_gender
                    else:
                       changesprite = "Androgynous"    
                else:
                    changing_char = True  

        if changing_char: #not HD, not doing a test
            if name in all_variants:
                changesprite = "Vanilla"
            else:
                changesprite = "true"
            new_name =  nb_names_dict[name]  
            
        if isGS:
            content.write("  \""+name+"Name\": \""+new_name+"\",\n")    
            content.write("  \""+name+"Gender\": \""+gender+"\",\n")    
            content.write("  \""+name+"Pronoun\": \""+pronoun+"\",\n")    
        if name != "Charlie":    
            content.write("  \""+name+"Images\": \""+changesprite+"\",\n")  
    for name in other_portraits:
        if isHD:
            content.write("  \""+name+"Images\": \"Vanilla\",\n")      
        else:
            content.write("  \""+name+"Images\": \"false\",\n")                 
   
    if isGS:
        with open("./other/advancedtitle_config.json","r") as f:
            data = f.readlines()
        for l in data:
            content.write(l)
        content.write("  \"EditIslandCharacters\": \"Full\",\n")
        content.write("  \"PatchOriginalWeddingArt\": \"false\",\n\n")   
        if not custom_possession:  
            content.write("  \"PossessiveS\": \"true\",\n\n")   
        for name in name_list:
            if name in birthday_dict.keys(): 
                content.write("  \""+name+"Birthday"+"\": \""+birthday_dict[name]+"\",\n") 
            if custom_possession:
                if name ==new_name:
                    content.write("  \""+name+"Possession\": \""+possession_dict[name]+"\",\n")  
                else:    
                    content.write("  \""+name+"Possession\": \""+possession(new_name)+"\",\n") 
            if name in spouse_list:
                content.write("  \""+name+"GameGender\": \""+ orig_gender_dict[name]+"\",\n")       
    content.write("\n}")            
    content.close()

def gender_string():
    # something like "Male, Female, Neutral"
    s="\"AllowValues\": \""
    for p in genders[0:len(genders)-1]:
        s+=p+", "
    s+=genders[len(genders)-1]
    s+="\""    
    return s

def pronoun_string():
    # something like "He, She, They"
    s="\"AllowValues\": \""
    for p in pronouns[0:len(pronouns)-1]:
        s+=p+", "
    s+=pronouns[len(pronouns)-1]
    s+="\""    
    return s

def initialise_variables(name):
    #Lines to initialise variables for content
    o_gender = orig_gender_dict[name]
    s = ""
    if isGS:
        s += "    \""+name+"Name\": {\"Default\": \""+realname(name)+"\"},\n"
        
        s+="    \""+name+"Gender\": {\"Default\": \""+o_gender+"\","+gender_string()+"},\n"

        s+="    \""+name+"Pronoun\": {\"Default\": \""+orig_pronoun_dict[o_gender]+"\","+pronoun_string()+"},\n"
    if isHD:
        s+="    \""+name+"Images\": {\"Default\": \""+orig_gender_dict[name]+"\",\"AllowValues\": \""
        s+= orig_gender_dict[name] 
        if name in variants_dict.keys():
            for variant in variants_dict[name]:
                if name =="Wizard" and variant =="Young":
                    s+=", Male Young (no sprites), Male Young (androgynous sprites)" 
                else:    
                    s+=", "+ orig_gender_dict[name] + " "+ variant    
        if name in genderswap_list:
            s+=", Female (no sprites), Female (androgynous sprites)"
        s+=", Androgynous"    
        if name in darker_chars:
            s+=", Androgynous Darker"
        if name in wheelchair_chars:
            s+=", Androgynous Wheelchair"   
        if name in islander_chars:
            s+=", Androgynous Islander"  
    else:   
        s+="    \""+name+"Images\": {\"Default\": \""+"false"+"\",\"AllowValues\": \"" 
        if name in all_variants:
            s+="Vanilla"
            if name in darker_chars:
                s+=", Darker"
            if name in wheelchair_chars:
                s+=", Wheelchair"   
            if name in islander_chars:
                s+=", Islander"  
        else:
            s+="true" 
    s+= ", false\"},\n"                         
    s+="\n"

    return s

def initialise_advanced(name): 
    s = ""  
    if isGS: 
        if name in birthday_dict.keys(): 
            s+="    \""+name+"Birthday"+"\": {\"Default\": \""+birthday_dict[name]+"\"},\n" 
        if custom_possession:
            s+="    \""+name+"Possession\":  {\"Default\": \""+possession_dict[name]+"\",\"AllowValues\": \"', 's\"},\n"     
        if name in spouse_list:
            s+="    \""+name+"GameGender\": {\"Default\": \""+orig_gender_dict[name]+"\", \"AllowValues\": \"Male, Female\"},\n"       
    if not s =="":
        s+="\n"

    return s    

def gender_variables(name):
    #Set pronoun and gender related words
    s = ""
    for word in gender_words["Neutral"].keys()+pronoun_words["They"].keys():
        s += "                {\"Name\": \""+name+word+"\", \"Value\": \"{{sqbr.getGS/"+name+word+"}}\"},\n"           
    if name !="Farmer":
        if custom_possession!=True:
            s += "                {\"Name\": \""+name+"Possession\", \"Value\": \"{{sqbr.getGS/"+name+"Possession}}\"},\n" 
    s+="\n"
    return s


##Talkoh specific

def image_start_talkoh(name, type, variant):
    #at the start of an image block 

    s= "		{\"Action\": \"EditImage\","
    if type =="sprite":
        location = "Characters/"
    else:
        if variant =="setup":
            location = "Mods/HDPortraits/" 
            s = "		{\"Action\":\"Load\","   
        else:    
            location = "Mods/talkohSeasonal/"     

    extra_code = ""
    if name in beach_bodies and (name,variant) !=("Emily","LongSleeved"):
        extra_code =", "+location
        extra_code+=name+"_Beach"
    if name in extras.keys():
        extra_code =", "+location
        extra_code+=extras[name]  
    s+= "\"Target\":\""+location+artname(name, type) + extra_code + "\","     
    return s       

def image_middle_talkoh(name, type,variant):
    return "\"FromFile\": \""+location_talkoh(variant, type)+"{{TargetWithoutPath}}.png\"," 

def image_end_talkoh(name, type, variant):
    #at the end of an image block
    if name =="other":
        return "\"When\": {\"MiscImageEdits\": \"true\"}},\n"
    else:    
        s = "\"When\": {"
        if variant =="Female":
            s+="\""+name+"FemalePortrait\": true"    
        elif variant =="Young" and name =="Wizard":
            s+="\"WizardYoungPortrait\": true"       
        elif variant !="":
            s+="\""+name+"Images\": \""+test_variable_talkoh(name, variant)+"\""  
        else:
            s+="\""+name+"Images|contains=false\": \"false\""    
        s+="}},\n"
        return s

def image_line_talkoh(name, type,variant):
    if artname(name, type)=="":
        return ""
    else:
        return image_start_talkoh(name, type,variant) +image_middle_talkoh(name, type,variant)+image_end_talkoh(name, type, variant)    

## Androgynous

def image_start(name, type, variant):
    #at the start of an image block 

    s= "		{\"Action\": \"EditImage\","
    if type =="sprite":
        location = "Characters/"
    elif isHD:
        location = "Mods/talkohSeasonal/"     
    else:
        location = "Portraits/"       
        
    extra_code = ""
    if name in beach_bodies:
        extra_code =", "+location
        extra_code+=name+"_Beach"
    if name in extras.keys():
        extra_code =", "+location
        extra_code+=extras[name]  
    s+= "\"Target\":\""+location+artname(name, type) + extra_code + "\","     
    return s

def image_middle_basic(name, type,variant):
    return "\"FromFile\": \""+location(variant, type)+"{{TargetWithoutPath}}.png\"," 

def image_middle_location(name, location):       
    return "\"FromFile\": \"Androgynous/"+location+"/"+name+".png\"," 

def image_end(name, type, variant):
    #at the end of an image block 
    if name =="other":
        return "\"When\": {\"MiscImageEdits\": \"true\"}},\n"
    else:    
        s = "\"When\": {"
        if isHD and type =="sprite" and variant =="" and name in genderswap_list:
            s+="\""+name+"AndrogynousSprite\": true"
        elif variant !="" or isHD:
            s+="\""+name+"Images\": \""+test_variable(name, variant)+"\""  
        else:
            s+="\""+name+"Images|contains=false\": \"false\""    
        s+="}},\n"
        return s

def image_line(name, type,variant):
    #code to replace image at location
    if artname(name, type)=="":
        return ""
    else:
        return image_start(name, type,variant) +image_middle_basic(name, type,variant)+image_end(name, type, variant)

def image_line_other(name):
    return image_start(name, "sprite", "") +image_middle_basic(name,  "sprite", "")+image_end("other","sprite", "")

def image_line_pos(name, type,variant,x, y, w, h):
    #code to replace image at location in a given box
    s =image_start(name, type,variant)
    pos_string ="{ \"X\": "+str(x)+", \"Y\": "+str(y)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }" 
    s+="\"FromArea\": "+pos_string+",\"ToArea\":  "+pos_string+","
    s+=image_middle_basic(name, type,variant)+image_end(name, type, variant)
    return s

def image_line_pos_loc(name, location, type, variant,x, y, w, h):
    #code to replace image at location in a given box
    s ="		{\"Action\": \"EditImage\",\"Target\":\""+location + "\","  
    pos_string ="{ \"X\": "+str(x)+", \"Y\": "+str(y)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }" 
    s+="\"FromArea\": "+pos_string+",\"ToArea\":  "+pos_string+","
    s+= "\"FromFile\": \"Androgynous/"+location+".png\"," 
    s+=image_end(name, type, variant)
    return s    

def image_pair(name, location1, location2,variant):
    #code to replace image at location in a given box
    s ="		{\"Action\": \"EditImage\",\"Target\": \"" + location1+"\","
    s+=image_middle_location(name, location2)+image_end(name, "sprite", variant)
    return s    

def image_pair_pos(name, location1, location2, variant,x1, y1, x2,y2,w, h):
    #code to replace image at location in a given box
    if variant =="":
        location = location2
    else:
        location = location2+"_"+variant    
    s ="		{\"Action\": \"EditImage\",\"Target\": \"" + location1+"\","
    s+= "\"FromFile\": \"Androgynous/"+location+".png\"," 
    s+="\"FromArea\": { \"X\": "+str(x2)+", \"Y\": "+str(y2)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }," 
    s+="\"ToArea\": { \"X\": "+str(x1)+", \"Y\": "+str(y1)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }," 
    s+=image_end(name, "sprite", variant)
    return s    

def image_lineSpouse(name,variant):
    #name of spouse, any extra properties like "Wheelchair"
    o_gender = orig_gender_dict[name]

    start = "		{\"Action\": \"EditImage\",""\"Target\":\"Characters/"+spritename(name) + "\","  
    if variant !="":
            end_variable="\""+name+"Images\": \""+test_variable(name, variant)+"\""  
    else:
            end_variable="\""+name+"Images|contains=false\": \"false\""    
    test_string = "\"When\": {\""+name+"GameGender\": \""+genderswap(o_gender)+"\", \"DayEvent|contains=flower dance\": \"false\","+end_variable+"}},\n"  
    s = start + image_middle_basic(name, "sprite",variant)   
    s+="\"FromArea\": { \"X\": 0, \"Y\": 288, \"Width\": 48, \"Height\": 32 }," 
    s+="\"ToArea\": { \"X\": 0, \"Y\": 384, \"Width\": 48, \"Height\": 32 }," 
    s+= test_string 
    if not name in ["Maru","Haley"]: #have shorter sprite sheets
        s+=start + image_middle_basic(name, "sprite",variant)
        s+="\"FromArea\": { \"X\": 0, \"Y\": 384, \"Width\": 48, \"Height\": 32 }," 
        s+="\"ToArea\": { \"X\": 0, \"Y\": 288, \"Width\": 48, \"Height\": 32 }," 
        s+=test_string     
    return s

def extra_sprites(name):  
    #all image replacements for character called name
    s = ""
    if name =="Abigail":
        s+=image_line_pos_loc(name, "Characters/ClothesTherapyCharacters","sprite", "", 0, 32, 64, 32)   
        s+=image_line_pos_loc(name, "Characters/ClothesTherapyCharacters","sprite","", 0, 160, 16, 32) 
    elif name =="Caroline":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 9, 108,9,108,9, 9)    
    elif name =="Clint":
        s+=image_line_pos_loc(name,"Characters/ClothesTherapyCharacters","sprite","", 0, 64, 64, 32)  
        s+=image_line_pos_loc(name,"Characters/ClothesTherapyCharacters","sprite","", 32, 160, 32, 32) 
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 54, 117,54,117,9, 9)       
    elif name =="Elliott":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 99, 99,99,99,9, 9)  
    elif name =="Emily":
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 448, 212,96,0,32, 32)      
    elif name =="Gil":
        s+=image_pair_pos(name, "Maps/townInterior", "Gil/townInterior","",176, 624,0,0, 32, 64) 
        s+=image_pair_pos(name, "Maps/townInterior", "Gil/townInterior","",207, 656, 32,32,32, 32)  
        s+=image_pair_pos(name, "Maps/MovieTheater_TileSheet", "Other/MovieTheater_TileSheet","",224, 208,224, 208, 32, 48) 
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet", "Other/MovieTheater_TileSheet","",224, 208,224, 208, 32, 48) 
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet_international", "Other/MovieTheater_TileSheet","",224, 208,224, 208, 32, 48) 
    elif name =="Governor":
        s+=image_pair_pos(name, "Maps/MovieTheater_TileSheet", "Other/MovieTheater_TileSheet","",208,224,208,224, 16,32)      
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet", "Other/MovieTheater_TileSheet","",208,224,208,224, 16,32)     
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet_international", "Other/MovieTheater_TileSheet","",208,224,208,224, 16,32)        
    elif name =="Grandpa":
        s+=image_pair_pos(name, "LooseSprites/Cursors2", "Grandpa/Cursors2","", 186, 265, 0,0,22, 34)  
        s+=image_pair_pos(name, "LooseSprites/Cursors2", "Grandpa/Cursors2","Darker", 186, 265, 0,0,22, 34) 
        s+=image_pair_pos(name, "LooseSprites/Cursors", "Grandpa/Cursors","",555, 1957, 0,0,17, 33)  
        s+=image_pair_pos(name, "LooseSprites/Cursors", "Grandpa/Cursors","Darker",555, 1957, 0,0,17, 33)  
        s+=image_pair_pos(name, "Minigames/jojacorps", "Grandpa/jojacorps","",427, 0, 0,0,427, 477)  #main picture
        s+=image_pair_pos(name, "Minigames/jojacorps", "Grandpa/jojacorps","Darker",427, 0, 0,0,427, 477)
        s+=image_pair_pos(name, "Minigames/jojacorps", "Grandpa/jojacorps","",497, 523, 70,523, 36, 18) #talking
        s+=image_pair_pos(name, "Minigames/jojacorps", "Grandpa/jojacorps","Darker",497, 523, 70,523, 36, 18)
        s+=image_pair_pos(name, "Minigames/jojacorps", "Grandpa/jojacorps","Darker",463, 556, 36,556, 74, 17) #hands
    elif name =="Gunther":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 27, 117,27,117,9, 9) 
        s+=image_pair_pos(name, "Maps/MovieTheater_TileSheet", "Other/MovieTheater_TileSheet","",208,192,208,192, 16,32) 
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet", "Other/MovieTheater_TileSheet","",208,192,208,192, 16,32)  
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet_international", "Other/MovieTheater_TileSheet","",208,192,208,192, 16,32)          
    elif name =="Gus":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 18, 117,18,117,9, 9) 
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 352, 212,0,0,32, 32)  
    elif name =="Haley":
        s+=image_pair(name, "LooseSprites/CowPhotos","Haley/CowPhotos","")
        s+=image_pair(name, "LooseSprites/CowPhotosWinter","Haley/CowPhotoWinter","")
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 36, 99,36,99,9, 9)  
    elif name =="Harvey":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 90, 99,90,99,9, 9)      
    elif name =="Jas":
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","",164, 97, 34,32,13, 20)   
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","Darker",164, 97, 34,32,13, 20) 
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 108, 108,108,108,9, 9)
    elif name =="Jodi":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 45, 108,45,108,9, 9)  
    elif name =="Krobus":     
        s+=image_line_pos_loc(name,"Characters/KrobusRaven","sprite","",0,0,160,32)      
    elif name =="Lewis":
        s+=image_line_pos_loc(name,"Characters/ClothesTherapyCharacters","sprite","", 0, 32, 64, 32)  
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 54, 108,54,108,9, 9)  
    elif name =="Linus":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 63, 108,63,108,9, 9)                        
    elif name =="Marnie":
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","", 146, 89, 16,24,18, 28) 
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","Darker", 146, 89, 16,24,18, 28)   
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Cursors_Marnie","", 557, 1424,0,0,62, 28)    
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Cursors_Marnie","Darker", 557, 1424,0,0,62, 28) 
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Marnie_Paintings","", 0, 1925,0,0,50, 47)   
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Marnie_Paintings","Darker", 0, 1925,0,0,50, 47)   
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 0, 108,0,108,9, 9)  
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 0, 108,0,108,9, 9)    
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 480, 212,128,0,32, 32) 
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","Darker", 480, 212,128,0,32, 32)        
    elif name =="Marcello": 
        s+=image_pair_pos(name, "Maps/MovieTheater_TileSheet", "Other/MovieTheater_TileSheet","",16,192,16,192, 16,32)  
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet", "Other/MovieTheater_TileSheet","",16,192,16,192, 16,32)  
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet_international", "Other/MovieTheater_TileSheet","",16,192,16,192, 16,32)         
    elif name =="Marlon":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 72, 108,72,108,9, 9)   
        s+=image_pair_pos(name, "Maps/MovieTheater_TileSheet", "Other/MovieTheater_TileSheet","",0,192,0,192, 16,32)  
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet", "Other/MovieTheater_TileSheet","",0,192,0,192, 16,32)  
        s+=image_pair_pos(name, "Maps/MovieTheaterJoja_TileSheet_international", "Other/MovieTheater_TileSheet","",0,192,0,192, 16,32)     
    elif name =="Pam":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 36, 108,36,108,9, 9)     
    elif name =="Robin":
        s+=image_line_pos_loc(name,"Characters/ClothesTherapyCharacters","sprite","", 0, 96, 64, 32) 
        s+=image_line_pos_loc(name,"Characters/ClothesTherapyCharacters","sprite","", 16, 160, 16, 32)         
    elif name =="Shane":
        s+=image_line_pos_loc(name, "Characters/ClothesTherapyCharacters","sprite","", 0, 0, 64, 32)  
        s+=image_line_pos_loc(name, "Characters/ClothesTherapyCharacters","sprite","", 0, 0, 64, 32)  
    elif name =="Willy":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 81, 108,81,108,9, 9)
    elif name =="Wizard":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 90, 108,90,108,9, 9)  
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 416, 212,64,0,32, 32)  
        s+=image_line_pos_loc(name,"Characters/KrobusRaven","sprite","",0,64,160,104)                    
    return s      

def image_code_background(): 
    s=image_pair_pos("other", "LooseSprites/Cursors2", "Other/Cursors2_fairy","",208, 256,0,0, 48, 64)  #fairy
    s+=image_pair_pos("other", "LooseSprites/Cursors", "Other/Cursors_witch","",276, 1885,0,0, 44, 61) #witch
    s+=image_pair_pos("other", "Minigames/jojacorps", "Other/jojacorps","",0, 420,0,420, 264, 179) #farmer face
    s+=image_pair_pos("other", "Minigames/jojacorps", "Other/jojacorps","",0, 600,0,600, 1200, 200) #computers
    #s+=image_pair_pos("other", "Minigames/jojacorps", "Other/jojacorps","",642, 246,0,0, 61, 28) #paintings
    #s+=image_pair_pos("other", "Minigames/jojacorps", "Other/jojacorps","",642, 7,0,0, 61, 28) #paintings 
    s+=image_line_other("Toddler") #toddlers
    s+=image_line_other("Toddler_girl")
    s+=image_line_other("Toddler_girl_dark")
    s+=image_line_other("Toddler_dark")
    s+=image_pair("other","Characters/LeahExFemale","Characters/LeahEx","")
    s+=image_pair("other","Characters/LeahExMale","Characters/LeahEx","")
    return s


def disposition(name,gender):
    gender=gender.lower()
    if name =="Abigail":
        return "teen/rude/outgoing/neutral/"+gender+"/datable/Sebastian/Town/{{AbigailBirthday}}/Caroline '{{CarolineParent}}' Pierre '{{PierreParent}}'/SeedShop 1 9/{{AbigailName}}"
    elif name =="Elliott":
        return "adult/polite/neutral/neutral/"+gender+"/datable/Leah/Town/{{ElliottBirthday}}/Willy ''/ElliottHouse 1 5/{{ElliottName}}"
    elif name =="Emily":
        return "adult/polite/outgoing/positive/"+gender+"/datable/null/Town/{{EmilyBirthday}}/Haley '{{HaleySibling}}'/HaleyHouse 16 5/{{EmilyName}}"   
    elif name =="Haley":
        return "adult/rude/outgoing/neutral/"+gender+"/datable/Alex/Town/{{HaleyBirthday}}/Emily '{{EmilySibling}}'/HaleyHouse 8 7/{{HaleyName}}"
    elif name =="Harvey":
        return "adult/polite/shy/positive/"+gender+"/datable/Maru/Town/{{HarveyBirthday}}//HarveyRoom 13 4/{{HarveyName}}"      
    elif name =="Alex":
        return "adult/rude/outgoing/positive/"+gender+"/datable/Haley/Town/{{AlexBirthday}}/George 'grandie {{GeorgeName}}' Evelyn 'grandie {{EvelynName}}'/JoshHouse 19 5/{{AlexName}}"
    elif name =="Leah":
        return "adult/polite/neutral/positive/"+gender+"/datable/Elliott/Town/{{LeahBirthday}}//LeahHouse 3 7/{{LeahName}}"    
    elif name =="Maru":
        return "teen/neutral/outgoing/positive/"+gender+"/datable/Harvey/Town/{{MaruBirthday}}/Robin '{{RobinParent}}' Demetrius '{{DemetriusParent}}' Sebastian 'half-{{SebastianSibling}}'/ScienceHouse 2 4/{{MaruName}}"
    elif name =="Penny":
        return "teen/polite/shy/positive/"+gender+"/datable/Sam/Town/{{PennyBirthday}}/Pam '{{PamParent}}'/Trailer 4 9/{{PennyName}}"      
    elif name =="Sam":
        return "teen/neutral/outgoing/positive/"+gender+"/datable/Penny/Town/{{SamBirthday}}/Vincent 'little {{VincentSibling}}' Jodi '{{JodiParent}}' Kent '{{KentParent}}' Sebastian ''/SamHouse 22 13/{{SamName}}"
    elif name =="Sebastian":
        return "teen/rude/shy/negative/"+gender+"/datable/Abigail/Town/{{SebastianBirthday}}/Robin '{{RobinParent}}' Maru 'half-{{MaruSibling}}' Sam ''/SebastianRoom 10 9/{{SebastianName}}"    
    elif name =="Shane":
        return "adult/rude/shy/negative/"+gender+"/datable/null/Town/{{ShaneBirthday}}/Marnie '{{MarnieAuncleU}}'/AnimalShop 25 6/{{ShaneName}}"        
    elif name =="Caroline": 
        return "adult/polite/neutral/neutral/female/not-datable/Pierre/Town/{{CarolineBirthday}}/Pierre '{{PierreSpouse}}' Abigail ''/SeedShop 22 5/{{CarolineName}}"
    elif name == "Clint": 
        return "adult/rude/shy/negative/male/not-datable/Emily/Town/{{ClintBirthday}}/Emily ''/Blacksmith 3 13/{{ClintName}}"
    elif name ==  "Demetrius": 
        return "adult/polite/neutral/positive/male/not-datable/Robin/Town/{{DemetriusBirthday}}/Robin '{{RobinSpouse}}' Maru ''/ScienceHouse 19 4/{{DemetriusName}}"
    elif name ==  "Willy": 
        return "adult/neutral/neutral/neutral/male/not-datable/null/Town/{{WillyBirthday}}/Elliott ''/FishShop 5 4/{{WillyName}}"
    elif name == "Evelyn": 
        return "adult/polite/outgoing/positive/female/not-datable/George/Town/{{EvelynBirthday}}/George '{{GeorgeSpouse}}' Alex 'grand{{AlexChild}}'/JoshHouse 2 17/{{EvelynName}}"
    elif name =="George": 
       return "adult/rude/neutral/negative/male/not-datable/Evelyn/Town/{{GeorgeBirthday}}/Evelyn '{{EvelynSpouse}}' Alex 'grand{{AlexChild}}'/JoshHouse 16 22/{{GeorgeName}}"
    elif name =="Gus": 
       return "adult/neutral/outgoing/positive/male/not-datable/null/Town/{{GusBirthday}}/Emily '' Pam ''/Saloon 18 6/{{GusName}}"
    elif name =="Jas": 
       return "child/neutral/shy/positive/female/not-datable/Vincent/Town/{{JasBirthday}}/Vincent ''/AnimalShop 4 6/{{JasName}}"
    elif name =="Jodi": 
       return "adult/polite/neutral/neutral/female/not-datable/Kent/Town/{{JodiBirthday}}/Sam '{{SamChild}}' Vincent '{{VincentChild}}' Kent 'husband'/SamHouse 4 5/{{JodiName}}"
    elif name =="Kent": 
       return "adult/neutral/shy/negative/male/not-datable/Jodi/Town/{{KentBirthday}}/Jodi 'wife' Sam '{{SamChild}}' Vincent '{{VincentChild}}'/SamHouse 22 5/{{KentName}}"
    elif name =="Leo": 
       return  "child/neutral/shy/neutral/male/not-datable/Leo/Other/{{LeoBirthday}}//IslandHut 5 6/{{LeoName}}"
    elif name =="Lewis": 
       return "adult/neutral/outgoing/positive/male/not-datable/null/Town/{{LewisBirthday}}/Marnie ''/ManorHouse 8 5/{{LewisName}}"
    elif name =="Linus": 
       return "adult/neutral/shy/positive/male/not-datable/null/Town/{{LinusBirthday}}//Tent 1 2/{{LinusName}}"
    elif name =="Marnie": 
       return "adult/polite/outgoing/positive/female/not-datable/Lewis/Town/{{MarnieBirthday}}/Lewis '' Shane '{{ShaneNibling}}' Jas '{{JasNibling}}'/AnimalShop 12 14/{{MarnieName}}"
    elif name == "Pam": 
       return "adult/rude/outgoing/negative/female/not-datable/Gus/Town/{{PamBirthday}}/Penny '{{PennyChild}}' Gus ''/Trailer 15 4/{{PamName}}"
    elif name == "Pierre": 
       return "adult/neutral/outgoing/positive/male/not-datable/Caroline/Town/{{PierreBirthday}}/Abigail '{{AbigailChild}}' Caroline '{{CarolineSpouse}}'/SeedShop 4 17/{{PierreName}}"
    elif name =="Robin": 
       return "adult/neutral/outgoing/positive/female/not-datable/Demetrius/Town/{{RobinBirthday}}/Demetrius '{{DemetriusSpouse}}' Maru '{{MaruChild}}' Sebastian '{{SebastianChild}}'/ScienceHouse 21 4/{{RobinName}}"
    elif name == "Vincent": 
       return "child/neutral/outgoing/positive/male/not-datable/Jas/Town/{{VincentBirthday}}/Jas ''/SamHouse 10 23/{{VincentName}}"
    elif name =="Sandy": 
       return "adult/neutral/outgoing/positive/female/not-datable/null/Desert/{{SandyBirthday}}/Emily ''/SandyHouse 2 5/{{SandyName}}"
    elif name =="Krobus": 
       return "adult/polite/shy/neutral/male/not-datable/null/Other/{{KrobusBirthday}}//Sewer 31 17/{{KrobusName}}"
    elif name == "Marlon": 
        return "adult/neutral/outgoing/neutral/male/not-datable/Marnie/Town///AdventureGuild 5 11/{{MarlonName}}",
    elif name == "Dwarf": 
       return "adult/neutral/outgoing/positive/undefined/not-datable/null/Other/{{DwarfBirthday}}//Mine 43 6/{{DwarfName}}"
    elif name =="Wizard": 
       return "adult/rude/neutral/negative/male/not-datable/null/Other/{{WizardBirthday}}//WizardHouse 3 17/{{WizardName}}"

def dance_wedding():
    s = "\n"
    for name in spouse_list:
        o_gender =  orig_gender_dict[name]
        if o_gender =="Male":
            Y = "288"
        else:
            Y = "384"
        s += "		{\"Action\": \"EditImage\",\"Target\": \"Characters/"+name+"\","
        s += "\"FromFile\": \"assets/Wedding/"+name+"_Wedding.png\",\"ToArea\": { \"X\": 0, \"Y\": "+Y+", \"Width\": 48, \"Height\": 32 },"
        s += "\"When\": { \""+name+"GameGender\": \""+genderswap(o_gender)+"\", \"DayEvent\": \"wedding\",\""+name+"Images\":\"false\", \"PatchOriginalWeddingArt\":\"true\"}},"
        s+="\n"
        s+= "		{\"Action\": \"EditData\",\"Target\": \"Data/NPCDispositions\",\"Update\": \"OnLocationChange\","
        s+="\"When\": { \""+name+"GameGender\": \""+genderswap(o_gender)+"\",\"DayEvent|contains=flower dance\": \"false\"},"
        s+="\"Entries\": {\""+name+"\":\""+disposition(name,genderswap(o_gender))+"\"}},"
        s+="\n\n"
    s+="		{\"Action\": \"EditData\",\"Target\": \"Strings/Locations\",\n"
    s+="             \"Entries\": {\n"
    s+="        			\"DoorUnlock_NotFriend_Male\": \"You're not good enough friends with {0} to enter their bedroom.\",\n"
    s+="        			\"DoorUnlock_NotFriend_Female\": \"You're not good enough friends with {0} to enter their bedroom.\",\n"
    s+="			}},\n\n"    
    return s

def wedding_code():
    wedding_line = "\"@... %spouse... #$b# As the mayor of Pelican Town, and regional bearer of the matrimonial seal, I now pronounce you... married!$h\",\n"
    s ="\n		{\n"
    s+="      		\"Action\": \"EditData\",\n"
    s+="      		\"Target\": \"strings/StringsFromCSFiles\",\n"
    s+="      		\"Entries\": {\n"
    s+="			\"Utility.cs.5371\": "+wedding_line
    s+="			\"Utility.cs.5373\": "+wedding_line
    s+="			\"Utility.cs.5375\": "+wedding_line
    s+="			\"Utility.cs.5377\": "+wedding_line
    s+="			}},\n"
    return s

def create_content():
    # Config
    path = end_path()+"content.json"  
    content = open(path,"w")
    content.write("{\n    \"Format\": \"1.27.0\",\n    \"ConfigSchema\":\n {\n")
    if isGS:
            content.write("    \"MiscTextEdits\": { \"AllowValues\": \"true, false\",\"Default\": \"false\"},\n")
    content.write("    \"MiscImageEdits\": { \"AllowValues\": \"true, false\",\"Default\": \"false\"},\n\n")
    if isGS:
        content.write("    \"FarmerGender\":{ \"AllowValues\": \"false,Male, Female, Neutral\",\"Default\": \"false\"},\n")
        content.write("    \"FarmerPronoun\": {\"Default\": \"They\","+pronoun_string()+"},\n\n")
    if isHD:
        content.write("    \"Genderbent Bachelors\": {\n")
        content.write("    	\"AllowValues\": \"Classic, RedK1rby\",\n")
        content.write("    	\"Default\": \"Classic\",\n")
        content.write("    	\"Description\": \"Choose between RedK1rby-style beach portraits or the classic ones for Bachelors switched to Female.\"\n")
        content.write("    },\n\n")
        
    for name in name_list:
        content.write(initialise_variables(name))  
    for name in other_portraits:
        if isHD:
            content.write("    \""+name+"Images\": {\"Default\": \""+"Vanilla"+"\",\"AllowValues\": \"false, Vanilla, Androgynous\"},\n\n")  
        else:
            content.write("    \""+name+"Images\": {\"Default\": \""+"false"+"\",\"AllowValues\": \"false, true\"},\n\n")  
    if isGS:
        with open("./other/advancedtitle_content.json","r") as f:
            data = f.readlines()
        for l in data:
            content.write(l)
        content.write("    \"EditIslandCharacters\": { \"AllowValues\": \"Full, Minimal, None\",\"Default\": \"Full\"},\n")    
        content.write("    \"PatchOriginalWeddingArt\": { \"AllowValues\": \"true, false\",\"Default\": \"false\"},\n\n") 
        content.write("    \"PossessiveS\": { \"AllowValues\": \"true, false\",\"Default\": \"true\"},\n\n")  
        for name in name_list:
            content.write(initialise_advanced(name))      
    content.write("    },\n")  

    #Dynamic Tokens      
    content.write("    \"DynamicTokens\": [\n")   
    for name in genderswap_list:
        content.write("                {\"Name\": \""+name+"FemalePortrait\", \"Value\":\"false\"},\n")   
        content.write("                {\"Name\": \""+name+"FemalePortrait\", \"Value\":\"true\",\"When\":{\""+name+"Images\": \"Female (no sprites)\"}},\n") 
        content.write("                {\"Name\": \""+name+"FemalePortrait\", \"Value\":\"true\",\"When\":{\""+name+"Images\": \"Female (androgynous sprites)\"}},\n") 
        content.write("                {\"Name\": \""+name+"AndrogynousSprite\", \"Value\":\"false\"},\n")   
        content.write("                {\"Name\": \""+name+"AndrogynousSprite\", \"Value\":\"true\",\"When\":{\""+name+"Images\": \"Androgynous\"}},\n") 
        content.write("                {\"Name\": \""+name+"AndrogynousSprite\", \"Value\":\"true\",\"When\":{\""+name+"Images\": \"Female (androgynous sprites)\"}},\n")     
    content.write("                {\"Name\": \"WizardYoungPortrait\", \"Value\":\"false\"},\n")   
    content.write("                {\"Name\": \"WizardYoungPortrait\", \"Value\":\"true\",\"When\":{\"WizardImages\": \"Male Young (no sprites)\"}},\n") 
    content.write("                {\"Name\": \"WizardYoungPortrait\", \"Value\":\"true\",\"When\":{\"WizardImages\": \"Male Young (androgynous sprites)\"}},\n")          
    content.write("                {\"Name\": \"WizardAndrogynousSprite\", \"Value\":\"true\",\"When\":{\"WizardImages\": \"Male Young (androgynous sprites)\"}},\n")                   
    if isGS:
        content.write("                {\"Name\": \"ChangeFarmerGender\", \"Value\":\"true\"},\n")
        content.write("                {\"Name\": \"ChangeFarmerGender\", \"Value\":\"false\",\"When\":{\"FarmerGender\": \"false\"}},\n")   
        content.write("                {\"Name\": \"ChangeFarmerGender\", \"Value\":\"false\",\"When\":{\"HasMod |contains=Hana.GenderNeutralityMod\": true}},\n")    
        content.write(gender_variables("Farmer"))  
        for name in name_list:
            content.write(gender_variables(name))  
    content.write("    ],\n")  

    #Changes
    content.write("	\"Changes\": [\n")  
    if isHD:
        content.write(hd_setup())
    content.write(create_image_code())
    if isHD:
        content.write(hd_extra_portraits())
    
    content.write(image_code_background())     
    if isGS:
        content.write("\n		{\n")
        content.write("			\"Action\": \"EditData\",\n")
        content.write("			\"Target\": \"Data/NPCDispositions\",\n")
        content.write("			\"Entries\": {\n")
        for name in name_list:
            if name in birthday_dict.keys() and name !="Leo": #has a birthday and disposition
                content.write("				\""+name+"\":\""+disposition(name,orig_gender_dict[name])+"\",\n")
        content.write("			}},\n")
        content.write("		{\"Action\": \"EditData\",\"Target\": \"Data/NPCDispositions\",\"Entries\": {\n")
        content.write("				\"Leo\":\""+disposition("Leo","male")+"\"\n")
        content.write("			},\"When\": {\"EditIslandCharacters\": \"Full\"}},\n")
        with open("./mine/change_names.json","r") as f:
            content.write(f.read())	
        content.write(dance_wedding())	
        with open("./mine/farmer.json","r") as f:
            content.write(f.read())	         
        with open("./mine/dialogue_objects.json","r") as f:
            content.write(f.read())	  
        with open("./mine/my_dialogue_fixes.json","r") as f:
            content.write(f.read())	  
        #with open("./mine/MoviesReactions.json","r") as f:
        #    content.write(f.read())	     
        with open("./mine/diverse_island.json","r") as f:
            content.write(f.read())	          
        with open("./mine/dammitclint.json","r") as f:
            content.write(f.read())	          
        with open("./mine/journalist.json","r") as f:
            content.write(f.read())	    
        with open("./mine/mymods.json","r") as f:
            content.write(f.read())	                       
        content.write(wedding_code())            
    content.write("	]\n}") 
    content.close()   

###### image code
# 

def test_variable(name, variant):
    # for When "(name) Image" : "test_variable(name, variant)"
    # type = portrait, sprite
    # variant = Darker etc

    if isHD:
        if variant =="":
            return "Androgynous"
        else:
            return "Androgynous "+ variant  
    else:
            return variant     

def test_variable_talkoh(name, variant):
    # for When "(name) Image" : "test_variable(name, variant)"
    # type = portrait, sprite
    # variant = Darker etc
    if variant in ["Young","Coat","LongSleeved", "Shaved"]:
        return orig_gender_dict[name]+ " "+ variant    
    else:
        return variant                              


def location(variant, type):
    #location of the image we're using 

    if variant =="":
        if type == "sprite":
            return "Androgynous/Characters/"
        else:
            return "Androgynous/Portraits/"
    else:
        if type == "sprite":
            return "Androgynous/Characters/Variants/"+ variant + "/"
        else:
            return "Androgynous/Portraits/Variants/"+ variant + "/"     

def location_talkoh(variant, type):
    #location of the image we're using 

    if variant =="":
        if type == "sprite":
            return "assets/Characters/"
        else:
            return "assets/Portraits/"
    elif variant in ["Young","Coat","LongSleeved", "Shaved"]:
        if type == "sprite":
            return "assets/Characters/Variants/"+ variant + "/"
        else:
            return "assets/Portraits/Variants/"+ variant + "/"
    elif variant.count("Female")>0:
        if type == "sprite":
            return "Androgynous/Characters" 
        else:
            return "assets/Portraits/Genderbent/"
    else:
        print("Error, unknown variant: "+variant)        

def hd_extra_portraits():
    s = ""
    for name in variants_dict.keys():
        for variant in variants_dict[name]:
            s+= image_line_talkoh(name, "portrait", variant)   
    s+= image_line_talkoh("Linus", "sprite", "Coat")
    s+= image_line_talkoh("Pam", "sprite", "Young")   
    # s+="        {\n			\"Action\":\"EditImage\",\n"
    # s+="			\"Target\":\"Characters/Wizard\",\n"     
    # s+="			\"FromFile\":\"Androgynous/Characters/{{TargetWithoutPath}}.png\",\n"
    # s+=" 			\"When\": {\"WizardImages\": \"Male Young (androgynous sprites)\"}\n        },\n\n" 
    # s+="\n"         
    for name in genderswap_list:
        s+= image_line_talkoh(name, "portrait", "Female") 
        # s+="        {\n			\"Action\":\"EditImage\",\n"
        # s+="			\"Target\":\"Characters/"+spritename(name) 
        # if name in beach_bodies:
        #     s+= ", Characters/"+spritename(name)+"_Beach"
        # s+="\",\n"     
        # s+="			\"FromFile\":\"Androgynous/Characters/{{TargetWithoutPath}}.png\",\n"
        # s+=" 			\"When\": {\""+name+"Images\": \"Female (androgynous sprites)\"}\n        },\n\n" 
        # s+="\n"   
        if name in beach_bodies:
            s+="        {\n			\"Action\":\"EditImage\",\n"
            s+="			\"Target\":\"Mods/talkohSeasonal/"+portraitname(name) + "_Beach\",\n"
            s+="			\"FromFile\":\"assets/Portraits/Genderbent/Classic/"+ name+"_Beach.png\",\n"
            s+=" 			\"When\": {\""+name+"FemalePortrait\": true,  \"Genderbent Bachelors\": \"Classic\"}\n        },\n\n"
            
             
    return s 
 
def hd_setup():
    s = ""
    name_string = "\""
    for name in portrait_list + other_portraits:
        name_string+= "Mods/talkohSeasonal/"+portraitname(name) + ", "
        if name in extras.keys():
            name_string+= "Mods/talkohSeasonal/"+extras[name] + ", "
    for name in beach_bodies:
        name_string+= "Mods/talkohSeasonal/"+portraitname(name) + "_Beach, "
    name_string += "\",\n"   
    s+="        {\n			\"Action\":\"Load\",\n"
    s+="			\"Target\":"+ name_string
    s+="			\"FromFile\":\"assets/Portraits/{{TargetWithoutPath}}.png\",\n"
    s+="			\"When\" :{\"HasMod |contains=talkohlooeys.SeasonalPortraits\": false}\n"
    s+="        },\n\n" 
    
    for name in portrait_list:
        s += image_start_talkoh(name, "portrait", "setup")
        s+="\"FromFile\":\"assets/base.json\","
        s+= "\"When\": {\""+name+"Images|contains=false\": \"false\",\"HasMod |contains=talkohlooeys.SeasonalPortraits\": false}},\n"  
    
    name_string = "\"" 
    for name in portrait_list + other_portraits:
        name_string+= "Mods/HDPortraits/"+portraitname(name) + ", "
        if name in extras.keys():
            name_string+= "Mods/HDPortraits/"+extras[name] + ", "
    for name in beach_bodies:
        name_string+= "Mods/HDPortraits/"+portraitname(name) + "_Beach, "    
    name_string += "\",\n"   
    s+="        {\n			\"Action\":\"EditData\",\n"
    s+="			\"Target\":"+ name_string
    s+="			\"Entries\": {\n"
    s+="	    		\"Portrait\":\"Mods/talkohSeasonal/{{TargetWithoutPath}}\"\n"
    s+="			},\n"
    s+="			\"When\" :{\"HasMod |contains=talkohlooeys.SeasonalPortraits\": false}\n"
    s+="        },\n\n"
    return s

def create_image_code(): 
    s = ""
    for name in other_portraits:
        s+= image_line(name, "portrait", "")   
        s+="\n"    
    for name in portrait_list:
        s+= image_line(name, "portrait", "")  
        if name =="Kent":
                s+=image_line_pos(name,"sprite","", 0, 0, 64, 160) #for compatibility with Kent does the dishes  
        else:    
                s+= image_line(name, "sprite", "")   
        if name in darker_chars:
            s+= image_line(name, "portrait", "Darker")  
            s+= image_line(name, "sprite", "Darker")      
        if name in wheelchair_chars: 
            s+= image_line(name, "sprite", "Wheelchair")  
        if name in islander_chars:
            s+= image_line(name, "portrait", "Islander")  
            s+= image_line(name, "sprite", "Islander")   
        s+="\n"             
    for name in no_portrait_list:   
        s+= image_line(name, "sprite", "")    
        s+="\n" 
    if isGS:
            for name in spouse_list:
                s+= image_lineSpouse(name,"")
                if name in darker_chars:
                    s+=image_lineSpouse(name,"Darker")
                elif name in wheelchair_chars:    
                    s+=image_lineSpouse(name,"Wheelchair")      
                s+="\n"         
    for name in portrait_list + no_portrait_list:
        e=extra_sprites(name) 
        if e!="":
            s+=e 
            s+="\n"                
    return s

isGS = True
for isHD in [True, False]:
    for g in ["Male", "Female", "Neutral", "Test"]:
        create_config(g) 
for isGS in [True, False]:
    for isHD in [True, False]:
        create_config("None")

for isGS in [True, False]:
    for isHD in [True, False]:
        create_content()

#create_content(False, False)

#create_hd(False)

   
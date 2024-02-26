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
name_list2= ["Robin","Sam","Sandy","Sebastian","Shane","Vincent","Willy","Witch","Wizard",]

name_list = name_list1 + ["ProfessorSnail"]+name_list2 #for pronouns etc

sprite_list = sorted(name_list + ["Bear"])
sprite_list.remove("Gil")
sprite_list.remove("Witch")

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
orig_gender_dict = {"ProfessorSnail": "Male","Abigail":"Female","Alex":"Male","Birdie":"Female","Bouncer":"Male","Caroline":"Female","Charlie":"Female","Clint":"Male","Demetrius":"Male","Dwarf":"Male","Elliott":"Male","Emily":"Female","Evelyn":"Female","George":"Male","Gil":"Male","Governor":"Male","Grandpa":"Male","Gunther":"Male","Gus":"Male","Haley":"Female","Harvey":"Male","Henchman":"Male","Jas":"Female","Jodi":"Female","Kent":"Male","Krobus":"Male","Leah":"Female","Leo":"Male","Lewis":"Male","Linus":"Male","Marcello":"Male","Marlon":"Male","Marnie":"Female","Maru":"Female","MisterQi":"Male","Morris":"Male","OldMariner":"Male","Pam":"Female","Penny":"Female","Pierre":"Male","Robin":"Female","Sam":"Male","Sandy":"Female","Sebastian":"Male","Shane":"Male","Vincent":"Male","Willy":"Male","Witch":"Female","Wizard":"Male",}
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

nb_names_dict = {"Abigail":"Ashley","Alex":"Alex","Birdie":"Birdie","Bouncer":"Bouncer","Caroline":"Cary","Charlie":"Charley","Clint":"Coby","Demetrius":"Dubaku","Dwarf":"Smoluanu","Elliott":"Eden","Emily":"Elery","Evelyn":"Evelyn","George":"Georgie","Gil":"Gili","Governor":"Governor","Grandpa":"Grandie","Gunther":"Greer","Gus":"Gabi","Haley":"Hadyn","Harvey":"Harper","Henchman":"Guard","Jas":"Jay","Jodi":"Joey","Kent":"Kim","Krobus":"Krobus","Leah":"Leigh","Leo":"Lee","Lewis":"Lou","Linus":"Lucky","Marcello":"Modeste","Marlon":"Merlyn","Marnie":"Martie","Maru":"Maru","MisterQi":"Qi","Morris":"Moran","OldMariner":"Old Mariner","Pam":"Pat","Penny":"Pip","Pierre":"Paget","ProfessorSnail":"Professor Snail","Robin":"Robin","Sam":"Sam","Sandy":"Sandy","Sebastian":"September","Shane":"Shae","Vincent":"Vinnie","Willy":"Willie","Witch":"Rowan","Wizard":"Morgan",}

variants_dict = {"Harvey": ["Shaved"],"Emily": ["LongSleeved"], "Pam": ["Young"], "Linus": ["Coat"],"Wizard": ["Young"]}
genderswap_list = ["Alex","Elliott","Harvey","Sam", "Shane","Sebastian","Wizard","Willy"]
   

birthday_code = False
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
    elif name =="Witch":
        return "Rowan"    
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
    elif name in ["Charlie","Gil","Witch"]:
        return ""
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
        new_name = realname(name)
        new_title = "Wizard"
        
        if current_gender =="Neutral":
            gender = "Neutral"
            pronoun = "They" 
            new_name =  nb_names_dict[name]  
            new_title = "Mage"
            if isHD:
                changesprite = "Androgynous"
            else:
               changing_char = True       
        elif current_gender =="Test":
            gender = "Neutral"
            pronoun = random.choice(pronouns)  
            new_name =  nb_names_dict[name]  
            new_title = "Mage"
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
                new_title = "Witch"  
                if isHD:
                    if  name in genderswap_list:
                        changesprite = "Female (no sprites)"
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
            if name =="Wizard":
                 content.write("  \""+name+"Title\": \""+new_title+"\",\n")   
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
            if birthday_code:
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

        if name =="Wizard":
            s += "    \""+name+"Title\": {\"Default\": \"Wizard\"},\n"
        
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
        if birthday_code:
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
    combined = [x for x in gender_words["Neutral"].keys()]+ [x for x in pronoun_words["They"].keys()]
    for word in combined:
        s += "                {\"Name\": \""+name+word+"\", \"Value\": \"{{sqbr.getGS/"+name+word+"}}\"},\n"           
    if name !="Farmer":
        if custom_possession!=True:
            s += "                {\"Name\": \""+name+"Possession\", \"Value\": \"{{sqbr.getGS/"+name+"Possession}}\"},\n" 
    if name =="Wizard":
            s += "                {\"Name\": \""+name+"Initial\", \"Value\": \"{{sqbr.getGS/"+name+"Initial}}\"},\n"     
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

def image_start_talkoh2(name, type, variant):
    #at the start of an image block 

    s= "		{\"Action\": \"EditImage\","
    if type =="sprite":
        location = "Characters/"
    else:
        if variant =="setup":
            location = "Mods/HDPortraits/" 
            s = "		{\"Action\":\"Load\","   
        else:    
            location = "Mods/talkohPortraits/"     

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
        return "\"When\": {\"MiscImageEdits\": \"true\",\"HasMod |contains=talkohlooeys.HiResPortraits\": false}},\n"
    else:    
        s = "\"When\": {"
        if variant =="Female":
            s+="\""+name+"FemalePortrait\": true"    
        elif variant =="Young" and name =="Wizard":
            s+="\"WizardYoungPortrait\": true"       
        elif variant !="":
            s+="\""+name+"Images\": \""+test_variable_talkoh(name, variant)+"\""  
        else:
            s+="\""+name+"Images|contains=false\": \"false\",\"HasMod |contains=talkohlooeys.HiResPortraits\": false"    
        s+="}},\n"
        return s

def image_end_talkoh2(name, type, variant):
    #at the end of an image block
    if name =="other":
        return "\"When\": {\"MiscImageEdits\": \"true\",\"HasMod |contains=talkohlooeys.HiResPortraits\": true}},\n"
    else:    
        s = "\"When\": {"
        if variant =="Female":
            s+="\""+name+"FemalePortrait\": true"    
        elif variant =="Young" and name =="Wizard":
            s+="\"WizardYoungPortrait\": true"       
        elif variant !="":
            s+="\""+name+"Images\": \""+test_variable_talkoh(name, variant)+"\""  
        else:
            s+="\""+name+"Images|contains=false\": \"false\",\"HasMod |contains=talkohlooeys.HiResPortraits\": true"    
        s+="}},\n"
        return s        

def image_line_talkoh(name, type,variant):
    if artname(name, type)=="":
        return ""
    else:
        return image_start_talkoh(name, type,variant) +image_middle_talkoh(name, type,variant)+image_end_talkoh(name, type, variant)    

def image_line_talkoh2(name, type,variant):
    if artname(name, type)=="":
        return ""
    else:
        return image_start_talkoh2(name, type,variant) +image_middle_talkoh(name, type,variant)+image_end_talkoh2(name, type, variant)    

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
        if isHD:
            return "\"When\": {\"MiscImageEdits\": \"true\",\"HasMod |contains=talkohlooeys.HiResPortraits\": false}},\n"
        else:
            return "\"When\": {\"MiscImageEdits\": \"true\"}},\n"    
    else:    
        s = "\"When\": {"
        if isHD and type =="sprite" and variant =="" and name in genderswap_list:
            s+="\""+name+"AndrogynousSprite\": true"
        elif variant !="" or isHD:
            s+="\""+name+"Images\": \""+test_variable(name, variant)+"\""  
        else:
            s+="\""+name+"Images|contains=false\": \"false\""  
        if isHD:
            s+=",\"HasMod |contains=talkohlooeys.HiResPortraits\": false"      
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
    elif name =="Witch":
        s+=image_pair_pos(name, "LooseSprites/Cursors", "Other/Cursors_witch","",276, 1885,0,0, 44, 61) #witch
    elif name =="Wizard":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 90, 108,90,108,9, 9)  
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 416, 212,64,0,32, 32)  
        s+=image_line_pos_loc(name,"Characters/KrobusRaven","sprite","",0,64,160,104)                    
    return s      

def image_code_background(): 
    s=image_pair_pos("other", "LooseSprites/Cursors2", "Other/Cursors2_fairy","",208, 256,0,0, 48, 64)  #fairy
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

def set_disposition(name):
    relationships = ""
    if name =="Abigail":
        relationships = "\"Caroline\": \"{{CarolineParent}}\", \"Pierre\": \"{{PierreParent}}\""
    elif name =="Emily":
        relationships = "\"Haley\": \"{{HaleySibling}}\""  
    elif name =="Alex":
        relationships = "\"George\": \"grandie {{GeorgeName}}\", \"Evelyn\": \"grandie {{EvelynName}}\""
    elif name =="Maru":
        relationships = "\"Robin\": \"{{RobinParent}}\", \"Demetrius\": \"{{DemetriusParent}}\", \"Sebastian\": \"half-{{SebastianSibling}}\""  
    elif name =="Penny":
        relationships = "\"Pam\": \"{{PamParent}}\""  
    elif name =="Sam":
        relationships = "\"Vincent\": \"little {{VincentSibling}}\", \"Jodi\": \"{{JodiParent}}\", Kent\": \"{{KentParent}}\""  
    elif name =="Sebastian":
        relationships = "\"Robin\": \"{{RobinParent}}\", \"Maru\": \"half-{{MaruSibling}}\""  
    elif name =="Shane":
        relationships = "\"Marnie\": \"{{MarnieAuncleU}}\""  
    elif name =="Caroline": 
        relationships = "\"Pierre\": \"{{PierreSpouse}}\""   
    elif name == "Demetrius": 
        relationships = "\"Robin\": \"{{RobinSpouse}}\""  
    elif name =="Evelyn": 
        relationships = "\"George\": \"{{GeorgeSpouse}}\", \"Alex\": \"grand{{AlexChild}}\""  
    elif name =="George": 
        relationships = "\"Evelyn\": \"{{EvelynSpouse}}\", \"Alex\": \"grand{{AlexChild}}\""   
    elif name =="Jodi": 
        relationships = "\"Sam\": \"{{SamChild}}\", \"Vincent\": \"{{VincentChild}}\", \"Kent\" \"{{KentSpouse}}\""  
    elif name =="Kent": 
        relationships = "\"Jodi\": \"{{JodiSpouse}}\", \"Sam\": \"{{SamChild}}\", \"Vincent\": \"{{VincentChild}}\""       
    elif name =="Marnie": 
        relationships = "\"Shane\": \"{{ShaneNibling}}\", \"Jas\": \"{{JasNibling}}\""  
    elif name =="Pam": 
        relationships = "\"Penny\": \"{{PennyChild}}\""  
    elif name =="Pierre": 
        relationships = "\"Abigail\": \"{{AbigailChild}}\", \"Caroline\": \"{{CarolineSpouse}}\""  
    elif name =="Robin": 
        relationships = "\"Demetrius\": \"{{DemetriusSpouse}}\", \"Maru\": \"{{MaruChild}}\", \"Sebastian\": \"{{SebastianChild}}\""                           

    s = "		{\"Action\": \"EditData\",\"Target\": \"Data/Characters\","
    s+="\"TargetField\": [\""+name+"\"],\n"
    s+="\"Entries\": {\n"
    s+="\"Gender\": "+str(genders.index(orig_gender_dict[name]))+",\n" 
    if relationships!="":
        s+="\"FriendsAndFamily\": {"+relationships+"},\n"
    s+="}"
    if name =="Leo":
        s+=",\"When\": {\"EditIslandCharacters\": \"Full\"}"
    s+="},\n"
    return s
    
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
        s += "		{\"Action\": \"EditData\",\"Target\": \"Data/NPCDispositions\",\"Update\": \"OnLocationChange\","
        s+="\"Fields\": {\""+name+"\": {4: \""+genderswap(o_gender).lower()+"\"}},"
        s+="\"When\": { \""+name+"GameGender\": \""+genderswap(o_gender)+"\",\"DayEvent|contains=flower dance\": \"false\"}},\n\n"
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
    content.write("{\n    \"Format\": \"2.0.0\",\n    \"ConfigSchema\":\n {\n")
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
    if isHD:
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
        content.write("\n")
        for name in birthday_dict.keys():
            content.write(set_disposition(name))
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
            s+= image_line_talkoh2(name, "portrait", variant)   
    s+= image_line_talkoh("Linus", "sprite", "Coat")
    s+="        {\"Action\": \"EditImage\",\"Target\": \"LooseSprites/BundleSprites\",\"FromFile\": \"assets/Characters/Variants/Coat/BundleSprites.png\",\"ToArea\": { \"X\": 160, \"Y\": 0, \"Width\": 32, \"Height\": 32 },\"When\": {\"LinusImages\": \"Male Coat\"}},\n"
    s+="        {\"Action\": \"EditImage\",\"Target\": \"LooseSprites/Cursors2\",\"FromFile\": \"assets/Characters/Variants/Coat/Cursors2.png\",\"ToArea\": { \"X\": 129, \"Y\": 241, \"Width\": 14, \"Height\": 15 },\"When\": {\"LinusImages\": \"Male Coat\"}},\n\n"
    s+= image_line_talkoh("Pam", "sprite", "Young")         
    for name in genderswap_list:
        s+= image_line_talkoh(name, "portrait", "Female") 
        if name in beach_bodies:
            s+="        {\"Action\": \"EditImage\",\"Target\":\"Mods/talkohSeasonal/"+portraitname(name) + "_Beach\","
            s+="\"FromFile\":\"assets/Portraits/Genderbent/Classic/"+ name+"_Beach.png\","
            s+="\"When\": {\""+name+"FemalePortrait\": true,  \"Genderbent Bachelors\": \"Classic\",\"HasMod |contains=talkohlooeys.HiResPortraits\": false}},\n"
            s+="        {\"Action\": \"EditImage\",\"Target\":\"Mods/talkohPortraits/"+portraitname(name) + "_Beach\","
            s+="\"FromFile\":\"assets/Portraits/Genderbent/Classic/"+ name+"_Beach.png\","
            s+="\"When\": {\""+name+"FemalePortrait\": true,  \"Genderbent Bachelors\": \"Classic\",\"HasMod |contains=talkohlooeys.HiResPortraits\": true}},\n"
        s+="\n"    
    return s 
 
def hd_setup():
    s = ""
    for name in portrait_list + other_portraits:
        end_string = "\"When\": {\""+name+"Images|contains=false\": \"false\",\"HasMod |contains=talkohlooeys.SeasonalPortraits\": false,\"HasMod |contains=talkohlooeys.HiResPortraits\": false}},\n"  
        name_string= "\"Mods/talkohSeasonal/"+portraitname(name) 
        if name in extras.keys():
            name_string+= ", Mods/talkohSeasonal/"+extras[name] 
        if name in beach_bodies:
            name_string+= ", Mods/talkohSeasonal/"+portraitname(name) + "_Beach, "
        name_string += "\","   
        s+="        {\"Action\":\"Load\",\"Target\":"+ name_string
        s+="\"FromFile\":\"assets/Portraits/{{TargetWithoutPath}}.png\","
        s+=end_string

        s += image_start_talkoh(name, "portrait", "setup")
        s+="\"FromFile\":\"assets/base.json\","
        s+= end_string

        name_string= "\"Mods/HDPortraits/"+portraitname(name)
        if name in extras.keys():
            name_string+= ", Mods/HDPortraits/"+extras[name] 
        if name in beach_bodies:
            name_string+= ", Mods/HDPortraits/"+portraitname(name) + "_Beach, "    
        name_string += "\","   
        s+="        {\"Action\":\"EditData\",\"Target\":"+ name_string
        s+="\"Entries\": {\"Portrait\":\"Mods/talkohSeasonal/{{TargetWithoutPath}}\"},"
        s+=end_string+"\n"
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
    for name in portrait_list + no_portrait_list + ["Witch"]:
        e=extra_sprites(name) 
        if e!="":
            s+=e 
            s+="\n"                
    return s

def token_line(name, word):
    return "    {\"Name\": \""+name+word+"\", \"Value\":: \"{{sqbr.getGS/"+name+word+"}}\", \"When\": {\"HasMod|contains=sqbr.getGS\" :\"true\"}},\n"

def create_tokens():
    #list of tokens for use within other mods referencing Gender Setter
    path = "./mine/tokens.json"  
    content = open(path,"w")
    for name in name_list:
        o_gender = orig_gender_dict[name]

        content.write("    {\"Name\": \""+name+"Name\", \"Value\": \""+realname(name)+"\"},\n")
        content.write(token_line(name, "Name"))
        if name =="Wizard":
            content.write("    {\"Name\": \""+name+"Title\", \"Value\": \"Wizard\"},\n")
            content.write(token_line(name, "Title"))
        
        content.write("    {\"Name\": \""+name+"Gender\", \"Value\": \""+o_gender+"\"},\n")
        content.write(token_line(name, "Gender"))

        content.write("    {\"Name\": \""+name+"Pronoun\", \"Value\": \""+orig_pronoun_dict[o_gender]+"\"},\n")
        content.write(token_line(name, "Pronoun"))
        #Set pronoun and gender related words
        for word in gender_words["Neutral"].keys():
            content.write("    {\"Name\": \""+name+word+"\",\"Value\":\""+gender_words[o_gender][word]+"\"},\n")
            content.write(token_line(name, word))
        for word in pronoun_words["They"].keys():  
            content.write("    {\"Name\": \""+name+word+"\",\"Value\":\""+pronoun_words[orig_pronoun_dict[o_gender]][word]+"\"},\n")
            content.write(token_line(name, word))  
        if custom_possession!=True:
            content.write("    {\"Name\": \""+name+"Possession\", \"Value\": \"'s\"},\n")
            content.write(token_line(name, "Possession"))
        content.write("\n")        
    content.close()            


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
   
create_tokens()   
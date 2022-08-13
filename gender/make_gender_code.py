from __future__ import print_function
import math
import glob
from re import S
from xml.etree.ElementTree import TreeBuilder

### A script to generate a mod from unpacked content
### To run, open a terminal/command line from within this folder and type "python make_gender_code.py"
###############
  
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
    dict1["_they"] = pronoun.lower()    
    for w in ["_they","_them","_their"]:    
        dict1[w+"U"] = dict1[w].capitalize()
    return dict1    

    
## General data       
   
end_path = "../../Genderiser/"
end_path_images = "../../Androgynous Villagers/"

## Original data

name_list1= ["Abigail","Alex","Birdie","Bouncer","Caroline","Charlie","Clint","Demetrius","Dwarf","Elliott","Emily","Evelyn","George","Gil","Governor","Grandpa","Gunther","Gus","Haley","Harvey","Henchman","Jas","Jodi","Kent","Krobus","Leah","Leo","Lewis","Linus","Marcello","Marlon","Marnie","Maru","MisterQi","Morris","OldMariner","Pam","Penny","Pierre",]
name_list2= ["Robin","Sam","Sandy","Sebastian","Shane","Vincent","Willy","Wizard",]
beach_bodies = ["Abigail","Alex","Caroline","Clint","Demetrius","Elliott","Emily","Haley","Harvey","Jodi","Leah","Lewis","Marnie","Maru","Pam","Penny","Pierre","Robin","Sam","Sebastian","Shane"]
spouse_list = ["Abigail","Alex","Elliott","Emily","Haley","Harvey","Leah","Maru","Penny","Sam","Sebastian","Shane"]

possession_dict= {"ProfessorSnail": "'s","Abigail":"'s","Alex":"'s","Birdie":"'s","Bouncer":"'s","Caroline":"'s","Charlie":"'s","Clint":"'s","Demetrius":"'","Dwarf":"'s","Elliott":"'s","Emily":"'s","Evelyn":"'s","George":"'s","Gil":"'s","Governor":"'s","Grandpa":"'s","Gunther":"'s","Gus":"'","Haley":"'s","Harvey":"'s","Henchman":"'s","Jas":"'","Jodi":"'s","Kent":"'s","Krobus":"'","Leah":"'s","Leo":"'s","Lewis":"'","Linus":"'","Marcello":"'s","Marlon":"'s","Marnie":"'s","Maru":"'s","MisterQi":"'s","Morris":"'","OldMariner":"'s","Pam":"'s","Penny":"'s","Pierre":"'s","Robin":"'s","Sam":"'s","Sandy":"'s","Sebastian":"'s","Shane":"'s","Vincent":"'s","Willy":"'s","Wizard":"'",}
orig_gender_dict = {"ProfessorSnail": "Male","Abigail":"Female","Alex":"Male","Birdie":"Female","Bouncer":"Male","Caroline":"Female","Charlie":"Female","Clint":"Male","Demetrius":"Male","Dwarf":"Male","Elliott":"Male","Emily":"Female","Evelyn":"Female","George":"Male","Gil":"Male","Governor":"Male","Grandpa":"Male","Gunther":"Male","Gus":"Male","Haley":"Female","Harvey":"Male","Henchman":"Male","Jas":"Female","Jodi":"Female","Kent":"Male","Krobus":"Male","Leah":"Female","Leo":"Male","Lewis":"Male","Linus":"Male","Marcello":"Male","Marlon":"Male","Marnie":"Female","Maru":"Female","MisterQi":"Male","Morris":"Male","OldMariner":"Male","Pam":"Female","Penny":"Female","Pierre":"Male","Robin":"Female","Sam":"Male","Sandy":"Female","Sebastian":"Male","Shane":"Male","Vincent":"Male","Willy":"Male","Wizard":"Male",}
orig_pronoun_dict ={
    "Male": "He",
    "Female": "She",
}

name_list = name_list1 + ["ProfessorSnail"]+name_list2

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
  "Marlon": "winter 19",
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

variables_dict = {"Child2": "_godchild", "Child3": "nibling", 
    "GenderUC":"_They","GenderLC":"_they","PronounUC1":"_Them","PronounLC1":"_them","PronounUC2":"_Their","PronounLC2":"_their","PronounLC3":"_theirs",
    "GenderLC2":"_adult","GenderLC3":"_guy","GenderLC4":"_kid","Child":"_child","Sibling":"_sibling","Relation":"_Auncle","ParentUC":"_Parent","ParentLC":"_parent","MarriedUC":"_Spouse","MarriedLC":"_spouse","Marital":"_Mx","Elder":"_Grandparent",}

nb_names_dict = {"Abigail":"Ashley","Alex":"Alex2","Birdie":"Birdie2","Bouncer":"Bouncer2","Caroline":"Cary","Charlie":"Charley","Clint":"Coby","Demetrius":"Dubaku","Dwarf":"Smoluanu","Elliott":"Eden","Emily":"Elery","Evelyn":"Evelyn2","George":"Georgie","Gil":"Gili","Governor":"Governor2","Grandpa":"Grandie","Gunther":"Greer","Gus":"Gabi","Haley":"Hadyn","Harvey":"Harper","Henchman":"Guard","Jas":"Jay","Jodi":"Joey","Kent":"Kim","Krobus":"Krobus2","Leah":"Leigh","Leo":"Lee","Lewis":"Lou","Linus":"Lucky","Marcello":"Modeste","Marlon":"Merlyn","Marnie":"Martie","Maru":"Maru2","MisterQi":"Qi","Morris":"Moran","OldMariner":"Old Mariner2","Pam":"Pat","Penny":"Pip","Pierre":"Paget","ProfessorSnail":"Professor Snail2","Robin":"Robin2","Sam":"Sam2","Sandy":"Sandy2","Sebastian":"September","Shane":"Shae","Vincent":"Vinnie","Willy":"Willie","Wizard":"Ma'akhah",}

birthday_code = True
nb_config = True
custom_possession = False
edit_text = True

## New data
genders = ["Male","Female","Neutral"]
pronouns = ["He","She","They","They (singular)","It","Xe","Fae","E"]
singular_words = { 
    "_are":"is",
    "_were":"was",
    "_have":"has",
    "_'re":"'s",
    "_'ve":"'s",
    "_s":"s",
    "_es":"es"}
plural_words = {
    "_are":"are",
    "_were":"were",
    "_have":"have",
    "_'re":"'re",
    "_'ve":"'ve",
    "_s":"",
    "_es":""}
pronoun_words = {
    "She": make_p_dict("She",{"_them":"her","_their":"her","_theirs":"hers","_themself":"herself"} ,singular_words),
    "He": make_p_dict("He", {"_them":"him","_their":"his","_theirs":"his","_themself":"himself"}, singular_words),
    "They": make_p_dict("They", {"_them":"them", "_their":"their","_theirs":"theirs","_themself":"themself"}, plural_words),
    "They (singular)": make_p_dict("They", {"_them":"them", "_their":"their","_theirs":"theirs","_themself":"themself"},  singular_words),
    "It": make_p_dict("It", {"_them":"it","_their":"its","_theirs":"its","_themself":"itself"}, singular_words),
    "Xe": make_p_dict("Xe", {"_them":"xem","_their":"xyr","_theirs":"xyrs","_themself":"xemself"}, singular_words),
    "Fae": make_p_dict("Fae", {"_them":"faer","_their":"faer","_theirs":"faers","_themself":"faerself"}, singular_words),
    "E": make_p_dict("E", {"_them":"em","_their":"eir","_theirs":"eirs","_themself":"emself"}, singular_words),
    "Ze": make_p_dict("Ze", {"_them":"hir","_their":"hir","_theirs":"hirs","_themself":"hirself"}, singular_words),
}

gender_words = {
    "Female": {"_adult":"woman","_guy":"girl","_kid":"girl","_child":"daughter","_sibling":"sister","_Auncle":"Aunt","_parent":"mother","_parentU":"Mom","_spouse":"wife","_spouseU":"Wife","_Mx":"Mrs.","_Grandparent":"Granny"},
    "Male": {"_adult":"man","_guy":"guy","_kid":"boy","_child":"son","_sibling":"brother","_Auncle":"Uncle","_parent":"father","_parentU":"Dad","_spouse":"husband","_spouseU":"Husband","_Mx":"Mr.","_Grandparent":"Grandpa"},
    "Neutral": {"_adult":"person","_guy":"person","_kid":"kid","_child":"child","_sibling":"sibling","_Auncle":"Auncle","_parent":"parent","_parentU":"Parent","_spouse":"spouse","_spouseU":"Spouse","_Mx":"Mx.","_Grandparent":"Grandie"},

}

neutralparent_dict = {"Vincent_guy":"kid","Evelyn_Grandparent": "Grandie {{EvelynName}}", "George_Grandparent": "Grandie {{GeorgeName}}"}
for name in ["Pierre", "Caroline", "Kent","Jodi","Robin","Demetrius","Evelyn",]:
    neutralparent_dict[name+"_parent"] = "parent "+"{{"+name+"Name}}"
    neutralparent_dict[name+"_parentU"] = "Parent "+"{{"+name+"Name}}"

gender_exceptions = { 
    "Female": {"Lewis_Mx": "Ms.", "Morris_Mx": "Ms.","Penny_Mx": "Miss","Birdie_guy": "lady","Governor_adult": "girl"},
    "Male": {"Penny_Mx": "Mister", "Birdie_guy": "man", "Governor_adult": "guy"},
    "Neutral": neutralparent_dict,
    }

darker_chars = ["Marnie","Jas","Elliott","Grandpa"]
wheelchair_chars = ["Leah"]

## Data processing   

def realname(name):
    #real name original of character, removes spaces and aliases
    if nb_config:
        return nb_names_dict[name]
    else:    
        if name =="MisterQi":
            return "Mister Qi"
        elif name =="OldMariner": 
                return "Old Mariner"   
        elif name =="Wizard":
            return "Magnus"
        else:
            return name   

def artname(name):
    #name of art file for character
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

def genderswap(gender):
    if gender =="Male":
        return "Female"
    elif gender =="Female":
        return "Male"   
    else:
        return gender                        

def create_config():
    #create config file
    if edit_text:
        path = end_path+"config.json"
    else:
        path = end_path_images+"config.json"    
    content = open(path,"w")
    content.write("{\n")
    if edit_text:
        content.write("  \"EditIslandCharacters\": \"Full\",\n")
        content.write("  \"MiscTextEdits\": \"true\",\n")
    content.write("  \"MiscImageEdits\": \"true\",\n")
    content.write("\n")
    for name in name_list:
        o_gender = orig_gender_dict[name]
        if nb_config:
            gender = "Neutral"
            g_gender =o_gender
            pronoun = "They"
            if name in darker_chars:
                changesprite = "Darker"
            elif name in wheelchair_chars:
                changesprite = "Wheelchair"  
            else:
                changesprite = "true"
            new_name =  nb_names_dict[name]   
        else:    
            gender = o_gender
            g_gender = o_gender
            pronoun = orig_pronoun_dict[o_gender]
            changesprite = "false"
            new_name = name
        if edit_text:
            content.write("  \""+name+"Name\": \""+new_name+"\",\n")    
            content.write("  \""+name+"Gender\": \""+gender+"\",\n")    
            content.write("  \""+name+"Pronoun\": \""+pronoun+"\",\n")    
        content.write("  \""+name+"Images\":\" "+changesprite+"\",\n")             
   
    if edit_text:
        with open("./advancedtitle_config.json","r") as f:
            data = f.readlines()
        for l in data:
            content.write(l)
        content.write("  \"PatchOriginalWeddingArt\": \"false\",\n\n")     
        for name in name_list:
            if name in birthday_dict.keys(): 
                content.write("  \""+name+"Birthday"+"\": \""+birthday_dict[name]+"\",\n") 
            if custom_possession:
                content.write("  \""+name+"Possession\": \""+possession_dict[name]+"\",\n")  
            if name in spouse_list:
                content.write("  \""+name+"GameGender\": \""+ g_gender+"\",\n")       
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
    if edit_text:
        s += "    \""+name+"Name\": {\"Default\": \""+realname(name)+"\"},\n"
        
        s+="    \""+name+"Gender\": {\"Default\": \""+o_gender+"\","+gender_string()+"},\n"

        s+="    \""+name+"Pronoun\": {\"Default\": \""+orig_pronoun_dict[o_gender]+"\","+pronoun_string()+"},\n"
    if name in darker_chars:
        s+="    \""+name+"Images\": {\"Default\": \""+"false"+"\",\"AllowValues\": \"Lighter,Darker,false\"},\n"
    elif name in wheelchair_chars:    
        s+="    \""+name+"Images\": {\"Default\": \""+"false"+"\",\"AllowValues\": \"Able-bodied, Wheelchair, false\"},\n"
    else:
        s+="    \""+name+"Images\": {\"Default\": \""+"false"+"\",\"AllowValues\": \"true,false\"},\n"    
    s+="\n"

    return s

def initialise_advanced(name): 
    s = ""  
    if edit_text: 
        if name in birthday_dict.keys(): 
            s+="    \""+name+"Birthday"+"\": {\"Default\": \""+birthday_dict[name]+"\"},\n" 
        if custom_possession:
            s+="    \""+name+"Possession\": \"'s\",\n"     
    if name in spouse_list:
        s+="    \""+name+"GameGender\": {\"Default\": \""+orig_gender_dict[name]+"\", \"AllowValues\": \"Male, Female\"},\n"       
    if not s =="":
        s+="\n"

    return s    

def gender_variables(name):
    #Set pronoun and gender related words
    s = ""
    for g in genders:
        g_dict = gender_words[g]
        for word in g_dict.keys():
            s += "                {\"Name\": \""+name+word+"\","
            if name+word in gender_exceptions[g].keys():
                variable = gender_exceptions[g][name+word]
            else:
                variable = g_dict[word]    
            s += "\"Value\": \""+variable+"\",\"When\": { \""+name+"Gender\": \""+g+"\" }},\n"
        if name == "Elliott": 
            s += "                {\"Name\": \"ElliottLetter\", \"Value\": \""+g_dict["_spouse"]+"\"," 
            s += "\"When\": { \""+name+"Gender\": \""+g+"\" }},\n"     
        elif name =="Shane":
            s += "                {\"Name\": \"Shane_godchild\", \"Value\": \"god"+g_dict["_child"]+"\"," 
            s += "\"When\": { \""+name+"Gender\": \""+g+"\" }},\n" 
    s+="\n"
    for p in pronouns:
        g_dict = pronoun_words[p]
        for word in g_dict.keys():
            variable = g_dict[word]  
            s += "                {\"Name\": \""+name+word+"\", \"Value\": \""+variable+"\", \"When\": { \""+name+"Pronoun\": \""+p+"\" }},\n"
          
    if name =="Shane":
            s += "                {\"Name\": \"Shane_nibling\", \"Value\": \"niece\", \"When\": { \"ShaneGender\": \"Female\" }},\n"
            s += "                {\"Name\": \"Shane_nibling\", \"Value\": \"nephew\", \"When\": { \"ShaneGender\": \"Male\" }},\n"     
    if custom_possession!=True:
        s+="                {\"Name\": \""+name+"Possession\", \"Value\":\"'s\"},\n"          
    s+="\n"
    return s

def image_start(location,extra):
    #at the start of an image block
    if extra =="":
        return "		 {\"Action\": \"EditImage\",\"Target\": \"" + location+"\",\"FromFile\": \"assets/{{Target}}.png\","
    else:
        return "		 {\"Action\": \"EditImage\",\"Target\": \"" + location+"\",\"FromFile\": \"assets/"+location+"_"+extra+".png\","

def image_end(name,extra):
    #at the end of an image block
    if name =="other":
        return "\"When\": {\"MiscImageEdits\": \"true\"}},\n"
    else:    
        s = "\"When\": {"
        if extra !="":
            s+="\""+name+"Images\": \""+extra+"\""  
        else:
            s+="\""+name+"Images|contains=false\": \"false\""    
        s+="}},\n"
        return s

def image_line(name, location,extra):
    #code to replace image at location
    return image_start(location,extra) +image_end(name,extra)


def image_line_pos(name, location, extra,x, y, w, h):
    #code to replace image at location in a given box
    s =image_start(location,"")
    pos_string ="{ \"X\": "+str(x)+", \"Y\": "+str(y)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }" 
    s+="\"FromArea\": "+pos_string+",\"ToArea\":  "+pos_string+","
    s+=image_end(name,extra)
    return s

def image_pair(name, location1, location2,extra):
    #code to replace image at location in a given box
    s ="		 {\"Action\": \"EditImage\",\"Target\": \"" + location1+"\",\"FromFile\": \"assets/"+location2+".png\","
    s+=image_end(name,extra)
    return s    

def image_pair_pos(name, location1, location2, extra,x1, y1, x2,y2,w, h):
    #code to replace image at location in a given box
    if extra =="":
        location = location2
    else:
        location = location2+"_"+extra    
    s ="		 {\"Action\": \"EditImage\",\"Target\": \"" + location1+"\",\"FromFile\": \"assets/"+location+".png\","
    s+="\"FromArea\": { \"X\": "+str(x2)+", \"Y\": "+str(y2)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }," 
    s+="\"ToArea\": { \"X\": "+str(x1)+", \"Y\": "+str(y1)+", \"Width\": "+str(w)+", \"Height\": "+str(h)+" }," 
    s+=image_end(name,extra)
    return s    

def image_line_spouse(name,extra):
    #name of spouse, any extra properties like "Wheelchair"
    o_gender = orig_gender_dict[name]
    art_name = artname(name)
    location = "Characters/"+art_name
    if extra =="":
        e_string =""
        e_var = "\""+name+"Images|contains=false\": \"false\""
    else:
        e_string ="_"+extra 
        e_var = "\""+name+"Images\": \""+extra+"\""  
    s="		 {\"Action\": \"EditImage\",\"Target\": \"" + location+"\",\"FromFile\": \"assets/Characters/"+art_name+e_string+".png\","
    s+="\"When\": {"+e_var+"}},\n"
    s+="		 {\"Action\": \"EditImage\",\"Target\": \"" + location+"\",\"FromFile\": \"assets/Characters/"+art_name+e_string+".png\","
    s+="\"FromArea\": { \"X\": 0, \"Y\": 288, \"Width\": 48, \"Height\": 32 }," 
    s+="\"ToArea\": { \"X\": 0, \"Y\": 384, \"Width\": 48, \"Height\": 32 }," 
    s+="\"When\": {\""+name+"GameGender\": \""+genderswap(o_gender)+"\", \"DayEvent|contains=flower dance\": \"false\","+e_var+"}},\n"    
    if not name in ["Maru","Haley"]: #have shorter sprite sheets
        s+="		 {\"Action\": \"EditImage\",\"Target\": \"" + location+"\",\"FromFile\": \"assets/Characters/"+art_name+e_string+".png\","
        s+="\"FromArea\": { \"X\": 0, \"Y\": 384, \"Width\": 48, \"Height\": 32 }," 
        s+="\"ToArea\": { \"X\": 0, \"Y\": 288, \"Width\": 48, \"Height\": 32 }," 
        s+="\"When\": {\""+name+"GameGender\": \""+genderswap(o_gender)+"\", \"DayEvent|contains=flower dance\": \"false\","+e_var+"}},\n"   
    return s

def image_code(name):  
    #all image replacements for character called name
    s = ""
    art_name = artname(name)
    if art_name == "None":
        s+=""
    else:
        location = "Characters/"+art_name
        if name in spouse_list:
            #need gendered variants
            s+= image_line_spouse(name,"")
            if name in darker_chars:
                s+=image_line_spouse(name,"Darker")
            elif name in wheelchair_chars:    
                s+=image_line_spouse(name,"Wheelchair")
        else:    
            s+=image_line(name,location,"")
            if name in darker_chars:
                s+=image_line(name,location, "Darker")

        s+=image_line(name,"Portraits/"+art_name,"")   
        if name in darker_chars:
            s+=image_line(name,"Portraits/"+art_name,"Darker")   

        if name in beach_bodies:
            s+=image_line(name,"Characters/"+art_name+"_Beach","")
            s+=image_line(name,"Portraits/"+art_name+"_Beach","")
            if name in darker_chars:
                s+=image_line(name,"Characters/"+art_name+"_Beach", "Darker")
                s+=image_line(name,"Portraits/"+art_name+"_Beach", "Darker")
    if name =="Abigail":
        s+=image_line_pos(name, "Characters/ClothesTherapyCharacters","", 0, 32, 64, 32)   
        s+=image_line_pos(name, "Characters/ClothesTherapyCharacters","", 0, 160, 16, 32) 
    elif name =="Caroline":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 9, 108,9,108,9, 9)    
    elif name =="Clint":
        s+=image_line_pos(name,"Characters/ClothesTherapyCharacters","", 0, 64, 64, 32)  
        s+=image_line_pos(name,"Characters/ClothesTherapyCharacters","", 32, 160, 32, 32) 
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 54, 117,54,117,9, 9)       
    elif name =="Elliott":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 99, 99,99,99,9, 9)  
    elif name =="Gil":
        s+=image_line(name,"Portraits/Gil","")   
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
    elif name =="Haley":
        s+=image_pair(name, "LooseSprites/CowPhotos","Haley/CowPhotos","")
        s+=image_pair(name, "LooseSprites/CowPhotosWinter","Haley/CowPhotoWinters","")
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 36, 99,36,99,9, 9)  
    elif name =="Harvey":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 90, 99,90,99,9, 9)      
    elif name =="Jas":
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","",164, 97, 34,32,13, 20)   
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","Darker",164, 97, 34,32,13, 20) 
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 108, 108,108,108,9, 9)
    elif name =="Jodi":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 45, 108,45,108,9, 9)  
    elif name =="Lewis":
        s+=image_line_pos(name,"Characters/ClothesTherapyCharacters","", 0, 32, 64, 32)  
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 54, 108,54,108,9, 9)  
    elif name =="Linus":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 63, 108,63,108,9, 9)                        
    elif name =="Marnie":
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","", 146, 89, 16,24,18, 28) 
        s+=image_pair_pos(name, "TileSheets/SecretNotesImages","MarnieJas/SecretNotesImages","Darker", 146, 89, 16,24,18, 28)   
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Cursors_Marnie","", 557, 1424,0,0,62, 28)    
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Cursors_Marnie","Darker", 557, 1424,0,0,62, 28) 
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 0, 108,0,108,9, 9)  
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 0, 108,0,108,9, 9)           
    elif name =="Maru":     
        s+=image_line(name,"Portraits/Maru_Hospital","") 
        s+=image_line(name,"Characters/Maru_Hospital","") 
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
        s+=image_line_pos(name,"Characters/ClothesTherapyCharacters","", 0, 96, 64, 32) 
        s+=image_line_pos(name,"Characters/ClothesTherapyCharacters","", 16, 160, 16, 32)         
    elif name =="Shane":
        s+=image_line_pos(name, "Characters/ClothesTherapyCharacters","", 0, 0, 64, 32)  
        s+=image_line_pos(name, "Characters/ClothesTherapyCharacters","", 0, 0, 64, 32)  
    elif name =="Willy":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 81, 108,81,108,9, 9)
    elif name =="Wizard":
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 90, 108,90,108,9, 9)                   
    return s

def image_code_background(): 
    s=image_pair_pos("other", "LooseSprites/Cursors2", "Other/Cursors2_fairy","",208, 256,0,0, 48, 64)  #fairy
    s+=image_pair_pos("other", "LooseSprites/Cursors", "Other/Cursors_witch","",276, 1885,0,0, 44, 61) #witch
    s+=image_pair_pos("other", "Minigames/jojacorps", "Other/jojacorps","",0, 420,0,420, 264, 179) #farmer face
    s+=image_pair_pos("other", "Minigames/jojacorps", "Other/jojacorps","",0, 600,0,600, 1200, 200) #computers
    s+=image_line("other","Characters/Toddler","")   #toddlers
    s+=image_line("other","Characters/Toddler_girl","")   
    s+=image_line("other","Characters/Toddler_dark","") 
    s+=image_line("other","Characters/Toddler_girl_dark","")   
    return s


def disposition(name,gender):
    if name =="Abigail":
        return "teen/rude/outgoing/neutral/"+gender+"/datable/Sebastian/Town/{{AbigailBirthday}}/Caroline '{{Caroline_parent}}' Pierre '{{Pierre_parent}}'/SeedShop 1 9/{{AbigailName}}"
    elif name =="Elliott":
        return "adult/polite/neutral/neutral/"+gender+"/datable/Leah/Town/{{ElliottBirthday}}/Willy ''/ElliottHouse 1 5/{{ElliottName}}"
    elif name =="Emily":
        return "adult/polite/outgoing/positive/"+gender+"/datable/null/Town/{{EmilyBirthday}}/Haley '{{Haley_sibling}}'/HaleyHouse 16 5/{{EmilyName}}"   
    elif name =="Haley":
        return "adult/rude/outgoing/neutral/"+gender+"/datable/Alex/Town/{{HaleyBirthday}}/Emily '{{Emily_sibling}}'/HaleyHouse 8 7/{{HaleyName}}"
    elif name =="Harvey":
        return "adult/polite/shy/positive/"+gender+"/datable/Maru/Town/{{HarveyBirthday}}//HarveyRoom 13 4/{{HarveyName}}"      
    elif name =="Alex":
        return "adult/rude/outgoing/positive/"+gender+"/datable/Haley/Town/{{AlexBirthday}}/George 'grandie {{GeorgeName}}' Evelyn 'grandie {{EvelynName}}'/JoshHouse 19 5/{{AlexName}}"
    elif name =="Leah":
        return "adult/polite/neutral/positive/"+gender+"/datable/Elliott/Town/{{LeahBirthday}}//LeahHouse 3 7/{{LeahName}}"    
    elif name =="Maru":
        return "teen/neutral/outgoing/positive/"+gender+"/datable/Harvey/Town/{{MaruBirthday}}/Robin '{{Robin_parent}}' Demetrius '{{Demetrius_parent}}' Sebastian 'half-{{Sebastian_sibling}}'/ScienceHouse 2 4/{{MaruName}}"
    elif name =="Penny":
        return "teen/polite/shy/positive/"+gender+"/datable/Sam/Town/{{PennyBirthday}}/Pam '{{Pam_parent}}'/Trailer 4 9/{{PennyName}}"      
    elif name =="Sam":
        return "teen/neutral/outgoing/positive/"+gender+"/datable/Penny/Town/{{SamBirthday}}/Vincent 'little {{Vincent_sibling}}' Jodi '{{Jodi_parent}}' Kent '{{Kent_parent}}' Sebastian ''/SamHouse 22 13/{{SamName}}"
    elif name =="Sebastian":
        return "teen/rude/shy/negative/"+gender+"/datable/Abigail/Town/{{SebastianBirthday}}/Robin '{{Robin_parent}}' Maru 'half-{{Maru_sibling}}' Sam ''/SebastianRoom 10 9/{{SebastianName}}"    
    elif name =="Shane":
        return "adult/rude/shy/negative/"+gender+"/datable/null/Town/{{ShaneBirthday}}/Marnie '{{Marnie_Auncle}}'/AnimalShop 25 6/{{ShaneName}}"            


def replace_flowers():
    s = "\n"
    for name in spouse_list:
        o_gender =  orig_gender_dict[name]
        s += "             {\"Action\": \"EditImage\",\"Target\": \"Characters/"+name+"\","
        s += "\"FromFile\": \"assets/Wedding/"+name+"_Wedding.png\",\"ToArea\": { \"X\": 0, \"Y\": 288, \"Width\": 48, \"Height\": 32 },"
        s += "\"When\": { \""+name+"GameGender\": \""+genderswap(o_gender)+"\", \"DayEvent\": \"wedding\",\""+name+"Images\":\"false\", \"PatchOriginalWeddingArt\":\"true\"}},"
        s+="\n"
        s+= "             {\"Action\": \"EditData\",\"Target\": \"Data/NPCDispositions\",\"Update\": \"OnLocationChange\","
        s+="\"When\": { \""+name+"GameGender\": \""+genderswap(o_gender)+"\",\"DayEvent|contains=flower dance\": \"false\"},"
        s+="\"Entries\": {\""+name+"\":\""+disposition(name,genderswap(o_gender))+"\"}},"
        s+="\n\n"
    s+="             {\"Action\": \"EditData\",\"Target\": \"Strings/Locations\",\n"
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
    # Create content.json
    if edit_text:
        path = end_path+"content.json"
    else:
        path = end_path_images+"content.json"  
    content = open(path,"w")
    content.write("{\n    \"Format\": \"1.23\",\n    \"ConfigSchema\":\n {\n")
    if edit_text:
            content.write("    \"EditIslandCharacters\": { \"AllowValues\": \"Full, Minimal, None\",\"Default\": \"Full\"},\n")
            content.write("    \"MiscTextEdits\": { \"AllowValues\": \"true, false\",\"Default\": \"true\"},\n")
    content.write("    \"MiscImageEdits\": { \"AllowValues\": \"true, false\",\"Default\": \"true\"},\n\n")
    for name in name_list:
        content.write(initialise_variables(name))  
    if edit_text:
        with open("./advancedtitle_content.json","r") as f:
            data = f.readlines()
        for l in data:
            content.write(l)
        content.write("    \"PatchOriginalWeddingArt\": { \"AllowValues\": \"true, false\",\"Default\": \"false\"},\n\n")    
        for name in name_list:
            content.write(initialise_advanced(name))      
    content.write("    },\n")        
    content.write("    \"DynamicTokens\": [\n")         
    if edit_text:
        for name in name_list:
            content.write(gender_variables(name))  
    content.write("    ],\n")  
    content.write("	\"Changes\": [\n")  
    for name in name_list:
        content.write(image_code(name))     
    content.write(image_code_background())     
    if edit_text:
        with open("./mine/birthday_disposition.json","r") as f:
            content.write(f.read())
        with open("./mine/change_names.json","r") as f:
            content.write(f.read())	
        content.write(replace_flowers())	       
        with open("./mine/dialogue_objects.json","r") as f:
            content.write(f.read())	  
        with open("./mine/my_dialogue_fixes.json","r") as f:
            content.write(f.read())	      
        content.write(wedding_code())            
    content.write("	]\n}") 
    content.close()   
       
create_config() 
create_content()
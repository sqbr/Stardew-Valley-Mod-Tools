def image_code_old(name):  
    #all image replacements for character called name
    s = ""
    art_name = spritename(name)
    if art_name == "None":
        s+=""
    else:
        location = "Characters/"+art_name
        if name in spouse_list and isGS:
            #need gendered variants
            s+= image_lineSpouse(name,"")
            if name in darker_chars:
                s+=image_lineSpouse(name,"Darker")
            elif name in wheelchair_chars:    
                s+=image_lineSpouse(name,"Wheelchair")
        else: 
            if name =="Kent":
                s+=image_line_pos(name,location,"", 0, 0, 64, 160) #for compatibility with Kent does the dishes  
            else:       
                s+=image_line(name,location,"")
            if name in darker_chars:
                s+=image_line(name,location, "Darker")
            if name in wheelchair_chars:    
                s+=image_line(name,location,"Wheelchair")    
            if name in islander_chars:    
                s+=image_line(name,location,"Islander")         

        if name not in ["Marcello","OldMariner"]:
            s+=image_line(name,"Portraits/"+art_name,"")   
        if name in darker_chars:
            s+=image_line(name,"Portraits/"+art_name,"Darker") 
        elif name in islander_chars:    
            s+=image_line(name,"Portraits/"+art_name,"Islander")       

        if name in beach_bodies:
            s+=image_line(name,"Characters/"+art_name+"_Beach","")
            if name not in ["Lewis","Demetrius"]:
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
    elif name =="Emily":
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 448, 212,96,0,32, 32)      
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
        s+=image_line(name,"Portraits/Krobus_Trenchcoat","")   
        s+=image_line_pos(name,"Characters/KrobusRaven","",0,0,160,32)      
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
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Marnie_Paintings","", 0, 1925,0,0,50, 47)   
        s+=image_pair_pos(name, "LooseSprites/Cursors","MarnieJas/Marnie_Paintings","Darker", 0, 1925,0,0,50, 47)   
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","", 0, 108,0,108,9, 9)  
        s+=image_pair_pos(name, "LooseSprites/emojis","Other/emojis","Darker", 0, 108,0,108,9, 9)    
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 480, 212,128,0,32, 32) 
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","Darker", 480, 212,128,0,32, 32)        
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
        s+=image_pair_pos(name, "LooseSprites/JunimoNote","Other/emojis","", 416, 212,64,0,32, 32)  
        s+=image_line_pos(name,"Characters/KrobusRaven","",0,64,160,104)                    
    return s   

def sprite_variant_code(name,variant):
    #code for variant character sprite
    base_location = "Characters/"    
    beach_code = ""
    if name in beach_bodies and (name,variant) !=("Emily","LongSleeved"):
        beach_code =", "+base_location
        beach_code+=name+"_Beach"
    middle = "			\"Target\":\""+base_location+spritename(name) + beach_code + "\",\n"        
    test_string = variant
    if variant == "Female": #do  not have these images
        location = "Characters/Genderbent/"
        middle_string = "			\"Target\":\""+base_location+spritename(name)+ "\",\n" 
    elif variant == "Androgynous":
        location = "Characters/Androgynous/"
        middle_string = middle      
    else:
        middle_string = middle  
        if variant in ["Young","Coat"]:
            location = "Characters/Variants/"+variant + "/"
            test_string = orig_gender_dict[name]+ " "+ variant 
        else:    
            test_string = "Androgynous "+ variant 
            location = "Characters/Androgynous/Variants/" +variant + "/"     
    s = "        {\n			\"Action\":\"EditImage\",\n"
    s+=middle_string
    s+="			\"FromFile\":\"assets/" + location+ "{{TargetWithoutPath}}.png\",\n"
    s+= " 			\"When\": {\""+name+" Images\": \""+test_string+"\"}\n        },\n\n" 
    return s    


def HD_variant_code_old(name,variant):
    #code for variant HD portrait
    if variant =="":
        base_location = "Mods/HDPortraits/"
    else:
        base_location = "Mods/talkohSeasonal/"    
    beach_code = ""
    if name in beach_bodies and (name,variant) !=("Emily","LongSleeved"):
        beach_code =", "+base_location
        beach_code+=name+"_Beach"
    middle = "			\"Target\":\""+base_location+portraitname(name) + beach_code + "\",\n"     
    if variant =="":
        s = "        {\n			\"Action\":\"Load\",\n"
        s+=middle
        s+="			\"FromFile\":\"assets/base.json\",\n"
        s+= " 			\"When\": {\""+name+" Images|contains=false\": \"false\",\"HasMod |contains=talkohlooeys.SeasonalPortraits\": false}\n        },\n\n"      
    else:    
        test_string = variant
        if variant == "Female":
            location = "Portraits/Genderbent/"
            middle_string = "			\"Target\":\""+base_location+portraitname(name)+ "\",\n" 
        elif variant == "Androgynous":
           location = "Portraits/Androgynous/"   
           middle_string = middle  
        elif variant == "Wheelchair":   #portrait the same as androgynous
            location = "Portraits/Androgynous/"   
            middle_string = middle      
            test_string = "Androgynous "+ variant
        else:
            middle_string = middle  
            if variant in ["Young","Coat","LongSleeved", "Shaved"]:
                location = "Portraits/Variants/"+variant + "/"
                test_string = orig_gender_dict[name]+ " "+ variant
            else:    
                test_string = "Androgynous "+ variant
                location = "Portraits/Androgynous/Variants/" +variant + "/"     
        s = "        {\n			\"Action\":\"EditImage\",\n"
        s+=middle_string
        s+="			\"FromFile\":\"assets/" + location+ "{{TargetWithoutPath}}.png\",\n"
        s+= " 			\"When\": {\""+name+" Images\": \""+test_string+"\"}\n        },\n\n" 
    return s    
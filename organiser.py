import os
from pathlib  import Path #Objet path
import shutil

#Classer les fichiers par catégorie

def organiser_fichier(chemin_dossierSource): 
    categories = {
        'Images':['.jpg','.jpeg','.png','.gif','.svg','.bmp', '.svg','webp','.ico'], 
        'Documents' : ['.pdf','.doc', '.docx','.txt','.odt','.rtf', '.tex'], 
        'Data': ['.xls', '.xlsx', '.csv', '.ods'], 
        'Presentations': ['.ppt', '.pptx', '.odp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
        'Executables': ['.exe', '.msi', '.app', '.deb', '.rpm'],
    }
    
    #Dossier parent
    chemin = Path(chemin_dossierSource) #/"not.txt" pour accéder au fichier 
    if not chemin.exists(): 
        print(f"❌ Le dossier '{chemin_dossierSource}' n'existe pas.")
        return #Stop, on arrête la fonction ici si n'exist pas

    compteur = 0 
    #parcourir les fichiers existant dans le dossier 
    
    for fichier in chemin.iterdir():  #iterdir, Iterate over directory contents (children) of this path.
        print(fichier)
        
        if fichier.is_dir():  #ignore les dossiers
            continue 
        
        extension = fichier.suffix.lower()
        #print(extension) 
    
        for lesCategories , lesExtensions in categories.items() : #keys + values 
            
            if extension in lesExtensions : 
                
                #récuperer les catégories des fichiers dans le dossier
                nameCategory = lesCategories 
                print("Les categories existants : ", nameCategory)
                break #traite directement les pgm svt 
        
        #Une fois parcourus tous les catégories => décider 
        if not nameCategory: 
            nameCategory = "Autres"

        #Dossier enfant de parent "Chemin"
        sous_dossier = chemin / nameCategory #@adresse
        sous_dossier.mkdir(exist_ok=True) #construct , sans erreur si existe

        try: 
            #le nouveau fichier à rajouter
            nouveauChemin = sous_dossier / fichier.name #.name function de pathlib >> demo.txt et .stem >> demo 

            #gerer les doublons 
            if nouveauChemin.exists(): 
                base = fichier.stem #attribut 
                extension = fichier.suffix #attribut 
                i= 1 
                while nouveauChemin.exists() : 
                    nouveauChemin = sous_dossier / f"{base}_{i}{extension}"
                    i+=1

            shutil.move(str(fichier),str(nouveauChemin))      
            print(f"✓ {fichier.name} → {nameCategory}/")
            compteur += 1 


        except Exception as e : 
             print(f"❌ Erreur lors du déplacement de {fichier.name}: {e}")


    print(f"\n✨ Organisation terminée ! {compteur} fichier(s) déplacé(s).")
        

organiser_fichier("MonDossier")
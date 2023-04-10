import os  

# Pfad zum genutzten Verzeichnis 

path = "C:\\Users\\becke\\OfficePythonProgramming\\Projects\\3_Task"

# Name des neuen Ordners

dir_name = "business_structure"

try:

    # Neuen Ordner erstellen 
    os.mkdir(os.path.join(path, dir_name))     
    print("Ordner erstellt:", os.path.join(path, dir_name))

    os.mkdir(os.path.join(path, dir_name, "it_data")) # Unterordner erstellen   
    os.mkdir(os.path.join(path, dir_name, "documentation")) # Unterordner erstellen     
    os.mkdir(os.path.join(path, dir_name, "image")) # Unterordner erstellen     
    os.mkdir(os.path.join(path, dir_name, "mymodule")) # Unterordner erstellen     
    os.mkdir(os.path.join(path, dir_name, "src")) # Unterordner erstellen

except FileExistsError:     
    print("Der Ordner", os.path.join(path, dir_name), "existiert bereits.") # Fehlermeldung, falls Ordner bereits existiert
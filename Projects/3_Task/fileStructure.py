''''
Code is used to create a folder structure for the project 'business_structure'.
'''

import os  

# path to the folder where the new folder will be created
path = "C:\\Users\\becke\\OfficePythonProgramming\\Projects\\3_Task"

# name of the new folder
dir_name = "business_structure"

# try to create the new folder -> if it already exists, print an error message
try:
    
    os.mkdir(os.path.join(path, dir_name))                  # create the new folder     
    print("Folder create:", os.path.join(path, dir_name))   # success message

    os.mkdir(os.path.join(path, dir_name, "it_data"))       # create subfolder -> 'it_data'   
    os.mkdir(os.path.join(path, dir_name, "documentation")) # create subfolder -> 'documentation'
    os.mkdir(os.path.join(path, dir_name, "images"))        # create subfolder -> 'images'
    os.mkdir(os.path.join(path, dir_name, "mymodule"))      # create subfolder -> 'mymodule'
    os.mkdir(os.path.join(path, dir_name, "src"))           # create subfolder -> 'src'

except FileExistsError:     
    print("Folder", os.path.join(path, dir_name), "already exists.") # error message
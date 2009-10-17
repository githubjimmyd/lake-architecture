#Lake make_project.py

#so far, just creates a local folder space

import os



def create_project(project_name):
    #check if a project by that name exists
    currentpath = os.getcwd()
    for things in os.listdir(currentpath):
        if things == project_name:
            return print("That project name is already in use")
        
    #create the project space
    os.mkdir(os.path.join(currentpath,project_name))#should be try
    print("Project with name", project_name, "created successfully")
            

#Lake make_project.py

#so far, just creates a local folder space

import os



def create_project(project_name):
    #check if a project by that name exists
    currentpath = os.getcwd()
    projects = os.path.join(currentpath,"projects")
    for things in os.listdir(projects):
        if things == project_name:
            return print("That project name is already in use")
        
    #create the project space
    os.mkdir(os.path.join(projects,("prj_"+project_name)))#should be in a try
    print("Project with name", project_name, "created successfully")
            

def get_project_path_by_name(project_name):
    #prj_<project> directories
    current_path = os.getcwd()
    projects = os.path.join(current_path, "projects")
    for things in os.listdir(projects):
        if things[4:] == project_name:
            if os.path.isdir(os.path.join(projects,things)):
                return os.path.join(projects,things)

    return print("No such project")
            
def is_project(project_name):
    current_path = os.getcwd()
    projects = os.path.join(current_path, "projects")
    for things in os.listdir(projects):
        if things[4:] == project_name:
            if os.path.isdir(os.path.join(projects,things)):
                return True
    return False


def list_projects():
    current_path = os.getcwd()
    projects = os.path.join(current_path,"projects")
    prj_count = 0
    for things in os.listdir(projects):#search everything in the projects folder
        if os.path.isdir(os.path.join(projects,things)):#then it's a folder, not a file
            if (things[0:4] == "prj_"): #prj_ naming scheme, to deliniate projects
                prj_count+=1
                print(things[4:])#print the project without "prj_" in front, user doesn't need to know abuot naming scheme
    if not prj_count >= 1:
        print("No projects")

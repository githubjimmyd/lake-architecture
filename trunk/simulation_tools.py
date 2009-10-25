#simulation_tools

#everything is setup to run, but nothing is in an actual name space
import os


class lake_simulation():
    project_path = None

    def __init__(self, path):
        self.project_path = path
        #check to see if the project IS setup properly
        pass_check = False
        #no check yet
        #do check and pass
        pass_check = True

    def initialize_everything(self):
        path = self.project_path

        objects = []
        for things in os.listdir(path):
            if (things[0:4] == "obj_"): #know it's a object of some kind
                obj_name = things[4:]
                #use exec BUT naming scheme will be obj_<type>_<name> i.e. obj_basicAgent_fred
                #have to get the name at the end and exec it: exec <name> = lake_agent(...)

    def get_name_from_folder(self, folder):
        pass
        #x = last _ , then name = folder[x:]
        
            
    
    

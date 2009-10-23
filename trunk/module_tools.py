#module_tools.py
import os

def attach(what, where):
    #attach what module, to what object
    pass

def create_module(module_name):
    #modules and objects are in the inventory, that way users don't need to do two commands.
    current_path = os.getcwd()
    inventory = os.path.join(current_path, "inventory")

    #check if the module (name) already exists
    for things in os.listdir(inventory):
        if things[4:] == module_name:
            return print("Module with name", module_name, "already exists.")
        else:
            os.mkdir(os.path.join(inventory,("mod_"+module_name)))#mod_ naming scheme
            print("Module with name", module_name, "created successfully")

    
    ####!!!!!!!! should put the module in the project space, not inventory!

def get_modules_list_names():
    modules = []
    current_path = os.getcwd()
    inventory = os.path.join(current_path,"inventory")
    for things in os.listdir(inventory):
        if os.path.isdir(os.path.join(inventory,things)):
            if(things[0:4] == "mod_"):
                modules.append(things[4:])
    return modules
    

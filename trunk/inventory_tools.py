#inventory tools
def list_inventory():
    current_path = os.getcwd()
    inventory = os.path.join(current_path,"inventory")

    for things in os.listdir(inventory):#search everything in the inventory folder
        if os.path.isdir(os.path.join(inventory,things)):#then it's a folder, not a file
            if (things[0:4] == "obj_"): #obj_ naming scheme, to deliniate pre-made object templates
                print(things[4:])#print the obj_ without "obj_" in front, user doesn't need to know abuot naming scheme


def inventory_copy(inventory_object, newInstance):
    if parent.current_project == None:
        return print("Please enter project space or create new project")#redundant check

    print("copy...")

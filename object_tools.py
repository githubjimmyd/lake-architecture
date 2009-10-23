#object tools
import os

def create_object(anInventoryItem, aName):
    print("not built yet")
    


def get_objects_list_names():#returns a [] of inventory items for use by cmd prompt (string names, no obj_
    objects = []
    current_path = os.getcwd()
    inventory = os.path.join(current_path,"inventory")
    for things in os.listdir(inventory):
        if os.path.isdir(os.path.join(inventory,things)):
            if (things[0:4] == "obj_"):
                objects.append(things[4:])
    return objects



def check_for_object_in_inventory(aName):#check the inventory for an object by name (all stored by name)
    #fdoprint(aName, "aName")
    current_path = os.getcwd()
    inventory = os.path.join(current_path,"inventory")

    for things in os.listdir(inventory):
        #fdoprint(things[4:], "things : ", aName, "aName")
        if things[4:] == aName:
            return True
        else:
            pass
    return False
    
    


    

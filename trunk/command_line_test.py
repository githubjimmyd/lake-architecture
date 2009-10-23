#Lake Cognitive Architecture
#Dr. Jim Davies (jim@jimdavies.org)

######################################################
####           The Lake Command Interface          ###
######################################################

import cmd
import string, sys


from project_tools import *
from object_tools import *
from module_tools import *
from inventory_tools import *


class LakeCmdInterface(cmd.Cmd):
    current_project = None #path of current project
    current_project_name = None #name of current project (last thing in path)
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Welcome to the Lake Cognitive Architecture, type 'help' for basic instructions.")
        self.prompt = '>>> '

    def do_quit(self, arg):
        return True

    def do_enter(self, args):
        #use: enter <project_name>
        args = args.split()
        if len(args) > 2:
            return print("Too many arguments.  See 'help enter'")
        if len(args) == 0:
            return print("Too few arguments.  See 'help enter'")
        if is_project(args[0]):
            self.current_project = get_project_path_by_name(args[0])
            self.current_project_name = args[0]
            print("Now in project", self.current_project_name)
        else:
            return print("No such project.  Type 'projects' for a list of your projects.")

    def help_enter(self):
        print("syntax: enter <project>")
        print("-- enter a project space.")

    def do_inventory(self, args):
        #all objects are really <obj_objectName> folders.  i.e. <obj_basicAgent>
        inventory_objects = get_objects_list_names()
        modules = get_modules_list_names()
        
        
        
        #printing fancy.
        #replace me
        i = 0
        
        x = (len(inventory_objects) if (len(inventory_objects) >= len(modules)) else len(modules))
        while i < x:
            print("%22s %22s" %(inventory_objects[i],modules[i]))
            i += 1
         
    def help_inventory(self):
        print("syntax: inventory")
        print("Lists all pre-made template objects adopted by Lake")

    def do_projects(self, args):
        args = args.split()
        if len(args) > 1:
            print("Too many arguments.  See 'help projects'")
        list_projects()#from project_tools

    def help_projects(self):
        print("syntax: projects")
        print("-- Lists all your projects")
    

##    def onecmd(self, s):
##        print ('onecmd(%s)' % s)
##        return cmd.Cmd.onecmd(self, s)
##can use ^ if you want to interrupt the command.  Probably do that with the help system, making external helps
    
    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

    def do_create(self, args):
        args = args.split()
        #get rid of all the wrong syntax cases first.
        if len(args) == 0:
            return print("Not enough arguments. See 'help create'.")
        if not args[1] == "called":
            return print("Proper use: create", args[0], "called", args[2])
        if len(args) > 3:
            return print("Too many argument")
        #create <obj_> called <name>
        #create project called <name>

        ###project case###
        if args[0] == "project":
            create_project(args[2])
        elif args[0] == "module":
            create_module(args[2])
        
        elif check_for_object_in_inventory(args[0]): #check to see if there is a template in the inventory, True/False from object_tools
            if self.current_project == None:
                return print("Please enter project space or create new project")
            else:
                create_object(self.current_project, args[0])
        else:
            return print("Incorrect syntax.  See 'help create'")

            inventory_copy(args[0],args[2])   
            
        
        

    def help_create(self):
        print("syntax 1: create <object> called <name>")
        print("-- creates an instance of a template object from inventory.  See 'inventory' for inventory items.")
        print("syntax 2: create project called <name>")
        print("-- creates a new project space used to contain models and environments")


        

    def do_attach(self, args):
        #for attaching a module to another object
        args = args.split()
        

        
            



#
# try it out

lci = LakeCmdInterface()
lci.cmdloop()

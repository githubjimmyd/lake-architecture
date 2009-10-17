#Lake Cognitive Architecture
#Dr. Jim Davies (jim@jimdavies.org)

######################################################
####           The Lake Command Interface          ###
######################################################

import cmd
import string, sys


from project_tools import *
from inventory_tools import *

class LakeCmdInterface(cmd.Cmd):
    current_project = None
    current_project_name = None
    
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
            current_project = get_project_path_by_name(args[0])
            current_project_name = args[0]
            print("Now in project", current_project_name)
        else:
            return print("No such project.  Type 'projects' for a list of your projects.")

    def help_enter(self):
        print("syntax: enter <project>")
        print("-- enter a project space.")

    def do_inventory(self, args):
        #all objects are really <obj_objectName> folders.  i.e. <obj_basicAgent>
        list_inventory()#from inventory_tools
         
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
        if len(args) == 0:
            return print("Not enough arguments. See 'help create'.")
        if not args[1] == "called":
            return print("Proper use: create", args[0], "called <a name>")
        if len(args) > 3:
            return print("Too many argument")
        #create <obj_> called <name>
        #create project called <name>

        ###project case###
        if args[0] == "project":
            create_project(args[2])
        
        elif check_inventory(args[0]): #check to see if there is a template in the inventory, True/False from inventory_tools
            if self.current_project == None:
                return print("Please enter project space or create new project")
            else:
                print("In a project, now what?")

            inventory_copy(args[0],args[2])   
            
        
        

    def help_create(self):
        print("syntax 1: create <object> called <name>")
        print("-- creates an instance of a template object from inventory.")
        print("syntax 2: create project called <name>")
        print("-- creates a new project space used to contain models and environments")


        



        
            



#
# try it out

lci = LakeCmdInterface()
lci.cmdloop()

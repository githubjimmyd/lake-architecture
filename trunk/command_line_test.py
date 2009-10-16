#Lake Cognitive Architecture
#Dr. Jim Davies (jim@jimdavies.org)

######################################################
####           The Lake Command Interface          ###
######################################################

import cmd
import string, sys
import os

class LakeCmdInterface(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Welcome to the Lake Cognitive Architecture, type 'help' for basic instructions.")
        self.prompt = '>>> '

    def do_quit(self, arg):
        return True
    

    def do_inventory(self, *args):
        #args = [] of arguments
        #all objects are really <obj_objectName> folders.  i.e. <obj_basicAgent>
        currentpath = os.getcwd()
        inventory = currentpath + "\inventory"
        
        for things in os.listdir(inventory):
            if os.path.isdir(os.path.join(inventory,things)):
                #then it's a folder, not a file
                if (things[0:4] == "obj_"):
                    #then it begin's with obj_ and is an object
                    print(things[4:])#lists the objects
                
        

##    def onecmd(self, s):
##        print ('onecmd(%s)' % s)
##        return cmd.Cmd.onecmd(self, s)
##can use ^ if you want to interrupt the command.  Probably do that with the help system, making external helps
    
    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

    def do_create(self, *args):
        #args = [] of arguments
        #create <obj_> called <name>
        

    def help_create(self):
        print("")


        



        
            



#
# try it out

lci = LakeCmdInterface()
lci.cmdloop()

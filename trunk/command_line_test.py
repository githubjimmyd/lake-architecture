#Lake Cognitive Architecture
#Dr. Jim Davies (jim@jimdavies.org)

######################################################
####The lake environment in which all things happen###
######################################################

import cmd
import string, sys

class LakeCmdInterface(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        print("Welcome to the Lake Cognitive Architecture, type 'help' for basic instructions.")
        self.prompt = '>>> '

    def do_quit(self, arg):
        return True

    def do_inventory(self, *args):
        #args = [] of arguments
        

##    def onecmd(self, s):
##        print ('onecmd(%s)' % s)
##        return cmd.Cmd.onecmd(self, s)
##can use ^ if you want to interrupt the command.  Probably do that with the help system, making external helps
    
    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

    def do_create(self, arg):
        if arg == "":
            self.help_create()
        

    def help_create(self):
        print("")


        



        
            



#
# try it out

lci = LakeCmdInterface()
lci.cmdloop()

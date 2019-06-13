"""
List the files in the current working directory.

@author Foo Barstein
@date 13 June 2019
"""

"""
Get a list of all the files in a given directory.
@arg directory The directory whose files to return
@return The list of files in this directory
"""
def get_list_of_files(directory):
    
    #get a list of the files in the current working directory
    file_list = os.listdir(directory)

    # return this list of files    
    return file_list

"""
Print out each of the files in a list of files
@arg list_of_files The list of files
"""
def print_list_of_files(list_of_files):
    
    #print out that list of files in this folder
    print("We have a list of all the files in the current working directory:")
    print(list_of_files)
    print() # line break
    
    print("Here is a nicer listing of all these files:")
    
    #loop through each filename in the list
    for filename in list_of_files:
        #print out each filename 
        print("\t-{}".format(filename) )
    

# import the os module
import os

"""
The main logic of the program.
"""
def main():
    #get the current working directory (by default the folder where this program is saved)
    cwd = os.getcwd()
    
    # get the list of files in this directory
    files = get_list_of_files(cwd)
    
    # print them out
    print_list_of_files(files)

# run the program
main()
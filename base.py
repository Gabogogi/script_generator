import sys
import re


def py_script_maker(script_name):
    """Generates python file with shebang line
       script_name (str): name of python script you wish to create
    """
    if script_name.endswith('.py'):
        pass
    else:
        script_name = script_name + '.py'

    with open(script_name, 'w') as file:
        file.write('#!/usr/bin/env python3\n')
        print(script_name + ' created')


def shell_script_maker(script_name):
    """Generates bash script with shebang line
    script_name (str): name of bash script you wish to create
    """
    with open(script_name, 'w') as file:
        file.write('#!/usr/bin/env bash\n')
        print(script_name + ' created')
    
   
def my_help():
    print("This file generates a python or bash script with shebang line\n")
    print("Python script: <this file> -p <name of output file>")
    print("Bash script: <this file> -b <name of output file>")


def flag_checker(flag):
    '''Enforces -p or -b as second argument'''
    flags = ['-p', '-b']
    if flag not in flags:
        sys.exit('Invalid flag. Provide -p or -b')
    else:
        return flag


def is_valid_name(name):
    '''No leading hyphens or special characters'''
    if name.startswith('-'):
        sys.exit("leading hyphen not allowed")
    pattern = r'^[a-zA-Z0-9_-]+$'
    if re.match(pattern, name):
        return name
    else:
        sys.exit("No special characters allowed")

def main():
    if len(sys.argv) == 1:
        sys.exit("No args passed. See '<base.py> Help' for options")
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'Help':
            my_help()
            sys.exit()
        else:
            sys.exit("Provide output file name. See '<base.py> Help' for option")
    elif len(sys.argv) == 3:
        pass
    else:
        sys.exit("Too many arguments. See '<base.py> Help' for options")

    for i, arg in enumerate(sys.argv):
        print(i, sys.argv[i])

    if flag_checker(sys.argv[1]) == '-p':
        py_script_maker(is_valid_name(sys.argv[2]))
    else:
        shell_script_maker(is_valid_name(sys.argv[2]))



if __name__ == "__main__":
    main()

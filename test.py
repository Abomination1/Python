from pathlib import Path
import os
import os.path
import shutil
import pip


path = Path('./')

def main():
    d = os.getcwd() #Gets the current working directory
    print(d)
    os.chdir('github'gitr)
    d = os.getcwd() #Gets the current working directory
    print(d)
    f = open("requre.txt ", "r")
    print(d)
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    f.close
     #or, readlines reads the individual line into a list
     #fl =f.readlines()
     #for x in fl:
     #print x


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


if __name__== "__main__":
  main()

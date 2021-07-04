from os import walk
import pathlib

def runShell():
    while True:
        print("--Shell Home--")
        cmd = None
        passed = False
        possibleCmds = ['LIST','ADD','HELP','EXIT']
        while passed == False:
            cmd = input('The possible commands are ' + ', '.join(possibleCmds) + ": ")
            if cmd in possibleCmds:
                passed = True
            else:
                print('invalid input')

        if cmd == 'LIST':
            listDirectory()
        elif cmd == 'ADD':
            addNumbers()
        elif cmd == 'HELP':
            showHelp()
        else:
            return

def listDirectory():
    print("--Contents of current directory--")
    mypath = pathlib.Path().absolute()
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break
    for name in f:
        print(str(name))

def addNumbers():
    print("--Add numbers--")
    number1 = None
    passed1 = False
    while not passed1:
        try:
            number1 = int(input("enter the first number to add: "))
            passed1 = True
        except:
            passed1 = False

    number2 = None
    passed2 = False
    while not passed2:
        try:
            number2 = int(input("enter the second number to add: "))
            passed2 = True
        except:
            passed2 = False

    print("added result = " + str(number1 + number2))

def showHelp():
    print('YOU GET NO HELP!')

runShell()

#!/usr/bin/python3

import core
import maleditor
import gmailemail
import os
import sys

green = core.lgreen
yellow = core.yellow
purple = core.lpurple
red = core.lred
blue = core.lblue
cyan = core.lcyan
rr = core.rr
bold = core.bold
ul = core.ul
line = purple + bold + "--------------------------------------------------------------------------------------" + rr
toolVersion = 0  # get tool version from update.py not in main.py


def get_install_location():
    # allows for python to find installation folder
    loc = ""
    try:
        file = open(os.path.join(sys.path[0], "location.txt"), "r")
        loc = file.read()
        file.close()
    except FileNotFoundError:
        print(red + "[!] Error, location.txt is not located" + rr)
    return loc


def clear():
    for i in range(4):
        os.system("clear")


def options():
    global toolVersion
    if toolVersion == 0:
        toolVersion = "Unable to determine version number"
    print("" + purple + bold + "Tool Version: " + rr + str(toolVersion) + "\n")
    print(" " + white + ul + "Please Select From The Menu" + rr + "\n")

    print("\t{:10s} MalEditor".format("[" + purple + "1" + rr + "]"))
    print("\t{:10s} Send Malware With Email w/ Gmail".format("[" + purple + "2" + rr + "]"))
    print("\t{:10s} Reloads The Screen".format("[" + purple + "r" + rr + "]"))
    print()  # prints empty line to separate options from functions
    # print("\t{:10s} Check for Updates(Coming soon)".format("[" + purple + "c" + rr + "]"))
    print("\t{:10s} Uninstall Malfactory".format("[" + red + "u" + rr + "]"))
    print("\t{:10s} Report bugs/glitches ".format("[" + purple + "z" + rr + "]"))
    print("\t{:10s} Exit ".format("[" + purple + "99" + rr + "]"))
    print()  # empty line for the looks


def helpMenu():
    print("Help menu")
    print("[1] MalEditor -is used for making malware using \"Malscript\", you can write and save your scripts here")
    print("[2] Reloads The Screen -is used for refreshing the screen")
    # etc , add more stuff here


def main():  # takes in user input and check for commands
    try:
        while True:
            command = input(red + "Mal" + purple + "Factory" + rr + " > ")
            command = command.lower()
            if command == "1":
                maleditor.startup()
            elif command == "2":
                gmailemail.startup()
            elif command == "r":
                clear()
                startup()
            elif command == "99" or command == "exit" or command == "quit":
                core.quit()
            elif command == "help":
                helpMenu()
            elif command == "z":
                print(
                    blue + "Please submit any bugs/issues/glitches at this link :\n" + ul + bold + "https://github.com/asian-code/malfactory/issues" + rr)
            elif command == "u":
                dontgo = input(red + bold + "[!] Are you sure you want to UNINSTALL Malfactory? (y/n):" + rr)
                dontgo = dontgo.lower()
                if dontgo == "y":
                    loc = get_install_location()
                    uninstall_loc = loc + "/uninstaller"
                    print(blue + "[+] Checking for uninstaller in " + rr + uninstall_loc)

                    sys.path.append(loc)
                    try:
                        import uninstaller
                    except ImportError:
                        print(red + "[!] Error trying to uninstall" + rr)

            else:
                print(rr + red + "\nSorry, " + command + " is not a command.\n")
    except KeyboardInterrupt:
        core.quit()
    except Exception:
        print(
            rr + "\n[" + red + "+" + rr + "] Error: something went wrong \n")  # Need general error message since this try is the whole program instead of a specific block of code
        raise


def startup():  # display logo and options
    os.system("resize -s 50 86")
    clear()
    print(line)
    core.randomlogo()
    print(line + "\n")
    core.textlogo()
    print(green + "[+] Checking for updates... " + rr)

    # testing code{

    loc = get_install_location()
    # if loc != "":
    updater_loc = loc + "/update"

    sys.path.append(loc)
    try:
        import update
        update.start_update()  # not force the update unless really outdated
        global toolVersion
        toolVersion = update.tool_version

    except ImportError:
        toolVersion = red + "[!] Error trying to update." + rr

    print(green + "[+] Checking for updater in " + rr + updater_loc + " | " + toolVersion)
        
    # } testing code

    options()

    main()

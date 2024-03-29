import sys

import config
import functions

functions.readProfiles()
functions.removeDuplicates()
config = config.init()


print("Welcome to the Cheater Tracker Written by Macky in Python\n")
print("Please Select: \n1)Add Profile\n2)Remove Profile\n3)List Profiles\n4)Check Bans for All\n5)Exit\n")

choice = None
if config[1] == True:
    choice = 4
else:
    choice = int(input())

if choice == 1 and config[3] == False:
    profile = input("Enter Profile URL to Add: ")
    
    if config[2] == True:
        try:
            prof = functions.getPermenantURL(profile) + '\n'
        except:
            print("Error adding selected profile.")
    else:
        prof = profile

    functions.addProfile(prof)

elif choice == 2 and config[4] == False:
    prof = input("\nEnter Profile URL to Remove: ")
    functions.removeProfile(prof)

elif choice == 3:
    functions.listProfiles()
    profileEntry = int(input("\n")) - 1
    
    x = int(input("\nPlease Select: \n1)Open Profile\n2)Check Ban Status\n"))

    if x == 1:
        functions.openProfile(functions.getProfileEntry(profileEntry))
    elif x == 2:
        print("\n")
        functions.checkBan(functions.getProfileEntry(profileEntry))
    else:
        print("Invalid Input. . .")

elif choice == 4:
    print('\n')
    for x in range(len(functions.profiles)):
        try:
            profileEntryx = str(functions.getProfileEntry(x))
        except:
            print("Profile could not be resolved.")
            continue
        alias = functions.getAlias(profileEntryx)
        try:
            print(alias)
        except:
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            alias = alias.translate(non_bmp_map)
            print(alias)
        if functions.checkBan(profileEntryx) and config[0] == True: #If the setting for this is true in the config
            functions.removeProfile(profileEntryx)
        print('\n')

elif choice == 5:
    exit(0)

elif choice == 1 and config[3] == True:
    print("Enter 'x' to Stop\n")
    while True:
        profile = input("")

        if profile == 'x':
            break

        if config[2] == True:
            try:
                prof = functions.getPermenantURL(profile) + '\n'
            except:
                print("Error converting profile to permanent URL, storing regular URL.")
                prof = profile
        else:
            prof = profile

        functions.addProfile(prof)

elif choice == 2 and config[4] == True:
    print("Enter 'x' to Stop\n")
    while True:
        prof = input("Enter Profile URL to Remove: ")
        
        if prof == 'x':
            break

        functions.removeProfile(prof)

else:
    print("Invalid Input. . . ")
    exit(-1)


functions.saveProfiles()

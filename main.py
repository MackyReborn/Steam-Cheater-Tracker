import functions

functions.readProfiles()

print("Welcome to the Cheater Tracker Written by Macky in Python\n")
print("Please Select: \n1)Add Profile\n2)Remove Profile\n3)List Profiles\n4)Exit\n")
choice = int(input())

if choice == 1:
    profile = input("Enter Profile URL to Add: ")
    functions.addProfile(profile)

elif choice == 2:
    profile = input("Enter Profile URL to Remove: ")
    functions.removeProfile(profile)

elif choice == 3:
    functions.listProfiles()
    profileEntry = int(input("\n"))
    
    x = int(input("Please Select: \n1)Open Profile\n2)Check Ban Status\n"))

    if x == 1:
        functions.openProfile(functions.getProfileEntry(profileEntry))
    elif x == 2:
        functions.checkBan(functions.getProfileEntry(profileEntry))
    else:
        print("Invalid Input. . .")

elif choice == 4:
    exit(0)

else:
    print("Invalid Input. . . ")
    exit(-1)


functions.saveProfiles()

'''
checkBan("https://steamcommunity.com/id/macky_")
checkBan("https://steamcommunity.com/id/willashley/")
checkBan("https://steamcommunity.com/profiles/76561198044592759")
'''
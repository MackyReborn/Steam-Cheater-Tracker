import webbrowser
import os
import time
import string
import array
import requests
from bs4 import BeautifulSoup

profiles = []

def readProfiles():
    theFile = open("profiles.txt", "r")

    for entry in theFile:
        if entry != "\n":
            profiles.append(entry)
    
    theFile.close()


def openProfile(url):
    webbrowser.open(url)


def listProfiles():
    for entry in profiles:
        print(entry)


def addProfile(profile):
    profiles.append(profile)


def removeProfile(profile):
    profiles.remove(profile)


def saveProfiles():
    theFile = open("profiles.txt", "w")

    for entry in profiles:
        theFile.write(entry + '\n')
    
    theFile.close()


def getProfileEntry(index):
    return profiles[index]


def checkBan(url):
    y = url.replace("\n", "")
    res = requests.get(y)
    steam_page = res.content
    soup = BeautifulSoup(steam_page, 'html.parser')
    webText = soup.find_all(text=True)

    output = ''
    blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
    ]

    for t in webText:
	    if t.parent.name not in blacklist:
	    	output += '{} '.format(t)

    if output.find("game ban on record") > -1:
        print("Account is Overwatch Banned")
    elif output.find("VAC ban on record") > -1:
        print("Account is VAC Banned")
    else:
        print("Account is not Banned")
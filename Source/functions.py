import webbrowser
import os
import sys
import time
import string
import array
import requests
from bs4 import BeautifulSoup

profiles = []

def getAlias(url):
    y = url.replace("\n", "")
    res = requests.get(y)
    steam_page = res.content
    soup = BeautifulSoup(steam_page, 'html.parser')
    persona = soup.find('span', class_='actual_persona_name')

    stringpersona = str(persona)

    alias = stringpersona.replace('<span class="actual_persona_name">', '')
    alias = alias.replace('</span>', '')

    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    alias = alias.translate(non_bmp_map)

    return alias


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
        entry.replace('\n', '')
        print(entry, getAlias(entry), '\n')


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
import array
import json
import os
import string
import sys
import time
import webbrowser

import requests
from bs4 import BeautifulSoup

profiles = []

def readSettings():
    input_string = open("settings.json", "r")
    return json.load(input_string)


def getAlias(url):
    y = url.replace("\n", "")
    res = requests.get(y)
    steam_page = res.content
    soup = BeautifulSoup(steam_page, 'html.parser')
    persona = soup.find('span', class_='actual_persona_name')

    stringpersona = str(persona)

    alias = stringpersona.replace('<span class="actual_persona_name">', '')
    alias = alias.replace('</span>', '')

    return alias

'''
def convertUrls():
    resultantUrls = []
    for profile in profiles:
        if profile == '\n':
            continue
        permUrl = getPermenantURL(profile)
        profiles.remove(profile)
        resultantUrls.append(permUrl)

    for url in resultantUrls:
        profiles.append(url)
'''

def getPermenantURL(url):
    y = url.replace('\n', '')
    x = 'https://steamid.xyz/' + y
    html_page = requests.get(x)
    page = html_page.content
    soup = BeautifulSoup(page, 'html.parser')
    tlink = soup.select('input[type="text"]')[6]
    plink = tlink.get('value')

    return plink



def checkDuplicates(profile):
    if profiles.count(profile) > 1:
        return True
    else:
        return False


def removeDuplicates():
    try:
        for profile in profiles:
            if (checkDuplicates(profile) == True):
                profiles.remove(profile)
    except:
        print("Could not Parse Accounts List!")


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
    permUrl = getPermenantURL(profile)
    profiles.append(permUrl)


def removeProfile(prof):
    append = prof.find('\n')
    if append == -1:
        profile = prof + '\n'
    else:
        profile = prof
    try:
        print("Removing ", profile)
        profiles.remove(profile)
        print("\nProfile Removed.\n")
    except:
        print("Error Removing Profile. ")


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
        return True
    elif output.find("VAC ban on record") > -1:
        print("Account is VAC Banned")
        return True
    else:
        print("Account is not Banned")
        return False

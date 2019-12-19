import webbrowser
import os
import sys
import json
import time
import string
import array
import valve
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


def addUser(url):
    return True

'''
def getPermenantURL(url):
    if url.find('profiles') > -1:
        return url
    y = url.replace('\n', '')
    rurl = "https://steamid.xyz/" + y

    res = requests.get(rurl)
    page = res.content
    soup = BeautifulSoup(page, 'html.parser')

    iurl = soup.findAll('input')
'''

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


def removeProfile(prof):
    profile = prof + '\n'
    try:
        profiles.remove(profile)
    except:
        print("Error Removing Selected Profile. ")


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
import json
import functions

def init():
    settings = functions.readSettings()
    autodelete = settings["autodelete"]
    autorun = settings["autorun"]

    return [autodelete, autorun]
import json
import functions

def init():
    settings = functions.readSettings()
    autodelete = settings["autodelete"]
    autorun = settings["autorun"]
    autoConvertUrls = settings["autoConvertUrls"]
    bulkAdd = settings["bulkAdd"]
    bulkRemove = settings["bulkRemove"]

    return [autodelete, autorun, autoConvertUrls, bulkAdd, bulkRemove]

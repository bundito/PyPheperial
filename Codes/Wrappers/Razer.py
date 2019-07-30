import requests
import json

global doneInit # for checking if init is done.
global debug

debug = False
doneInit = False

def debugON():
    global debug
    debug = True

def debugOFF():
    global debug
    debug = False

def PostReq(URL , jsondata):
    global debug

    Response = requests.post(url = URL , json = jsondata)
    jsonResult = json.loads(str(Response.text))

    if debug:
        print(Response.text)

    return jsonResult

def KeepAlive():
    Response = requests.put("http://localhost:54235/razer/chromasdk/heartbeat" , "")
    print(Response.text)

def init():
    global doneInit
    url = "http://localhost:54235/razer/chromasdk/"
    data = {
        "title": 'PyPheperial',
        "description":  'A Wrapper for PyPheperial',
        "author": {
            "name":'Gooday2die',
            "contact": 'github.com/gooday2die/pypheperial'
        },
        "device_supported": ['keyboard', 'mouse', 'mousepad'],
        "category": 'application'
    }

    jsonResult = PostReq(url , data)

    if jsonResult['sessionid'] != None :
        print("[INFO] Razer SDK Initialization Success")
        print("[INFO] Razer SDK Session ID : " + str(jsonResult['sessionid']))
        doneInit = True

    else:
        print("[ERROR] Razer SDK Initialization Failed")
        print("Check If Razer SDK is enabled")



def MouseSTATICOn():
    url = "http://localhost:54235/razer/chromasdk/mouse"


    data = {
    "effect": "CHROMA_STATIC",
    "param": {
        "color": 255
        },
    }

    PostReq(url , data)



def MouseLEDOff():

    url = "http://localhost:54235/razer/chromasdk/mouse"

    data = {
    "effect": "CHROMA_NONE"
    }

    PostReq(url , data)


debugON()
init()
MouseLEDOff()
MouseSTATICOn()
KeepAlive()
init()

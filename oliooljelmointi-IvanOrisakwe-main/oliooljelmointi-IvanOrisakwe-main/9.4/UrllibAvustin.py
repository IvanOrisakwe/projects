# Tuomme urlopen metodin urllib API:sta
from urllib.request import urlopen

def UrllibGet(websivu):
    response = None

    #kokeillaan koodia virhetilanteiden varalta
    try:
        response = urlopen(websivu)
    #Näytetää virheilmoitus jos sellainen ilmenee
    except Exception as ex:
        print(ex)
    else:
        body = response.read()
    finally:
        if response is not None:
            response.close()
    return body

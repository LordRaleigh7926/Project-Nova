from urllib import request

def internet_status():
    try:
        request.urlopen('http://google.com', timeout=2)
        print("Internet Present")
        return True
    except request.URLError as err:
        print("Internet Not Present")
        return False

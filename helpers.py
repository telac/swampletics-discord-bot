from configparser import ConfigParser
import requests

LATEST = "watch?v=TJUVf_F3QCk"

def fetch_latest():
    url = "https://www.youtube.com/channel/UCs-w7E2HZWwXmjt9RTvBB_A/videos"
    r = requests.get(url)
    data = str(r.content).split(' ')
    videos = [line for line in data if 'watch?' in line]
    return videos[0].strip('"')

def get_stats():
    url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=swampletics"
    r = requests.get(url)
    return r.text.split("\n")

def is_new_video():
    latest = fetch_latest()
    if LATEST in latest:
        return False
    with open("latest", "w") as _latest:
        _latest.write(latest)

    return True

def config(section, filename='conf.ini'):
    parser = ConfigParser()
    parser.read(filename)
    conf = {}
    if parser.has_section(section):
        parameters = parser.items(section)
        for param in parameters:
            conf[param[0]] = param[1]
    else:
        raise Exception("config not found!")
    return conf

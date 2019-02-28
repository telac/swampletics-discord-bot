from configparser import ConfigParser
import requests

HUNTER_LEVEL_IS_2 = "watch?v=R-0y6ikXAss"

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
    if HUNTER_LEVEL_IS_2 in latest:
        return False
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

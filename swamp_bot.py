#!/usr/bin/env python
from swamp_client import SwampClient
from time import sleep
from datetime import datetime, timedelta
from helpers import *


BOT_PREFIX = ["!", "?"]
WEDNESDAY = 2
conf = config('swampletics')
client = SwampClient(command_prefix=BOT_PREFIX, channel=conf['channel'])


@client.command(name="hunter")
async def hunter():
    """
    get swampletics hunter level
    """
    hunter_level = str(get_stats()[22].split(",")[1])
    await client.say('swampletics hunter level is currently {}'.format(hunter_level))

@client.command(name="swampletics")
async def swampletics():
    """
    checks for new video
    """
    msg = 'no new video'
    if is_new_video():
        msg = 'N E W V I D E O \n'
        msg += fetch_latest().replace('href="', 'https://youtube.com')
    await client.say(msg)

@client.command(name="latest")
async def latest():
    """
    posts link to the latest S W A M P L E T I C S video
    """
    msg = fetch_latest().replace('href="', 'https://youtube.com')
    await client.say(msg)

@client.command(name="dopamine")
async def dopamine():
    """
    posts pure dopamine to discord
    """
    msg = "https://vignette.wikia.nocookie.net/2007scape/images/2/2d/Lamp_detail.png/revision/latest?cb=20160707155240"
    await client.say(msg)

@client.command(name="when")
async def when():
    """
    days to next swampletics video
    """
    dt = (WEDNESDAY - datetime.today().weekday()) % 7
    await client.say("{} days until next ＳＷＡＭＰＬＥＴＩＣＳ video".format(dt))

@client.event
async def on_message(message):
    msg = None
    words = message.content.strip("?").split(" ")
    if message.author == client.user:
        return
    if "day" in words and "swampletics" in words:
        today = datetime.today().weekday()
        if today == WEDNESDAY:
            msg = 'ITS SWAMPLETICS DAY'.format(message)
    if msg:
        await client.send_message(message.channel, msg)

    await client.process_commands(message)

if __name__ == "__main__":
    client.run(conf['token'])

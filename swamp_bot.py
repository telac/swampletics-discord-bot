#!/usr/bin/env python
from swamp_client import SwampClient
from time import sleep
from datetime import datetime
from helpers import *


BOT_PREFIX = ["!", "?"]
client = SwampClient(command_prefix=BOT_PREFIX)

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

@client.event
async def on_message(message):
    msg = None
    words = message.content.strip("?").split(" ")
    if message.author == client.user:
        return
    if "day" in words and "swampletics" in words:
        today = datetime.today().weekday()
        if today == 2:
            msg = 'ITS SWAMPLETICS DAY'.format(message)
    if msg:
        await client.send_message(message.channel, msg)

    await client.process_commands(message)

if __name__ == "__main__":
    conf = config('swampletics')
    client.run(conf['token'])

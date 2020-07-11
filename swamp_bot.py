#!/usr/bin/env python
import discord
from discord.ext import commands
from time import sleep
from datetime import datetime, timedelta
from helpers import *
from random import choice

WEDNESDAY = 2
BOT_PREFIX = ["!", "?"]
conf = config('swampletics')
description = """
a very useful bot
"""
bot = commands.Bot(command_prefix=BOT_PREFIX, description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name="hunter")
async def hunter(ctx):
    """
    get swampletics hunter level
    """
    hunter_level = str(get_stats()[22].split(",")[1])
    await ctx.send('swampletics hunter level is currently {}'.format(hunter_level))

@bot.command(name="swampletics")
async def swampletics(ctx):
    """
    checks for new video
    """
    msg = 'no new video'
    if is_new_video():
        msg = 'N E W V I D E O \n'
        msg += fetch_latest().replace('href="', 'https://youtube.com')
    await ctx.send(msg)

@bot.command(name="latest")
async def latest(ctx):
    """
    posts link to the latest S W A M P L E T I C S video
    """
    msg = "https://www.youtube.com/" + fetch_latest()
    await ctx.send(msg)

@bot.command(name="dopamine")
async def dopamine(ctx):
    """
    posts pure dopamine to discord
    """
    msg = "https://vignette.wikia.nocookie.net/2007scape/images/2/2d/Lamp_detail.png/revision/latest?cb=20160707155240"
    await ctx.send(msg)

@bot.command(name="ez4ence")
async def ez4ence(ctx):
    """
    cs go stuff
    """
    msg = "go b but then go a"
    msg1 = "go a but then go b"
    await ctx.send(choice([msg, msg1]))


@bot.command(name="when")
async def when(ctx):
    """
    days to next swampletics video
    """
    dt = (WEDNESDAY - datetime.today().weekday()) % 7
    await ctx.send("{} days until next ＳＷＡＭＰＬＥＴＩＣＳ video (rip weekly videos)".format(dt))



if __name__ == "__main__":
    bot.run(conf['token'])

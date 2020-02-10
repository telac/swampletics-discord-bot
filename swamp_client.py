import discord
from helpers import *
import asyncio


WEDNESDAY = 2


class SwampClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(kwargs)
        self.bg_task = self.loop.create_task(self.check_for_new_video())
        self.channel = kwargs['channel']
        print(self.channel)
        self.broadcasted = False

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

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
            await message.channel.send(msg)

    async def check_for_new_video(self):
        await self.wait_until_ready()
        channel = self.get_channel(self.channel)
        while True:
            print("checking for new video")
            if is_new_video() and not self.broadcasted:
                await channel.send('NEW SWAMPLETICS VIDEO HAS BEEN RELEASED!!')
                latest = fetch_latest().replace('href="', 'https://youtube.com')
                await channel.send(channel, latest)
                self.broadcasted = True
            await asyncio.sleep(60)

if __name__ == "__main__":
    conf = config('swampletics')
    client = SwampClient(channel=conf['channel'])
    client.run(conf['token'])

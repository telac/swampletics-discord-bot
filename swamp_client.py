from discord.ext.commands import Bot
from helpers import *
import asyncio


class SwampClient(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.check_for_new_video())
        self.channel = kwargs['channel']

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        channel = self.get_channel(self.channel)


    async def check_for_new_video(self):
        await self.wait_until_ready()
        channel = self.get_channel(self.channel)
        while True:
            if is_new_video():
                await self.send_message(channel, 'NEW SWAMPLETICS VIDEO HAS BEEN RELEASED!!')
                latest = fetch_latest().replace('href="', 'https://youtube.com')
                await self.send_message(channel, latest)
            await asyncio.sleep(60)

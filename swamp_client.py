from discord.ext.commands import Bot
from helpers import *
import asyncio


class SwampClient(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.check_for_new_video())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def check_for_new_video(self):
        await self.wait_until_ready()
        channel = self.get_channel('377895315786825730')
        while True:
            print("checking for new videos")
            if is_new_video():
                await self.send_message(channel, 'NEW SWAMPLETICS VIDEO HAS BEEN RELEASED!!')
                latest = fetch_latest().replace('href="', 'https://youtube.com')
                await self.send_message(channel, latest)
            await asyncio.sleep(60)

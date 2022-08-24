import discord
from discord.ext import commands

from .commands import narf, test


class TTSBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

        self.add_command(test)
        self.add_command(narf)

    async def on_ready(self) -> None:
        print(f'{self.user.name} has connected to Discord!')

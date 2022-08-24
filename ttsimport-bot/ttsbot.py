import logging

import discord
from discord.ext import commands

from .commands import decks

_logger = logging.getLogger(__name__)


class TTSBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

        self.add_command(decks)

    async def on_ready(self) -> None:
        _logger.info(f'{self.user.name} has connected to Discord!')

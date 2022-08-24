import io
import logging

import discord
from discord.ui import Select
from fftcgtool import FFDecks, Language

_logger = logging.getLogger(__name__)


class DeckLangSelect(Select):
    def __init__(self, decks: FFDecks) -> None:
        super().__init__(
            placeholder="Select Deck Language",
            options=[
                discord.SelectOption(
                    label="English",
                    value="en",
                    emoji="🇬🇧",
                ),
                discord.SelectOption(
                    label="French",
                    value="fr",
                    emoji="🇫🇷",
                ),
                discord.SelectOption(
                    label="German",
                    value="de",
                    emoji="🇩🇪",
                ),
                discord.SelectOption(
                    label="Italian",
                    value="it",
                    emoji="🇮🇹",
                ),
                discord.SelectOption(
                    label="Japanese (tooltips only)",
                    value="ja",
                    emoji="🇯🇵",
                ),
                discord.SelectOption(
                    label="Spanish",
                    value="es",
                    emoji="🇪🇸",
                ),
            ],
        )

        self.__decks = decks

    @property
    def language(self) -> Language:
        return Language(self.values[0])

    async def callback(self, interaction: discord.Interaction) -> None:
        requester = f"{interaction.user.name}#{interaction.user.discriminator}"
        _logger.info(f"… {requester} picked {self.language}!")

        await interaction.message.edit(
            view=None,
        )

        msg_files = [
            discord.File(
                fp=io.BytesIO(bytes(
                    deck.get_json(self.language),
                    "utf-8",
                )),
                filename=deck.file_name,
                description=deck.name,
            ) for deck in self.__decks
        ]

        await interaction.response.send_message(
            content="Here are your deck files!",
            files=msg_files,
            ephemeral=True,
        )

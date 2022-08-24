import discord
from discord.ui import Select
from fftcgtool import Language


class DeckLangSelect(Select):
    def __init__(self) -> None:
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

    @property
    def language(self) -> Language:
        return Language(self.values[0])

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.message.edit(
            content=f"You chose {self.language}!",
            view=None,
        )

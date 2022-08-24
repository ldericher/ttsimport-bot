import io
import logging
import os

import discord
from discord.ext import commands
from fftcgtool import FFDecks, Language

_logger = logging.getLogger(__name__)


@commands.command()
async def test(ctx, *args) -> None:
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


@commands.command()
async def narf(ctx) -> None:
    myfile = io.BytesIO(b'{"unfug": "wert"}')
    await ctx.send(file=discord.File(fp=myfile, filename="grob.json"))


def to_language(arg: str) -> Language:
    return Language(arg)


@commands.command()
async def decks(
    ctx: commands.Context,
    language: to_language,
    *deck_ids: str
) -> None:

    MAX_DECKS = int(os.getenv("TTSBOT_MAX_DECKS", 10))
    requester = f"{ctx.author.name}#{ctx.author.discriminator}"
    san_ids = list(FFDecks.sanitized_ids(deck_ids))

    reply_content = f"Hi {ctx.author.mention}!\n\n"
    _logger.info(f"{requester} requested {len(san_ids)} decks.")

    if len(san_ids) > MAX_DECKS:
        san_ids = san_ids[:MAX_DECKS]
        reply_content += \
            f"To keep things sane, I only looked at {MAX_DECKS} " + \
            "of your deck IDs.\n"

        _logger.info(
            f"Truncated {requester}'s request to {MAX_DECKS} decks."
        )

    if (decks := FFDecks(san_ids)):
        reply_content += \
            "I found and imported the following decks for you:\n" + \
            "\n".join("• " + deck.name for deck in decks)

        msg_files = [
            discord.File(
                fp=io.BytesIO(bytes(
                    deck.get_json(language),
                    "utf-8",
                )),
                filename=deck.file_name,
                description=deck.name,
            ) for deck in decks
        ]

        _logger.info(f"Sending {len(decks)} decks to {requester}!")

    else:
        reply_content += \
            "Unfortunately, I didn't find any valid decks for your " + \
            "request :cry:"

        msg_files = []

    await ctx.send(
        content=reply_content,
        files=msg_files,
    )

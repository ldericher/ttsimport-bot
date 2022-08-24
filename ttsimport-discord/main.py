import io
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


@commands.command()
async def narf(ctx) -> None:
    myfile = io.BytesIO(b'{"unfug": "wert"}')
    await ctx.send(file=discord.File(fp=myfile, filename="grob.json"))


@commands.command()
async def test(ctx, *args) -> None:
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


def main() -> None:
    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready() -> None:
        print(f'{bot.user.name} has connected to Discord!')

    bot.add_command(narf)
    bot.add_command(test)

    bot.run(TOKEN)


if __name__ == "__main__":
    main()

import io

import discord
from discord.ext import commands


@commands.command()
async def test(ctx, *args) -> None:
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


@commands.command()
async def narf(ctx) -> None:
    myfile = io.BytesIO(b'{"unfug": "wert"}')
    await ctx.send(file=discord.File(fp=myfile, filename="grob.json"))

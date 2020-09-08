import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")

# Events


@commands.Cog.listener()
async def on_command_error(self, ctx, ex):
    print(ex)
    await ctx.send("```Please check with .help the usage of this command or talk to Big Boss#3024 about it.```")

# Commands

# Load Cog Command


@client.command()
async def load(ctx, extension):
    """Loads a category"""
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')


# Unload Cog Command


@client.command()
async def unload(ctx, extension):
    """Unloads a category"""
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')


@client.command()
async def reload(ctx, extension):
    """Reloads a category"""
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzQ0NTUzNDUzNzgyNjk1OTY2.Xzk5cA.t9EwQKbZVBrDFSe_yAsmAUGo2d0')

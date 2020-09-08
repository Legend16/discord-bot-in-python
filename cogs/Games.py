import discord
from discord.ext import commands

import random


class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("```Please check with .help the usage of this command or talk to Big Boss#3024 about it.```")

    @commands.command(brief="Plays a game of rock, paper, scissors with a bot")
    async def rps(self, ctx, your_choice):
        your_choice.lower()
        your_choice.replace(" ", "")

        ROCK = 'rock'
        PAPER = 'paper'
        SCISSORS = 'scissors'

        bot_choice_options = ['Rock', 'Paper', 'Scissors']

        if your_choice == ROCK:
            await ctx.send(random.choice(bot_choice_options))
        elif your_choice == PAPER:
            await ctx.send(random.choice(bot_choice_options))
        elif your_choice == SCISSORS:
            await ctx.send(random.choice(bot_choice_options))
        else:
            await ctx.send('Incorrect sign\nPlease Enter rock | paper | scissors')


def setup(client):
    client.add_cog(Games(client))

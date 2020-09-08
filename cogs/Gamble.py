import discord
from discord.ext import commands

import random


class Gamble(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Tosses a coin")
    async def coin(self, ctx):
        coin_landing_options = ['Heads', 'Tails']
        await ctx.send(random.choice(coin_landing_options))

    @commands.command(brief="Plays a game of roulette with a bot")
    async def roulette(self, ctx, *, colour):

        colour = colour.lower()
        colour = colour.replace(" ", "")

        red_numbers = ['32', '19', '21', '25', '34', '27', '36',
                       '30', '23', '5', '16', '1', '14', '9', '18', '7', '12', '3']

        black_numbers = ['15', '4', '2', '17', '6', '13', '11', '8',
                         '10', '24', '33', '20', '31', '22', '29', '28', '35', '26']

        green_numbers = ['0']

        all_numbers = ['32', '19', '21', '25', '34', '27', '36', '30', '23', '5', '16', '1', '14', '9', '18', '7', '12',
                       '3', '15', '4', '2', '17', '6', '13', '11', '8', '10', '24', '33', '20', '31', '22', '29', '28', '35', '26', '0']

        GREEN = 'green'
        BLACK = 'black'
        RED = 'red'

        if colour == GREEN:

            if random.choice(all_numbers) in green_numbers:
                await ctx.send('You Won!, you landed a green spot!')
            else:
                await ctx.send('You Lost!, you didn\'t land on a green spot!')

        elif colour == BLACK:

            if random.choice(all_numbers) in black_numbers:
                await ctx.send('You Won!, you landed a black spot!')
            else:
                await ctx.send('You Lost!, you didn\'t land on a black spot!')

        elif colour == RED:

            if random.choice(all_numbers) in red_numbers:
                await ctx.send('You Won!, you landed a red spot!')
            else:
                await ctx.send('You Lost!, you didn\'t land on a red spot!')


def setup(client):
    client.add_cog(Gamble(client))

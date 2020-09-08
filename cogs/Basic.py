import discord
from discord.ext import commands
import random


class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online!')

    # 8Ball command

    @commands.command(aliases=['8ball'], brief="Tells you a random yes/no answer to a question")
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain',
                     'It is decidedly so',
                     'Without a doubt',
                     'Yes - definitely',
                     'You may rely on it',
                     'As I see it, yes',
                     'Most likely',
                     'Outlook Good',
                     'Yes',
                     'Signs point to yes',
                     'Reply hazy, try again',
                     'Ask again later',
                     'Better not tell you now',
                     'Cannot predict now',
                     'Concentrate and ask again',
                     'Don\'t count on it',
                     'My reply is no',
                     'My sources say no',
                     'Outlook not so good',
                     'Very Doubtful']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    # clear command

    @commands.command(brief="clears an amount of messages specified")
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    # Ping Command

    @commands.command(brief="Tells you the ping you are getting")
    async def ping(self, ctx):
        await ctx.send(f'```Pong!\n{round(self.client.latency * 1000)} ms```')


def setup(client):
    client.add_cog(Basic(client))

import discord
from discord.ext import commands

import random

class Funny(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        memes = ['https://i.redd.it/vr4oaf4jtwl51.jpg',
                 'https://preview.redd.it/gv3kbixsjwl51.jpg?width=640&crop=smart&auto=webp&s=216531530876f0a84a5fac699266b3ee2e325d02',
                 'https://preview.redd.it/8d8c5tf90vl51.jpg?width=640&crop=smart&auto=webp&s=46c3a7639c6b8181aebb7206789c712e922c0bcd',
                 'https://preview.redd.it/epa3f2wyjvl51.jpg?width=640&crop=smart&auto=webp&s=7b16abfda9e13c7b329942c491b01dc0e72dd828',
                 'https://preview.redd.it/swaz24r6nwl51.jpg?width=640&crop=smart&auto=webp&s=67e2d9da291ef14cd8dffec5627175a60db54712',
                 'https://preview.redd.it/mag8936lftl51.png?width=640&crop=smart&auto=webp&s=f6fc74d777ff0e5a346343c053ba2caccc8b7658',
                 'https://preview.redd.it/y06f6gfg9xl51.jpg?width=640&crop=smart&auto=webp&s=13a470912ebe069a270d6f5dd546b1a272a9ef23']

        await ctx.send(random.choice(memes))


    @commands.command()
    async def joke(self, ctx):
        jokes = ['```Did you hear the joke about the dumpster?\nIt\'s a load of rubbish```',
                 '```Doctor, Doctor! I\'m shrinking!\nCalm Down, Be a little patient```',
                 '```They\'ve invented a new version of rugby where only people who wear glasses can play it...\nIt is a non-contact sport```',
                 '```My sewing instructor thinks that I’m the worst student she has ever seen in her life.\nShit, wrong thread.```',
                 '```So I stopped a woman from getting kidnapped today.\nIt took a lot of self control though```',
                 '```99% of the world is illiterate.The other half can\'t do math.```']

        await ctx.send(random.choice(jokes))



def setup(client):
    client.add_cog(Funny(client))

import discord
from discord.ext import commands

import datetime


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kick command

    @commands.command(brief="Kicks a user from the server - Admin only")
    @commands.is_owner()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member}')

    # Ban command

    @commands.command(brief="Bans a user from the server - Admin only")
    @commands.is_owner()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member}')

    # Unban command

    @commands.command(brief="Unbans a user from the server - Admin only")
    @commands.is_owner()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name = member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.menton}')
                return

    @commands.command(brief="Shows status of server - Admin only")
    @commands.is_owner()
    async def status(self, ctx):
        guild = ctx.guild

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)

        embed = discord.Embed(description="Server Status",
                              colour=discord.Colour.dark_purple())

        embed.set_thumbnail(
            url="https://www.pinclipart.com/picdir/big/354-3546720_his-2013-helpdesk-support-2x-references-icon-png.png")

        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(name="Custom Emojies",
                        value=emoji_string or "No emojis available", inline=False)

        embed.add_field(name="Server Name", value=guild.name, inline=False)

        embed.add_field(name="# Voice Channels", value=no_voice_channels)

        embed.add_field(name="# Text Channels", value=no_text_channels)

        embed.add_field(name="AFK Channel:", value=guild.afk_channel)
        embed.set_author(name=self.client.user.name)
        embed.add_field(name="Time: ", value=datetime.datetime.now())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))

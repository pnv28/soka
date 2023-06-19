import discord
from discord.ext import commands
import requests
from discord import Option
from discord.commands import SlashCommandGroup

color = discord.Color.from_rgb(255, 192, 203)


class Misc(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="serverinfo", description="Shows Information about the server")
    async def serverinfo(self, ctx):
        if ( ctx.author.id != 389306174119608321 ):  return await ctx.respond("CMD in Development")

        ownerID=ctx.guild.owner.id
        serverIcon = ctx.guild.icon
        memberCount=ctx.guild.member_count
        serverName = ctx.guild
        serverEmbed = discord.Embed(
            title=serverName,
            color=color
        )
        serverEmbed.set_thumbnail(url=serverIcon)
        serverEmbed.add_field(name="Member Count", value=memberCount, inline=True)
        serverEmbed.add_field(name="Owner", value=f"<@{ownerID}>")
        await ctx.respond(embed = serverEmbed)
        

def setup(bot):
    bot.add_cog(Misc(bot))
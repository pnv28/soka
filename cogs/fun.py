import discord
from discord import Option
from discord.ext import commands
from requests import get
import json

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    discord.slash_command(name="meme", description="Gets meme from internet")
    async def meme(self, ctx):
        get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content,)
        meme = discord.Embed(title=f"{data[title]}", Color = discord.Color.random()).set_image(url=f"{data[url]}")
        await ctx.respond(embed=meme)

def setup(bot):
    bot.add_cog(Fun(bot))
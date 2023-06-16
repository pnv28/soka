import discord
from discord import Option
from discord.ext import commands
from requests import get
import json
from googletrans import Translator, constants
from pprint import pprint
from discord import Option
import aiohttp
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="translate", description="Uses google translate")
    async def translate(self, ctx, text:Option(str, description="Text to translate")):
        translator = Translator()
        translation = translator.translate(text)
        await ctx.respond(translation.text)

    @discord.slash_command(name="meme", description="Sends a meme")
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                rand = random.randint(0, 20)
                memes = await r.json()
                memeEmbed = discord.Embed(
                    title=memes["data"]["children"][rand]["data"]["title"],
                    color = discord.Color.green()
                )
                memeEmbed.set_image(url=memes["data"]["children"][rand]["data"]["url"])
                memeEmbed.set_footer(text=f"Memes by r/memes | Requested by {ctx.author}")
                await ctx.send(embed = memeEmbed)
    
    @discord.slash_command(name="avatar", description="Sends the avatar of the user or specified user")
    async def avatar(self, ctx, user: Option(discord.Member, description="The user who's avatar to fetch", required = False)):
        avatarURL= ""
        if( user == None ):
            avatarURL=ctx.author.avatar
        else:
            avatarURL=user.avatar
        
        embed = discord.Embed(
            title = f"Avatar",
            color = discord.Color.green()
        )
        embed.set_image(url=avatarURL)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))
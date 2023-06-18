import discord
from discord import Option
from discord.ext import commands
from googletrans import Translator, constants
from discord import Option
import aiohttp
import random
import requests
import json
import nekos
import anime_images_api
anime = anime_images_api.Anime_Images()

color = discord.Color.from_rgb(255, 192, 203)
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.message_command(name="Translate message to English")
    async def translate(self, ctx, message: discord.Message):
        translator = Translator()
        translation = translator.translate(message.content)
        translateEmbed = discord.Embed(
            title="Translation",
            description=f"""
            From ({translation.src})
            ```{message.content}```

            To ({translation.dest})
            ```{translation.text}```
            
            """,
            color = color
        )
        await ctx.respond(embed = translateEmbed)

    @discord.slash_command(name="meme", description="Sends a meme")
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                rand = random.randint(0, 20)
                memes = await r.json()
                memeEmbed = discord.Embed(
                    title=memes["data"]["children"][rand]["data"]["title"],
                    color = color
                )
                memeEmbed.set_image(url=memes["data"]["children"][rand]["data"]["url"])
                memeEmbed.set_footer(text=f"Memes by r/memes | Requested by {ctx.author}")
                await ctx.respond(embed = memeEmbed)
    
    @discord.slash_command(name="avatar", description="Sends the avatar of the user or specified user")
    async def avatar(self, ctx, user: Option(discord.Member, description="The user who's avatar to fetch", required = False)):
        avatarURL= ""
        if( user == None ):
            avatarURL=ctx.author.avatar
        else:
            avatarURL=user.avatar
        
        embed = discord.Embed(
            title = f"Avatar",
            color = color
        )
        embed.set_image(url=avatarURL)
        await ctx.respond(embed = embed)
    
    @discord.slash_command(name="random_fact", description="Fetches a random fact")
    async def random_fact(self, ctx):
        fact = nekos.fact()
        await ctx.respond(fact)


def setup(bot):
    bot.add_cog(Fun(bot))
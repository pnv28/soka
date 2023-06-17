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
import requests
import json
import nekos


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="translate", description="Uses google translate")
    async def translate(self, ctx, text:Option(str, description="Text to translate")):
        translator = Translator()
        translation = translator.translate(text)
        translateEmbed = discord.Embed(
            title="Translation",
            description=f"""
            From ({translation.src})
            ```{text}```

            To ({translation.dest})
            ```{translation.text}```
            
            """,
            color = discord.Color.from_rgb(255, 192, 203)
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
                    color = discord.Color.from_rgb(255, 192, 203)
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
            color = discord.Color.from_rgb(255, 192, 203)
        )
        embed.set_image(url=avatarURL)
        await ctx.respond(embed = embed)
    
    @discord.slash_command(name="random_fact", description="Fetches a random fact")
    async def random_fact(self, ctx):
        fact = nekos.fact()
        await ctx.respond(fact)

    @discord.slash_command(name="anime_quote", description="Fetches a random quote")
    async def random_quotes(self, ctx):
        response = requests.get("https://kyoko.rei.my.id/api/quotes.php")
        quote = response.json()["apiResult"][0]["english"]
        author = response.json()["apiResult"][0]["character"]
        anime = response.json()["apiResult"][0]["anime"]
        quoteEmbed = discord.Embed(
            title=f"Quote from {anime}",
            description = f"```{quote} - {author}```",
            color = discord.Color.from_rgb(255, 192, 203)

        )
        await ctx.respond(embed = quoteEmbed)
    
    @discord.slash_command(name="kill", description="Fake Kills the specified user with Anime Gifs")
    async def kill(self, ctx, user: Option(discord.Member, description="The user to fake kill")):
        response = requests.get("https://kyoko.rei.my.id/api/kill.php")
        gif = response.json()["apiResult"]["url"][0]
        killEmbed = discord.Embed(
            title= f"{ctx.author.mention} killed {user.mention}",
            color = discord.Color.from_rgb(255, 192, 203)
        )
        killEmbed.set_image(url=gif)
        await ctx.respond(gif)
        


def setup(bot):
    bot.add_cog(Fun(bot))
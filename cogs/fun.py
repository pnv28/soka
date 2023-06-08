import discord
from discord import Option
from discord.ext import commands
from requests import get
import json
from googletrans import Translator, constants
from pprint import pprint
from discord import Option

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="translate", description="Uses google translate")
    async def translate(self, ctx, text:Option(str, description="Text to translate")):
        translator = Translator()
        translation = translator.translate(text)
        await ctx.respond(translation.text)


def setup(bot):
    bot.add_cog(Fun(bot))
import discord
from discord import Option
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name= "join", description= "Connects to the VC the user is in")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.respond("You have to be in a Voice Channel for me to join")
            return

        channel = ctx.author.voice.channel
        voice_channel = await channel.connect()
        await ctx.respond(f"The bot has joined <#{channel.id}>")

    @discord.slash_command(name= "leave", description="Leaves the voice channel the bot is in")
    async def leave(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.respond("I have left the voice channel")
            return
        else:
            await ctx.respond("I am not in a Voice channel")



def setup(bot):
    bot.add_cog(Music(bot))
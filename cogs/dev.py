import discord
from discord.ext import commands

class Dev(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name= "hello", description="Returns hey")
    async def hello(self, ctx):
        await ctx.respond("Hey")

def setup(bot):
    bot.add_cog(Dev(bot))
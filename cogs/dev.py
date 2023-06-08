import discord
from discord.ext import commands

class Dev(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name= "ping", description= "Responds with Pong!")
    async def ping(self, ctx):
        await ctx.respond("Pong!")

    @discord.slash_command(name= "hello", description="Returns hey")
    async def hello(self, ctx):
        await ctx.respond("Hey")

    @discord.slash_command(name="rr", description="rickrolls pika")
    async def rr(self, ctx):
        if(ctx.author.id != 389306174119608321):
            await ctx.respond("Only Pnv28 can use this command")
            return
        await ctx.respond("<@696740455789887599> Never goona give you up, never gonna let you down. Never goona turn around and desert you")
    @discord.slash_command(name="pat", description="Only the proper person knows")
    async def pat(self, ctx):
        if ctx.author.id == 696740455789887599:
            await ctx.respond("https://media.discordapp.net/attachments/777542650772324383/1115655363895758848/pika_pat.gif")
            return
        elif ctx.author.id == 389306174119608321:
            await ctx.respond("https://media.discordapp.net/attachments/1079761116093227062/1115306933151342662/Untitled_design.gif")
            return
        else:
            await ctx.respond("You do not have proper perms to run this command MAFKA")

    @discord.slash_command(name="wee", description="Only the proper person knows")
    async def wee(self, ctx):
        if ctx.author.id == 389306174119608321:
            await ctx.respond("https://tenor.com/view/3mresen-little-girl-gif-24374514")
            await ctx.respond("<@696740455789887599> ^^")
            await ctx.respond("https://tenor.com/view/spinning-little-girl-gif-14293658")
            await ctx.respond("<@696740455789887599> ^^")

            return
        else:
            await ctx.respond("You do not have proper perms to run this command MAFKA")
    
    @discord.slash_command(name="hammer", description="You know")
    async def hammer(self, ctx):
        if(ctx.author.id != 696740455789887599):
            await ctx.respond("You do not have proper perms to run this command MAFKA")
            return
        await ctx.respond("https://tenor.com/view/minion-bonk-hammer-minions-despicable-me-gif-5290684")

def setup(bot):
    bot.add_cog(Dev(bot))
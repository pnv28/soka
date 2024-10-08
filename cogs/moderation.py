import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import MissingPermissions
from datetime import timedelta
import asyncio

class Moderation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(name="kick", description="Kicks a user from a server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:Option(discord.Member, description="Who to kick"), reason:Option(str, description="Reason", required=False)):
        if(ctx.author.id == member.id):
            await ctx.respond("You can not kick yourself")
            return
        if reason == None:
            reason = f"No reason provided by {ctx.author}"
        await member.kick(reason=reason)
        await ctx.respond(f"<@{member.id}> has been kick from **{ctx.guild}**\nReason:{reason}") 
    
    @kick.error
    async def kick(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You do not have permission to run that command")
        else:
            raise error

    @discord.slash_command(name="ban", description="Bans an user")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:Option(discord.Member, description="Who to ban"), reason:Option(str, description="Reason", required=False)):
        if(ctx.author.id == member.id):
            await ctx.respond("You can not ban yourself")
            return
        if reason == None:
            reason = f"No reason provided by the user <@{ctx.author.id}>"
        await member.ban(reason=reason)
        await ctx.respond(f"<@{member.id}> has been banned from **{ctx.guild}**\nReason:{reason}")

    @ban.error
    async def banerror(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You do not have permission to run that command")
        else:
            raise error


    @discord.slash_command(name="timeout", description="It timesout the user")
    @commands.has_permissions(moderate_members = True)
    async def timeout(self, ctx, member: Option(discord.Member, description="Whom to time out"), reason:Option(str, description="Reason", required=False), days:Option(int, description="Amount of days you want to timeout the user", max_value=28, required=False), hours:Option(int, description="Amount of hours you want to timeout the user", max_value=23, required=False), minutes:Option(int, description="Amount of minutes to time out someone", max_value=59, required=False), seconds:Option(int, description="Amount of seconds to time out someone", max_value=59, required=False)):
        if member.timed_out == True:
            await ctx.respond("You can not timed out some one who is already timedout")
            return
        if ctx.author.id == member.id:
            ctx.respond("You can not timeout yourself")
            return
        if days == None:
            days = 0
        if hours == None:
            hours = 0
        if minutes == None:
            minutes = 0
        if seconds == None:
            seconds = 0
        duration=timedelta(days = days, hours = hours, minutes=minutes, seconds=seconds)
        if reason == None:
            reason = f"No Reason provided by user {ctx.author}"
        await member.timeout_for(duration)
        await ctx.respond(f"<@{member.id}> has been timed out for {days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds\nReason: {reason}")
        
    @timeout.error
    async def timeouterror(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"You do not have the permissions to do this command")
        else:
            raise error

    @discord.slash_command(name="purge", description="Deletes number of specified messages")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def purge(self, ctx, no: Option(int, description="Number of messages to purge")):
        await ctx.defer()
        z = await ctx.channel.purge(limit = no)
        await asyncio.sleep(2)
    
    @purge.error
    async def purgeerror(ctx, error):
        if isinstance(eror, MissingPermissions):
            await ctx.respond(f"You do not have the permissions to do this command")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(error)
        else:
            raise error



def setup(bot):
    bot.add_cog(Moderation(bot))
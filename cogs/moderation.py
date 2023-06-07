import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import MissingPermissions

class Moderation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    f
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

def setup(bot):
    bot.add_cog(Moderation(bot))
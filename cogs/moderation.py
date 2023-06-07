import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import MissingPermissions

class Moderation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="kick", description="Kicks a user from a server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:Option(discord.Member, description="Who to ban"), reason:Option(str, description="Reason", required=False)):
        if(ctx.author.id == member.id):
            await ctx.respond("You can not kick yourself")
            return
        if reason == None:
            reason = f"No reason provided by {ctx.author}"
        await member.kick(reason=reason)
        await ctx.respond(f"<@{member.id}> has been kick from {ctx.guild}") 

def setup(bot):
    bot.add_cog(Moderation(bot))
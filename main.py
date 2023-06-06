import discord
import os

bot=discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online")

@bot.slash_command(name="ping", description="Responds with pong!")
async def ping(ctx):
    await ctx.respond("Pong!")

bot.load_extension('cogs.dev')

bot.run("MTExNTY0MTQyMTY1MTc4NzgzNg.GOYjxU.57VoHKzxGu-qjJZRcnyWsb_FDJn3aTkAGPMbSs")
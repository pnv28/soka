import discord
import os

bot=discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online")

cogList = [
    'dev',
    'fun'
]

print("Loading Cogs")
for cog in cogList:
    bot.load_extension(f'cogs.{cog}')
    print(f"Loaded {cog}.py")

bot.run("MTExNTY0MTQyMTY1MTc4NzgzNg.GOYjxU.57VoHKzxGu-qjJZRcnyWsb_FDJn3aTkAGPMbSs")
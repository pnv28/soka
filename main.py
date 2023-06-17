import discord
import os
import logging
from discord.ext import commands
from discord.ext.commands import MissingPermissions


#token = os.environ['token']

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = discord.Bot()


@bot.event
async def on_ready():
  print(f"{bot.user} is ready and online")

@bot.event
async def on_application_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.respond(error)
  if isinstance(error, MissingPermissions):
    await ctx.respond("You do not have permission to run that command")
  else:
    raise error

cogList = ['dev', 'moderation', 'fun']
print("Loading Cogs")
for cog in cogList:
  bot.load_extension(f'cogs.{cog}')
  print(f"Loaded {cog}.py")

bot.run("MTExNTY0MTQyMTY1MTc4NzgzNg.GOYjxU.57VoHKzxGu-qjJZRcnyWsb_FDJn3aTkAGPMbSs")

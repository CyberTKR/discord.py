from discord.ext import commands as discordCommands
import discord as discordBot
import os

intents = discordBot.Intents.all()
sWQfMFyt = discordCommands.Bot(intents=intents,command_prefix='>tolg: ')

@sWQfMFyt.event
async def setup_hook():
  for filename in os.listdir('DiscordCog'):
    if filename.endswith('.py'):
        await sWQfMFyt.load_extension(f'DiscordCog.{filename[:-3]}')
        print(f"Loaded Cog: {filename[:-3]}")
    else:
        print("Unable to load pycache folder.")

sWQfMFyt.run("BOT_TOKEN")
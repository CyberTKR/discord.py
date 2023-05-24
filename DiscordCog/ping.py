from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot
import time

class ping(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="ping", description="🤖 Ping")
    async def ping(self,tolga: discordBot.Interaction):
        start_time = time.monotonic()
        embed = discordBot.Embed(title="Pong!", color=0x00FFFF)
        await tolga.response.send_message(embed=embed)
        end_time = time.monotonic()
        elapsed_time = round((end_time - start_time) * 1000, 2)
        embed.add_field(name="Bot Ping", value=f"{elapsed_time} ms", inline=False)
        await tolga.followup.send(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(ping(sWQfMFyt))
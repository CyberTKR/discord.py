from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands

class pause(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="pause", description="▶️ Pause")
    async def pause(self,tolga: discordBot.Interaction):
        voice_sWQfMFyt = discordBot.utils.get(self.sWQfMFyt.voice_sWQfMFyts, guild=tolga.guild)
        voice_sWQfMFyt.pause()
        await tolga.response.send_message("Pause Music.")


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(pause(sWQfMFyt))
from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands

class resume(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt
        
        
    @slashCommand.command(name="resume", description="▶️ Resume")
    async def resume(self,tolga: discordBot.Interaction):
        voice = discordBot.utils.get(self.sWQfMFyt.voice_sWQfMFyts, guild=tolga.guild)
        if voice and voice.is_paused():
            voice.resume()
            await tolga.response.send_message("Audio playback resumed.")
        else:
            await tolga.response.send_message("Audio playback is not currently paused.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(resume(sWQfMFyt))
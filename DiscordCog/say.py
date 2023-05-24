from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class say(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="say", description="🤖 Text")
    async def say(tolga: discordBot.Interaction, text_for_say: str):
        await tolga.response.send_message(
            f" {tolga.user.mention} {text_for_say}"
        )

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(say(sWQfMFyt))
from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands

class spoiler(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="spoiler", description="🤖 Spoiler")
    async def translate(self,ctx: discordBot.Interaction, text: str):
        spoiler_message = f'||{text}||'
        await ctx.response.send_message(f'{spoiler_message}')


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(spoiler(sWQfMFyt))
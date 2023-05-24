from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands
from googletrans import Translator

class translate(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="translate", description="🤖 Translator")
    async def translate(self,ctx: discordBot.Interaction, text: str, lang: str):
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        await ctx.response.send_message(f'{translated.text}')


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(translate(sWQfMFyt))
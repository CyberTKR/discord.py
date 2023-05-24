from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class avatar(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="avatar", description="🤖 Avatar")
    async def avatar(self,tolga: discordBot.Interaction,
        member: discordBot.Member):
        embed = discordBot.Embed(title=f'{member.name}\'s Avatar', color=0x00FFFF)
        embed.set_image(url=member.avatar)
        await tolga.response.send_message(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(avatar(sWQfMFyt))
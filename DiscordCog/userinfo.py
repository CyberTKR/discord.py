from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands

class userinfo(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="userinfo", description="🤖 Userinfo")
    async def user_info(self,tolga: discordBot.Interaction,
        member: discordBot.Member):
        embed = discordBot.Embed(title=f'{member.name}\'s Info', color=0x00FFFF)
        embed.add_field(name='Username', value=member.name)
        embed.add_field(name='Discriminator', value=member.discriminator)
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Status', value=member.status)
        embed.add_field(name='Joined Server', value=member.joined_at)
        embed.add_field(name='Joined Discord', value=member.created_at)
        embed.set_thumbnail(url=member.avatar)
        await tolga.response.send_message(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(userinfo(sWQfMFyt))
from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands

class serverinfo(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="serverinfo", description="🤖 Serverinfo")
    async def serverinfo(self,tolga: discordBot.Interaction):
        server = tolga.guild
        embed = discordBot.Embed(title = f"{server.name} Info", description = "Information of this Server", color = discordBot.Color.blue())
        embed.add_field(name = '🆔Server ID', value = f"{server.id}", inline = True)
        embed.add_field(name = '📆Created On', value = server.created_at.strftime("%b %d %Y"), inline = True)
        embed.add_field(name = '👑Owner', value = f"{server.owner}", inline = True)
        embed.add_field(name = '👥Members', value = f'{server.member_count} Members', inline = True)
        embed.add_field(name = '💬Channels', value = f'{(len(server.text_channels))} Text | {(len(server.voice_channels))} Voice', inline = True)
        embed.set_author(name = f'{server.name}',icon_url = server.icon.url)
        embed.set_thumbnail(url = server.icon.url)
        embed.set_footer(text = "⭐ • Duo")    
        await tolga.response.send_message(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(serverinfo(sWQfMFyt))
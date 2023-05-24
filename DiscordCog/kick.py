from discord import app_commands as slashCommand
import discord as discordBot,datetime
from discord.ext import commands as discordCommands
from typing import Optional

class kick(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="kick", description="Kicks specified user from the server.")
    @discordCommands.has_permissions(administrator=True)
    async def kick(self,
        tolga: discordBot.Interaction,
        member: discordBot.Member,
        reason: Optional[str] = None,
    ):
        await member.kick(reason=reason)
        embed = discordBot.Embed(
            title=f"👟Notification Kickout",
            description=f"{member.mention} sunucudan başarıyla atıldı.\n\nSebep: {reason}",
            color=discordBot.Color.green(),
            timestamp=datetime.datetime.utcnow(),
        )
        embed.set_footer(text=tolga.user.name, icon_url=tolga.user.avatar)
        await tolga.response.send_message(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(kick(sWQfMFyt))
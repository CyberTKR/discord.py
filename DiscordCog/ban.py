from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands
import datetime
from typing import Optional

class ban(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="ban", description="Banned specified user from the server.")
    @discordCommands.has_permissions(administrator=True)
    async def ban(self,tolga: discordBot.Interaction, member: discordBot.Member, *,
        reason: Optional[str] = None,delete_days: Optional[int] = 0):
        if not member:
            await tolga.response.send_message("Please mention a valid member to ban!")
        else:
            try:
                await member.ban(delete_message_days=delete_days, reason=reason)
                embed = discordBot.Embed(
                    title=f"🚫 Notification Banned",
                    description=f"{member.mention} sunucudan başarıyla banlandi.\n\nSebep: {reason}",
                    color=discordBot.Color.green(),
                    timestamp=datetime.datetime.utcnow(),
                )
                embed.set_thumbnail(url=member.avatar)
                await tolga.response.send_message(embed=embed)
            except discordBot.Forbidden:
                await tolga.response.send_message("I don't have the required permissions to ban that member.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(ban(sWQfMFyt))
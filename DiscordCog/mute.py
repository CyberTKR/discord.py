from discord import app_commands as slashCommand
import discord as discordBot,datetime
from discord.ext import commands as discordCommands
from typing import Optional

class mute(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="mute", description="Muted 🔇🤖")
    @discordCommands.has_permissions(administrator=True)
    async def mute(self,tolga: discordBot.Interaction, member: discordBot.Member, *,
        reason: Optional[str] = None):
        if not member:
            await tolga.response.send_message("Please mention a valid member to mute!")
        else:
            muted_role = discordBot.utils.get(tolga.guild.roles, name="Muted")
            if not muted_role:
                muted_role = await tolga.guild.create_role(name="Muted")
                for channel in tolga.guild.channels:
                    await channel.set_permissions(muted_role, speak=False, send_messages=False)
            try:
                if reason == None:
                  reason = None
                await member.add_roles(muted_role, reason=reason)
                embed = discordBot.Embed(
                    title=f"🔇 Notification Mute",
                    description=f"{member.mention} sesi kapatildi.\n\nSebep: {reason}",
                    color=discordBot.Color.green(),
                    timestamp=datetime.datetime.utcnow(),
                )
                embed.set_thumbnail(url=member.avatar)
                await tolga.response.send_message(embed=embed)
            except discordBot.Forbidden:
                await tolga.response.send_message("I don't have the required permissions to mute that member.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(mute(sWQfMFyt))
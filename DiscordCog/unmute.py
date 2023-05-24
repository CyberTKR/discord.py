from discord import app_commands as slashCommand
import discord as discordBot,datetime
from discord.ext import commands as discordCommands
from typing import Optional

class unmute(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="unmute", description="Unmute 🔊🤖")
    @discordCommands.has_permissions(administrator=True)
    async def unmute(self,tolga: discordBot.Interaction, member: discordBot.Member, *,
        reason: Optional[str] = None):
        if not member:
            await tolga.response.send_message("Please mention a valid member to unmute!")
        else:
            muted_role = discordBot.utils.get(tolga.guild.roles, name="Muted")
            if not muted_role:
                await tolga.response.send_message("This member is not muted!")
            else:
                try:
                    if reason == None:
                      reason = None
                    await member.remove_roles(muted_role, reason=reason)
                    embed = discordBot.Embed(
                        title=f"🔊 Notification Unmute",
                        description=f"{member.mention} sesi acildi.\n\nSebep: {reason}",
                        color=discordBot.Color.green(),
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.set_thumbnail(url=member.avatar)
                    await tolga.response.send_message(embed=embed)
                except discordBot.Forbidden:
                    await tolga.response.send_message("I don't have the required permissions to unmute that member.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(unmute(sWQfMFyt))
from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class removerole(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="removerole", description="RemoveRole 🎭.")
    @discordCommands.has_permissions(administrator=True)
    async def removerole(self,
        tolga: discordBot.Interaction, member: discordBot.Member, role: discordBot.Role):
        await member.remove_roles(role)
        await tolga.response.send_message(f"{member.mention} kullanıcısına {role.mention} rolü geri alindi.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(removerole(sWQfMFyt))
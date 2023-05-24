from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class addrole(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="addrole", description="AddRole 🎭.")
    @discordCommands.has_permissions(administrator=True)
    async def AddRole(self,
        tolga: discordBot.Interaction, member: discordBot.Member, role: discordBot.Role):
        await member.add_roles(role)
        await tolga.response.send_message(f"{member.mention} kullanıcısına {role.mention} rolü verildi.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(addrole(sWQfMFyt))
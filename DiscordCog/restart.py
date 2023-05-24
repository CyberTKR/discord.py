from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import sys,os




class restartbot(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @staticmethod
    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)


    @discordCommands.command(name="restart", description="↻ Restartbot")
    @discordCommands.has_permissions(administrator=True)
    async def restart(self,ctx):
            await self.restart_program()


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(restartbot(sWQfMFyt))
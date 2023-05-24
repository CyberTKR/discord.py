from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands


class testBot(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt


    @discordCommands.command(name="testBot", description="! testBot")
    @discordCommands.has_permissions(administrator=True)
    async def testBot(self,ctx):
            await ctx.send("Hi tolga I'm DiscordBot")


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(testBot(sWQfMFyt))
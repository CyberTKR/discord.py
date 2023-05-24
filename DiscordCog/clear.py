from discord import app_commands as slashCommand
import discord as discordBot,asyncio
from discord.ext import commands as discordCommands

class clear_messages(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="clear", description="🧹 Clear messages")
    @discordCommands.has_permissions(administrator=True)
    async def clear_messages(self,tolga: discordBot.Interaction, amount: int):
        await tolga.response.defer()
        await tolga.followup.send(f"{amount} message(s) will be deleted.")

        await asyncio.sleep(5)
        channel = tolga.channel
        messages = []
        async for message in channel.history(limit=amount + 1):
            messages.append(message)
        await channel.delete_messages(messages)

        embed = discordBot.Embed(title="🧹 Messages cleared!", color=discordBot.Color.green())
        embed.add_field(name="Number of messages deleted:", value=amount, inline=False)

        await tolga.followup.send(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(clear_messages(sWQfMFyt))
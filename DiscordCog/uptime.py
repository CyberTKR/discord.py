from discord import app_commands as slashCommand
import discord as discordBot,datetime,time
from discord.ext import commands as discordCommands
start_timestamp = time.time()
startTime = datetime.datetime.fromtimestamp(start_timestamp)

class uptime(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="uptime", description="🤖 Uptime")
    async def uptime(self,tolga: discordBot.Interaction):
        delta_uptime = datetime.datetime.utcnow() - startTime
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        uptime_string = f"{days}d, {hours}h, {minutes}m, {seconds}s"

        # Create the embed with the bot's profile picture and uptime information
        embed = discordBot.Embed(title="Bot Uptime", description=f"The bot has been running for {uptime_string}.", color=discordBot.Color.blurple())
        embed.set_author(name=self.sWQfMFyt.user.name, icon_url=self.sWQfMFyt.user.avatar)

        # Send the embed as a response to the interaction
        await tolga.response.send_message(embed=embed)


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(uptime(sWQfMFyt))
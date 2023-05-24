from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands

class helps(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="help", description="🤖 BotHelp")
    async def help(self,tolga: discordBot.Interaction):
        embed = discordBot.Embed(title='Bot Commands', description='Here are the available commands:', color=0x00FFFF)
        embed.set_thumbnail(url='https://i.hizliresim.com/8s2d9py.png')
        embed.set_footer(text='Bot created by CyberTK')

        embed.add_field(name='/help', value='Displays information about the bot and available commands.', inline=True)
        embed.add_field(name='/ping', value='Calculates the bot\'s latency (ping) and reports it to the user.', inline=False)
        embed.add_field(name='/say', value='Say to input.', inline=False)
        embed.add_field(name='/avatar', value='Displays the profile picture of the user or the specified user.', inline=False)
        embed.add_field(name='/userinfo', value='Displays information about the user.', inline=False)
        embed.add_field(name='/serverinfo', value='Displays information about the server.', inline=False)
        embed.add_field(name='/kick', value='Kicks the specified user from the server.', inline=False)
        embed.add_field(name='/ban', value='Bans the specified user from the server.', inline=False)
        embed.add_field(name='/mute', value='Mutes the specified user in text and/or voice channels.', inline=False)
        embed.add_field(name='/unmute', value='Unmutes the specified user in text and/or voice channels.', inline=False)
        embed.add_field(name='/clear', value='Deletes the specified number of messages.', inline=False)
        embed.add_field(name='/play', value='Plays the specified music.', inline=False)
        embed.add_field(name='/pause', value='Stops the music.', inline=False)
        embed.add_field(name='/resume', value='Resume the music.', inline=False)
        embed.add_field(name='/uptime', value='Start\'s for bot time.', inline=False)
        embed.add_field(name='/translate', value='Translator.', inline=False)
        embed.add_field(name='/spoiler', value='Message Add Spoiler.', inline=False)
        embed.add_field(name='/spotify', value='Spotify search query music.', inline=False)
        embed.add_field(name='/profile', value='Profile Detail.', inline=False)
        embed.add_field(name='/addrole', value='Add user to role.', inline=False)
        embed.add_field(name='/removerole', value='Remove user to role.', inline=False)
        embed.add_field(name='/weather', value='Weather.', inline=False)
        embed.add_field(name='/createchannel', value='Createchannel.', inline=False)
        embed.add_field(name='/deletechannel', value='Deletechannel.', inline=False)
        embed.add_field(name='/createcategorych', value='Createchannel for category.', inline=False)
        embed.add_field(name='/deletecategorych', value='Deletechannel for category.', inline=False)
        embed.add_field(name='>tolg: restart', value='Restart to bot.', inline=False)
        embed.add_field(name='>tolg: testBot', value='testBot.', inline=False)
        await tolga.response.send_message(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(helps(sWQfMFyt))
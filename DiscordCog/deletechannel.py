from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class deletechannel(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="deletechannel", description="📜 Delete Text Channel")
    @discordCommands.has_permissions(administrator=True)
    async def deleteChannels(self,tolga: discordBot.Interaction, channel_name: str):
        # Komut kullanıcısından kanal adını alın
        guild = tolga.guild # Sunucu nesnesini alın
        existing_channel = discordBot.utils.get(guild.channels, name=channel_name) # Kanalın var olup olmadığını kontrol edin
        if existing_channel:
            # Kanalın var olduğundan emin olun
            await existing_channel.delete()
            await tolga.response.send_message(f'Kanal {channel_name} silindi!')
        else:
            await tolga.response.send_message('Kanal bulunamadı!')

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(deletechannel(sWQfMFyt))
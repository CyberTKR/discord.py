from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class createchannel(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="createchannel", description="📜 Create Text Channel")
    @discordCommands.has_permissions(administrator=True)
    async def create(self,tolga: discordBot.Interaction, channel_name: str):
        # Komut kullanıcısından kanal adını alın
        guild = tolga.guild # Sunucu nesnesini alın
        existing_channel = discordBot.utils.get(guild.channels, name=channel_name) # Kanalın var olup olmadığını kontrol edin
        if not existing_channel:
            # Kanalın henüz olmadığına emin olun
            await guild.create_text_channel(channel_name)
            await tolga.response.send_message(f'Kanal {channel_name} oluşturuldu!')
        else:
            await tolga.response.send_message('Kanal zaten var!')

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(createchannel(sWQfMFyt))
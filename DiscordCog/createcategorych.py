from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class createcategorych(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="createcategorych", description="📜 Create Text Channel For Category")
    @discordCommands.has_permissions(administrator=True)
    async def createChannels(self,tolga: discordBot.Interaction, category_name: str, channel_name: str):
        guild = tolga.guild # Sunucu nesnesini alın
        existing_category = discordBot.utils.get(guild.categories, name=category_name) # Kategorinin var olup olmadığını kontrol edin
        if existing_category:
            # Kategori varsa, yeni bir metin kanalı oluşturun ve kategoriye ekleyin
            await guild.create_text_channel(channel_name, category=existing_category)
            await tolga.response.send_message(f'Kanal {channel_name} kategoride {category_name} oluşturuldu!')
        else:
            await tolga.response.send_message(f'Kategori {category_name} bulunamadı!')

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(createcategorych(sWQfMFyt))
from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot

class deletecategorych(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="deletecategorych", description="📜 Delete Text Channel For Category")
    @discordCommands.has_permissions(administrator=True)
    async def create(self,tolga: discordBot.Interaction, category_name: str, channel_name: str):
        # Komut kullanıcısından kanal adını alın
        guild = tolga.guild # Sunucu nesnesini alın
        existing_category = discordBot.utils.get(guild.categories, name=category_name) # Kategorinin var olup olmadığını kontrol edin
        if existing_category:
            # Kategori varsa, belirtilen isimdeki kanalı arayın ve silin
            existing_channel = discordBot.utils.get(existing_category.channels, name=channel_name)
            if existing_channel:
                await existing_channel.delete()
                await tolga.response.send_message(f'Kanal {channel_name} silindi!')
            else:
                await tolga.response.send_message(f'Kanal {channel_name} bulunamadı!')
        else:
            await tolga.response.send_message(f'Kategori {category_name} bulunamadı!')

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(deletecategorych(sWQfMFyt))
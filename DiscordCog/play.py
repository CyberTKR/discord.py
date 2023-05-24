from discord import app_commands as slashCommand
import discord as discordBot,youtube_dl
from discord.ext import commands as discordCommands

class play(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="play", description="▶️ Play")
    async def play(self,tolga: discordBot.Interaction, url: str):
        await tolga.response.defer()
        voice_channel = tolga.user.voice.channel
        voice_sWQfMFyt = discordBot.utils.get(self.sWQfMFyt.voice_sWQfMFyts, guild=tolga.guild)

        if not voice_sWQfMFyt:
            voice_sWQfMFyt = await voice_channel.connect()

        # Create a youtube-dl extractor
        ytdl = youtube_dl.YoutubeDL()

        # Download the video and extract audio
        info = ytdl.extract_info(url, download=False)
        URL = info["formats"][0]["url"]

        # Play the audio in the voice channel
        voice_sWQfMFyt.play(discord.FFmpegPCMAudio(URL))

        # Create an embed with the information of the song being played
        embed = discordBot.Embed(title=f"{info['title']}", color=discordBot.Color.green())
        embed.set_thumbnail(url=info["thumbnail"])
        embed.add_field(name="Duration", value=info["duration"])
        embed.add_field(name="Channel", value=info["uploader"])
        embed.add_field(name="Views", value=info["view_count"])
        embed.set_footer(text='Bot created by CyberTK')

        await tolga.followup.send(embed=embed)

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(play(sWQfMFyt))
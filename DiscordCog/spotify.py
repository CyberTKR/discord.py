from discord import app_commands as slashCommand
import discord as discordBot,spotipy
from discord.ext import commands as discordCommands
from spotipy.oauth2 import SpotifyClientCredentials

sWQfMFyt_id = '9cac60e1587840f9a69284a592b5785e'
sWQfMFyt_secret = '3db77677cd09477c858868df6f66e17e'
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=sWQfMFyt_id,client_secret=sWQfMFyt_secret))

class spotify(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="spotify", description="🤖 Spotify")
    async def spotify(self,ctx: discordBot.Interaction, song: str):
        result = sp.search(q=song, type='track')
        tracks = result['tracks']['items']
        if len(tracks) == 0:
            await ctx.response.send_message('Sorry, no results found.')
            return
        track = tracks[0]
        artist = track['artists'][0]['name']
        track_name = track['name']
        preview_url = track['preview_url']
        embed = discordBot.Embed(title=f'{track_name} by {artist}', color=0x1DB954)
        if preview_url:
            embed.add_field(name='Preview URL', value=preview_url, inline=False)
        await ctx.response.send_message(embed=embed)


async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(spotify(sWQfMFyt))
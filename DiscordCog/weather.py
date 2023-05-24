from discord import app_commands as slashCommand
from discord.ext import commands as discordCommands
import discord as discordBot,json,requests

class weather(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="weather", description="🌩️ Weather")
    async def weather(self,tolga: discordBot.Interaction, location: str):
        api_key = "cda0502a82a8493e93a222443231005 "
        base_url = "http://api.weatherapi.com/v1/current.json?"
        complete_url = base_url + "key=" + api_key + "&q=" + location
        response = requests.get(complete_url)
        data = response.json()
        print(json.dumps(data,indent=2))
        if "error" not in data:
            celsius_temp = data["current"]["temp_c"]
            description = data["current"]["condition"]["text"]
            icon = data["current"]["condition"]["icon"]
            city_name = data["location"]["name"]
            country_name = data["location"]["country"]
            embed = discordBot.Embed(title=f'{city_name}, {country_name}', color=0x00FF00)
            embed.set_thumbnail(url=f'http:{icon}')
            embed.add_field(name="Temp", value=f'{celsius_temp} °C', inline=True)
            embed.add_field(name="Status", value=description.title(), inline=True)
            embed.add_field(name="Localtime", value=data["location"]["localtime"])
            await tolga.response.send_message(embed=embed)
        else:
            await tolga.response.send_message("Konum bulunamadı. Lütfen geçerli bir konum girin.")

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(weather(sWQfMFyt))
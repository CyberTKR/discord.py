from discord import app_commands as slashCommand
import discord as discordBot
from discord.ext import commands as discordCommands
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageChops

def circle(pfp,size = (215,215)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker (mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


class profile(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @slashCommand.command(name="profile", description="🤖 Profile")
    async def profile(self,tolga: discordBot.Interaction, member: discordBot.Member):
        name, nick, Id, status = str(member), member.name, str(member.id), "dawdadawd"
        created_at =  member.created_at.strftime("%a %b\n%B %Y")
        joined_at = member.joined_at.strftime("%a %b\n%B %Y")
        money, level = "3245324", "100"
        base = Image.open("./resimler/base.png").convert("RGBA")
        background = Image.open("./resimler/gaming1_background.png").convert("RGBA")
        pfp = member.avatar
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        draw = ImageDraw.Draw(base)
        pfp = circle(pfp,(215,215))
        font = ImageFont.truetype("./resimler/Nunito-Regular.ttf",38)
        akafont = ImageFont.truetype("./resimler/Nunito-Regular.ttf",30)
        subfont = ImageFont.truetype("./resimler/Nunito-Regular.ttf",25)
        draw.text((280,240), name, font = font)
        draw.text((270,315), nick, font = akafont)
        draw.text((65,490), Id, font = subfont)
        draw.text((405,490), status, font = subfont)
        draw.text((65,635), money, font = subfont)
        draw.text((405,635), level, font = subfont)
        draw.text((65,770), created_at, font = subfont)
        draw.text((405,770), joined_at, font = subfont)
        base.paste(pfp, (56,158), pfp)
        background.paste(base, (0,0),base)
        with BytesIO() as a:
          background.save(a, "PNG")
          a.seek(0)
          await tolga.response.send_message(file = discordBot.File(a,"profile.png"))

async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(profile(sWQfMFyt))
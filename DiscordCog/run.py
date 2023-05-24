from discord.ext import commands as discordCommands
import discord as discordBot,os
from PIL import Image, ImageDraw, ImageFont, ImageChops
from io import BytesIO
from .profile import circle
from tabulate import tabulate


class events(discordCommands.Cog):
    def __init__(self, sWQfMFyt):
        self.sWQfMFyt = sWQfMFyt

    @discordCommands.Cog.listener()
    async def on_ready(self):
        try:
            synced = await self.sWQfMFyt.tree.sync()
            await self.sWQfMFyt.change_presence(status=discordBot.Status.idle,activity=discordBot.Activity(type=discordBot.ActivityType.watching, name="CyberTK 🤖"))
            os.system("clear")
            print(f"{len(synced)} Komut esitlendi !")
            print(tabulate([['/help', '/ping'], ['/avatar', '/userinfo'], ['/serverinfo', '/kick'], ['/ban', '/mute'], ['/unmute', '/clear'], ['/play', '/pause'], ['/resume', '/uptime'], ['/translate', '/spoiler'], ['/spotify', '/profile'], ['/addrole', '/removerole'], ['/say', '/weather'], ['/createchannel', '/deletechannel'], ['/createcategorych', '/deletecategorych'],['>tolg: restart', '>tolg: testBot']]))
            a = "#"
            b = " "
            print(f"""
      Discord Genel Sunucu botu

           * Creator *

            CyberTK ✅︎

    𐄂 BotName: {self.sWQfMFyt.user.name}

    𐄂 BotID: {self.sWQfMFyt.user.id}

    """)
        except Exception as e:
            print(e)
            
    @discordCommands.Cog.listener()
    async def on_member_join(self,member):
        channel = discordBot.utils.get(member.guild.channels, name='join-leave') # JOIN-LEAVE CHANNEL NAME
        background = Image.open("./resimler/wel.jpg").convert("RGBA")
        pfp = member.avatar
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        draw = ImageDraw.Draw(background)
        pfp = circle(pfp,(250, 250))
        font = ImageFont.truetype("./resimler/Nunito-Regular.ttf",50)
        draw.text((170, 50), f"{member.guild.name}", color="white", font=font, align="center",stroke_fill="purple",stroke_width=5) 
        draw.text((150, 550), f"WELCOME", color="white", font=font, align="center",stroke_fill="purple",stroke_width=5) 
        draw.text((100, 700), f"{member.name}", color="white", font=font, align="center",stroke_fill="purple",stroke_width=5) 
        background.paste(pfp, (160, 235), pfp)
        background.paste(background, (0,0),background)
        with BytesIO() as a:
          background.save(a, "PNG")
          a.seek(0)
          await channel.send(file = discordBot.File(a,"profile.png"))
          await channel.send(f'Welcome {member.mention}!')

    @discordCommands.Cog.listener()
    async def on_member_remove(self,member):
        channel = discordBot.utils.get(member.guild.channels, name='join-leave') # JOIN-LEAVE CHANNEL NAME
        await channel.send(f'Bye bye {member.mention}!')
        
async def setup(sWQfMFyt):
    await sWQfMFyt.add_cog(events(sWQfMFyt))
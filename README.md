
# discord.py

## How to run?
 
- Adim 1: 
    
    * [x]  `Asagidaki token alma adimlarini uygulayarak tokeni alin`

- Adım 2: 
    
    * [x]  `Tokeni main.py icindeki BOT_TOKEN degeriyle yer degistirin.`

- Adım 3:
    
    * [x]  Komut satirina yazin `pip3 install -r requirements.txt.`

- Adım 4:
    
    * [x]  Komut satirina yazin `python3 main.py.`

## How do I get a discord bot token?
 
- Adım 1: Discord Developer Portal'a Giriş Yapın
    
`İlk olarak, web tarayıcınızı açın ve Discord Developer Portal sayfasına gidin. Eğer bir hesabınız yoksa, bir tane oluşturun ve oturum açın.`

- Adım 2: Uygulama Oluşturun
    
`Discord Developer Portal'a giriş yaptıktan sonra, üst menüde "Applications (Uygulamalar)" sekmesine tıklayın. Ardından, sağ üst köşede bulunan "New Application (Yeni Uygulama)" düğmesine tıklayın.`

- Adım 3: Botu Ayarlayın
    
`Uygulama oluşturduktan sonra, sol menüde "Bot" sekmesine gidin. Ardından, "Add Bot (Bot Ekle)" düğmesine tıklayın. Karşınıza bir onay mesajı çıkacak, "Yes, do it! (Evet, yap!)" seçeneğini seçin.`

- Adım 4: Botun Ayarlarını Yapılandırın

`Bot oluşturulduktan sonra, botunuzun ayarlarını yapılandırabilirsiniz. Bu bölümde, botunuzun adını, profili için bir avatar yükleyebilirsiniz. Ayrıca, burada botunuzun token'ını da bulacaksınız, bu token'ı botunuzun kodunda kullanacağız.`

- Adım 5: Bot İzinlerini Ayarlayın
    
`Sol menüde "OAuth2" sekmesine gidin. "Scopes (Kapsamlar)" bölümünde, botunuzu eklemek istediğiniz sunucuyu seçin. Ardından, "Bot Permissions (Bot İzinleri)" bölümünde botunuza vermek istediğiniz izinleri seçin. İzinlerinizi seçtikten sonra, otomatik olarak oluşturulan OAuth2 URL'sini kullanarak botunuzu sunucunuza ekleyebilirsiniz.`
## Yazarlar ve Teşekkür

- [@CyberTKR](https://www.github.com/CyberTKR)

  
## Kullanım/Örnekler

```python
from discord.ext import commands as discordCommands
import discord as discordBot
import os

intents = discordBot.Intents.all()
sWQfMFyt = discordCommands.Bot(intents=intents,command_prefix='>tolg: ')

@sWQfMFyt.event
async def setup_hook():
  for filename in os.listdir('DiscordCog'):
    if filename.endswith('.py'):
        await sWQfMFyt.load_extension(f'DiscordCog.{filename[:-3]}')
        print(f"Loaded Cog: {filename[:-3]}")
    else:
        print("Unable to load pycache folder.")

sWQfMFyt.run("BOT_TOKEN") #ADD YOUR BOT TOKEN
```

  
## Ekran Görüntüleri

![Uygulama Ekran Görüntüsü](https://i.hizliresim.com/bgz8ir6.png)

  
## Lisans

[BSD](https://github.com/CyberTKR/discord.py/blob/CyberTK/LICENSE)

  
## Demo


[![Watch the video](https://i.ytimg.com/vi/1l-GhdKmSFI/hqdefault.jpg)](https://youtu.be/1l-GhdKmSFI)

  

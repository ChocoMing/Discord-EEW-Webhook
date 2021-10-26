import re
import os
import json
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed

from time import sleep

load_dotenv()

Webhook_URL = os.getenv("WEBHOOK_URL")
city = os.getenv("CITY")
Area = os.getenv("AREA")

with open('file.json', mode='r', encoding='UTF8') as jfile:
    jdate1 = json.load(jfile)
    
ggg = re.sub(r"(\d)$", "\\1級", jdate1["1"]).replace("-", "弱").replace("+", "強")
sec = jdate1["2"]

webhook = DiscordWebhook(url=Webhook_URL, username="地牛Wake UP!", 
        avatar_url="https://cdn.discordapp.com/attachments/825307887219114034/902494942352519168/FB_IMG_1635241955969.jpg",
        content=f'倒數{sec}抵達!')

embed = DiscordEmbed(title=':rotating_light:【地震速報】', description='慎防搖晃(預估震度)', color='03b2f8')
embed.set_author(name='Taiwan EEW System', 
        icon_url='https://media.discordapp.net/attachments/345147297539162115/732527807435112478/EEW.png')
embed.set_timestamp()
embed.add_embed_field(name=city, value=f"{Area} {ggg}")
embed.set_footer(text=f'預計{sec}後到達')
webhook.add_embed(embed)

sent_webhook = webhook.execute()

sec1 = int(sec)
aaa = sent_webhook
while sec1:
    sec1 = sec1 - 1

    sleep(0.6)

    webhook.content = f'倒數{sec1}抵達!'
    sent_webhook = webhook.edit(aaa)

    if sec1 == 0:
        sleep(0.6)
        webhook.content = f'已抵達!'
        sent_webhook = webhook.edit(aaa)
        break

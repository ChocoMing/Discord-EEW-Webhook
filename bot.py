import re
from aiohttp.helpers import TOKEN
import discord
import datetime
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

bot = discord.Client()

#以下你你可以設定的變數
city = "XX市" #你要顯示的縣、市 例:台北市
Area = "XX區" #你要顯示的區 例:松山區
Webhook_URL = "你的Webhook網址"
BOT_TOKEN = "你的TOKEN" #到https://discord.com/developers/applications 取得(需有Discord帳號)
#------------------------------

@bot.event
async def on_ready():
    jdate1 = {"1": "1級"}
    ggg = re.sub(r"(\d)$", "\\1級", jdate1["1"]).replace(
        "-", "弱").replace("+", "強")
    embed = discord.Embed(title=':rotating_light:【地震速報】',
                          timestamp=datetime.datetime.utcnow(),
                          description='慎防搖晃(預估震度)', color=0x03b2f8)
    embed.set_author(name='Taiwan EEW System',
                     icon_url='https://media.discordapp.net/attachments/345147297539162115/732527807435112478/EEW.png')
    embed.add_field(name=city, value= f"{Area} {ggg}")

    async with aiohttp.ClientSession() as session:
        for webhook_url in [Webhook_URL]:
            webhook = Webhook.from_url(
                webhook_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(embed=embed, username="地牛Wake Up!", avatar_url="https://scontent.ftpe4-1.fna.fbcdn.net/v/t1.6435-9/31783240_381366989015031_1910938126604304384_n.png?_nc_cat=101&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=8ND3oeqVlMoAX_bm4Wu&_nc_ht=scontent.ftpe4-1.fna&oh=804e6c88f560d73055ea327509a26b08&oe=61445067")
    await bot.close()

bot.run(BOT_TOKEN)
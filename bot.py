import re
import discord
import datetime
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

bot = discord.Client()

@bot.event
async def on_ready():
    jdate1 = {"1": "1級"}
    ggg = re.sub(r"(\d)$", "\\1級", jdate1["1"]).replace(
        "-", "弱").replace("+", "強")
    embed = discord.Embed(title=':rotating_light:【地震速報】',
                          timestamp=datetime.datetime.utcnow(),
                          description='慎防搖晃(預估震度)', color=0x03b2f8)
    embed.set_author(name='Taiwan EEW System',
                     icon_url='icon_url')
    embed.add_field(name='XX市', value=f'XX區 {ggg}')
    embed.set_footer(text="巧克明#8831", icon='https://cdn.discordapp.com/attachments/824601587867058207/861242805954412574/167193030_914035709353788_1311373607286801533_n.png')

    async with aiohttp.ClientSession() as session:
        for webhook_url in 'webhook_url':
            webhook = Webhook.from_url(
                webhook_url, adapter=AsyncWebhookAdapter(session))
            await webhook.send(embed=embed, username="webhook_name", avatar_url="icon_url")
    await bot.close()

bot.run("TOKEN")
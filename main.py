import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import string
import time
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='/', intents=intents)

keep_alive()

user_agent = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.43 Mobile Safari/537.36'
referer = 'https://linkvertise.com'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith('http'):
            bypass_msg = await message.channel.send("กำลัง Bypass")
            start_time = time.time()

            response1 = requests.get(message.content, headers={'User-Agent': user_agent})
            headers2 = {'Referer': referer, 'User-Agent': user_agent}
            response2 = requests.get('https://fluxteam.net/android/checkpoint/check1.php', headers=headers2)
            headers3 = {'Referer': referer, 'User-Agent': user_agent}
            response3 = requests.get('https://fluxteam.net/android/checkpoint/main.php', headers=headers3)

            elapsed_time = time.time() - start_time

            lines = response3.text.splitlines()
            content = lines[184].replace('</code>', '')
            cleaned_content = content.translate({ord(char): None for char in string.whitespace})

            print(f"Key: {cleaned_content}")

            webhook_url = 'https://discord.com/api/webhooks/1186228370242015242/mY5dwIzMZGpl4SHEORWZA-8q-TGMqKCGRAOoAXk1Hvo35L0Ot3LGzgIeVnUNSrEl0wKh'
            webhook = DiscordWebhook(url=webhook_url)
            embed = DiscordEmbed(title=f"Bypass Success by {message.author.name}", description=f"```Key: {cleaned_content}```", color=0x00ff00)
            webhook.add_embed(embed)
            webhook.execute()

            await message.channel.send(f" {cleaned_content}")
            await bypass_msg.delete()

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run(os.environ['token'])

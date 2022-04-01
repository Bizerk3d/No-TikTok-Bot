import os
my_secret = os.environ['token']
import discord
from keepawake import keep_alive

client = discord.Client()

words = ["tiktok", "TikTok", "Tiktok", "tikTok"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  msg = message.content

  if any (word in msg for word in words):   
    await message.delete()
    await message.channel.send('Ah ah ah, what\'s the magic word?!')

keep_alive()
client.run(my_secret)

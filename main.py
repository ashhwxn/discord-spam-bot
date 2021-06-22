import discord
client = discord.Client()
keywords = ["TEXT"]

@client.event
async def on_message(message):
  for i in range(len(keywords)):
    for j in range(30):
      await message.channel.send("TEXT")

client.run("TOKEN")

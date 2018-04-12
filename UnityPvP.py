import discord
import asyncio
client = discord.Client()

@client.event
async def on_ready():
        print("Logged in as:")
        print(client.user.name)
        print("ID:")
        print(client.user.id)
        print("Ready to use!")

@client.event
async def on_message(message):
    if  message.author == client.user:
        return
    elif message.content.startswith("!unitypvp"):
        await client.send_message(message.channel, "Hey, I am coded by @TryHard#3061!")

client.run("NDM0MTEyNzU2ODc1MjY0MDEx.DbFuHw.PjBqrOkGX0nCfz7t51zqIXjKOz4")

import asyncio
import os
import aiohttp
from discord import Client, Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
GUILD_ID = os.getenv("GUILD_ID")

intents = Intents.default()
intents.guilds = True
intents.messages = True

client = Client(intents=intents)

async def sleep(ms):
    await asyncio.sleep(ms / 1000)

async def remove_all_commands():
    url = f"https://discord.com/api/v10/applications/{CLIENT_ID}/guilds/{GUILD_ID}/commands"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                commands = await response.json()
            
            for command in commands:
                del_url = f"{url}/{command['id']}"
                async with session.delete(del_url, headers=headers) as del_response:
                    if del_response.status == 204:
                        print(f"Deleted command: {command['name']}")
                    else:
                        print(f"Failed to delete {command['name']}: {del_response.status}")
                await asyncio.sleep(1)
            
            print("All commands removed")
        except Exception as e:
            print(f"Error removing commands: {e}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await remove_all_commands()

@client.event
async def on_message(message):
    pass

client.run(TOKEN)

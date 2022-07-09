import discord, os
from discord.ext import commands

from config import(
    token
)

intents = discord.Intents().all()

client = commands.Bot(command_prefix="r.", case_insensitive=True, intents=intents)
client.remove_command("help")

for directory in os.listdir("./cogs"):
  for filename in os.listdir(f"./cogs/{directory}"):
    if filename.endswith('.py'):
      client.load_extension(f'cogs.{directory}.{filename[:-3]}')

@client.event
async def on_ready():
  print("\nBot is online")
  print("-------------")
  print(f"{client.user}")
  print("-------------")

client.run(token)
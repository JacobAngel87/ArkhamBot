import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


bot = commands.Bot(command_prefix=os.getenv('COMMAND_PREFIX'),
                   help_command=None)
@bot.command(name='balls')
async def price(ctx):
    await ctx.send(f"Joe Biden")

@client.event
async def on_voice_state_update(member, before, after):
  if not before.channel and after.channel and member.id == 951690798175506472:
    channel = client.get_channel(709505921092550658)
    await channel.send('Tyson has small balls.')
    
bot.run(TOKEN)
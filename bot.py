import os
from pydoc import cli
import sys
import discord
import json
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix=os.getenv('COMMAND_PREFIX'),
                   help_command=None)

@bot.command(name='balls')
async def balls(ctx):
    await ctx.send(f"Joe Biden")

@bot.command(name='dog')
async def dog(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    text = response.text
    data = json.loads(text)
    await ctx.send(data['message'])

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 795517016626167830: # nigs channel
            if member.id == 951690798175506472: # tyson discord id
                await member.guild.system_channel.send("Tyson has small balls.")
            if member.id == 678433535920570399: # evan discord id
                await member.guild.system_channel.send("Evan has a tiny shaft.")
            if member.id == 535610244894556209: # jacob discord id
                response = requests.get("https://dog.ceo/api/breeds/image/random")
                text = response.text
                data = json.loads(text)
                await member.guild.system_channel.send(data['message'])
                await member.guild.system_channel.send("Jacob has a MEGA DICK.")
                
bot.run(TOKEN)
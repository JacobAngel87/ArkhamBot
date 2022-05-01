import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=os.getenv('COMMAND_PREFIX'),
                   help_command=None)
@bot.command(name='balls')
async def price(ctx):
    await ctx.send(f"Joe Biden")



bot.run(TOKEN)
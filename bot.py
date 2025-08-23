# bot.py
import os
import random
import math
import time
import logging
import traceback
from datetime import datetime
from tkinter import messagebox

import discord
from discord.ext import commands
from discord.app_commands import CommandInvokeError
from discord import app_commands
from dotenv import load_dotenv
from discord.utils import get
import asyncio
import aiohttp



intents = discord.Intents.default()
intents.message_content = True
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
APPLICATION_ID = int(os.getenv('APPLICATION_ID'))

bot = commands.Bot(command_prefix="🍰", intents=intents, application_id=APPLICATION_ID)
developer_id = int(os.getenv('DEV_ID'))  # Replace with your own user ID

# Check if the user is the developer
async def is_developer(interaction: discord.Interaction):
    return interaction.user.id == int(developer_id)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'haii maidbot':
        await message.channel.send('haii!! ^w^', reference=message)

    if 'bwaa' in message.content:
        exclamations = random.randint(2,7)
        await message.channel.send('bwaa' + ("!" * exclamations), reference=message)

@bot.event
async def on_ready():

    print(f"Bot Status: {bot.user} has connected to Discord!")
    await bot.tree.sync()

    # Only sync commands for the developer
    if bot.user.id == developer_id:
        await bot.tree.sync()
        print("Bot Status: Commands have been synced.")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="videos about voice synthesizers .w."))

@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "☕":
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)
        if reaction and reaction.count > 0 and not payload.channel_id == 1359313137886691421:
            message.channel = bot.get_channel(1359314930561581118)
            print("A coffeeboardable message has appeared!")
            await message.channel.send

async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded cog {filename}')
            except:
                print(f'Failed to load cog {filename}')
async def main():
    await bot.load_extension('cogs.echo')
    await bot.load_extension('cogs.cat')
    await bot.load_extension('cogs.baka')

    await bot.start(TOKEN)

asyncio.run(main())
# bot.py
import os
import random
import math
import time
import logging
import traceback
from datetime import datetime

import discord
from discord.ext import commands
from discord.app_commands import CommandInvokeError
from discord import app_commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True
load_dotenv()
TOKEN = os.getenv('hahaha you thought you would get the actual token for the bot')
APPLICATION_ID = os.getenv('hahaha you thought you would get the actual token for the bot')

bot = commands.Bot(command_prefix="🍰", intents=intents, application_id=APPLICATION_ID)
developer_id = pretendthisismyid  # type: ignore # Replace with your own user ID

# Check if the user is the developer
async def is_developer(interaction: discord.Interaction):
    return interaction.user.id == developer_id

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'haii maidbot':
        await message.channel.send('haii!! ^w^', reference=message)

    if 'bwaa' in message.content:
        exclamations = random.randint(2,7)
        await message.channel.send('bwaa' + ("!" * exclamations), reference=message)

# Slash command Test
@bot.tree.command(name="meow", description="mrrp")
async def meow(interaction: discord.Interaction):

    response = random.randint(1,4)
    letters = random.randint(2, 7)

    match(response):
        case 1:
            reply = "meow" + ("!" * letters)
        case 2:
            reply = "mrrp" + ("!" * letters)
        case 3:
            reply = "nyaa" + ("!" * letters)
    await interaction.response.send_message(reply)

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} at {datetime.now()}")
    await bot.tree.sync()

    # Only sync commands for the developer
    if bot.user.id == developer_id:
        await bot.tree.sync()
        logging.info("Commands synced")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="VOCALOID music ^w^"))

# Echo command that is "hidden" for other users
@bot.tree.command(name="console", description="might have some secret commands")
@app_commands.describe(message="enter smth")
async def echo(interaction: discord.Interaction, message: str):
    if await is_developer(interaction) or "shhhhhhh find it yourself (writing this out won't work)" in message:
        await interaction.response.send_message("hehehe ;3", ephemeral=True)
        await interaction.channel.send(message)
    else:
        await interaction.response.send_message("not cool beans", ephemeral=True)

@bot.tree.command(name="vocaloid", description="oo ee oo")
async def vocaloid(interaction: discord.Interaction):

    songs = ["https://youtu.be/9nFBnro15vY", "https://youtu.be/tY8OhmplZWY", "https://youtu.be/cLAE17XhSY4", "https://youtu.be/xipClcza6fw",
             "https://youtu.be/sV2H712ldOI", "https://youtu.be/kbNdx0yqbZE", "https://youtu.be/-eDYT_20YhM", "https://youtu.be/LaEgpNBt-bQ",
             "https://youtu.be/NocXEwsJGOQ", "https://youtu.be/M7VSEZOQIlg", "https://youtu.be/vjBFftpQxxM", "https://youtu.be/HsZQOXZbWkQ"
             ]
    response = random.randint(1, len(songs))
    await interaction.response.send_message(songs[response - 1])

bot.run('hahaha you thought you would get the actual token for the bot')

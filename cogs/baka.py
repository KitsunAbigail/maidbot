from discord.ext import commands
from discord import app_commands
import discord

async def is_dev(interaction: discord.Interaction) -> bool:
    return interaction.user.id == developer_id

class Baka(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="vocaloid", description="oo ee oo")
    async def vocaloid(self, interaction: discord.Interaction):
        songs = ["https://youtu.be/9nFBnro15vY", "https://youtu.be/tY8OhmplZWY", "https://youtu.be/cLAE17XhSY4",
                 "https://youtu.be/xipClcza6fw",
                 "https://youtu.be/sV2H712ldOI", "https://youtu.be/kbNdx0yqbZE", "https://youtu.be/-eDYT_20YhM",
                 "https://youtu.be/LaEgpNBt-bQ",
                 "https://youtu.be/NocXEwsJGOQ", "https://youtu.be/M7VSEZOQIlg", "https://youtu.be/vjBFftpQxxM",
                 "https://youtu.be/HsZQOXZbWkQ",
                 "https://youtu.be/KlTNKOnfXFk"
                 ]

        response = random.randint(1, len(songs))
        await interaction.response.send_message(songs[response - 1])

    @app_commands.command(name="utauloid", description="tetoris")
    async def utauloid(self, interaction: discord.Interaction):
        songs = ["https://youtu.be/yZkPe7TEuyk", "https://youtu.be/dbfFDAHmP_c", "https://youtu.be/_AjJZEcMdww",
                 "https://youtu.be/01xG-Ggx6EE",
                 "https://youtu.be/1U6qefKcOrg", "https://youtu.be/_SRp1kc0088", "https://youtu.be/Soy4jGPHr3g",
                 "https://youtu.be/0iVlSNpq8i8",
                 "https://youtu.be/sqK-jh4TDXo", "https://youtu.be/qKOJ5_IkUXY", "https://youtu.be/1xEfMnXyGkA"
                 ]

        response = random.randint(1, len(songs))
        await interaction.response.send_message(songs[response - 1])

async def setup(bot: commands.Bot):
    print('loading echo command')
    await bot.add_cog(Baka(bot))
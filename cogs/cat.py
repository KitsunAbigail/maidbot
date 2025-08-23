from discord.ext import commands
from discord import app_commands
import discord

async def is_dev(interaction: discord.Interaction) -> bool:
    return interaction.user.id == developer_id

class Cat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="meow", description="mrrp")
    async def meow(self, interaction: discord.Interaction):

        response = random.randint(1, 4)
        letters = random.randint(2, 7)
        reply = ""
        match response:
            case 1:
                reply = "meow" + ("w" * (letters // 2)) + ("!" * letters)
            case 2:
                reply = "mrrp" + ("p" * (letters // 2)) + ("!" * letters)
            case 3:
                reply = "nyaa" + ("a" * (letters // 2)) + ("!" * letters)
            case 4:
                reply = "mrow" + ("w" * (letters // 2)) + ("!" * letters)
        await interaction.response.send_message(reply)

    @app_commands.command(name="mrrp", description="mrrp")
    @app_commands.describe(count="mrrp", caps="mrrp")
    async def mrrp(self, interaction: discord.Interaction, count: int, caps: bool):
        meows = ['meow', 'mrrp', 'mrow', 'nyaa', 'mraow', 'mew', 'purr', 'raow', 'mrr']
        meowy = ''
        for i in range(count):
            meowy += meows[random.randint(0, 8)]
        await interaction.response.send_message(meowy.upper() if caps else meowy, ephemeral=True)


async def setup(bot: commands.Bot):
    print('loading echo command')
    await bot.add_cog(Cat(bot))
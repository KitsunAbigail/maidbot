from discord.ext import commands
from discord import app_commands
import discord

async def is_dev(interaction: discord.Interaction) -> bool:
    return interaction.user.id == developer_id

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="console", description="might have some secret commands")
    @app_commands.describe(message="enter smth")
    async def echo(self, interaction: discord.Interaction, message: str):
        if "beans" in message:
            await interaction.response.send_message("hehehe ;3", ephemeral=True)
            await interaction.channel.send("yes beans")
        elif "do j" in message or "guys help" in message:
            await interaction.response.send_message("hehehe ;3", ephemeral=True)
            await interaction.channel.send("guys help")
            await interaction.channel.send("do j")
        elif "beequotes" in message:
            await interaction.response.send_message("`i wATN T A FU RSOUT RIGHT N(WWWW`, `(⁠｡⁠•́⁠︿⁠•̀⁠｡⁠)`,"
                                                        
                                                        """``╱|、
        (˚ˎ 。7
         |、˜〵
        じし ˍ,)``"""
                                                        ""
                                                        ""
                                                        """``∧,,,∧
        (  ̳• · • ̳)
        /    づ♡``"""
                                                        ""
                                                        "`https://cdn.discordapp.com/emojis/876785474805571605.gif?size=128&animated=true`"
                                                        "https://cdn.discordapp.com/emojis/1377083606350037134.webp?size=128", ephemeral=True)
        else:
            if await is_dev(interaction):
                print("Message sent  by: " + str(interaction.user.id) + " " + message)
                await interaction.response.send_message("hehehe ;3", ephemeral=True)
                await interaction.channel.send(message)
            else:
                await interaction.response.send_message("not cool beans", ephemeral=True)

async def setup(bot: commands.Bot):
    print('loading echo command')
    await bot.add_cog(General(bot))
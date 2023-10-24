import discord
from discord.ext import commands
app = commands.Bot(command_prefix="!", intents=discord.Intents.all())

app.run("")

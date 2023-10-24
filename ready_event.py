import discord
from discord.ext import commands
app = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@app.event
async def on_ready(ctx):
  print("=".repeat(15))
  print("|  {ctx}  |")
  print("was successfully ready!")

app.run("")

import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté comme {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("👋 Salut ! Je suis ton bot Discord hébergé sur Render.")

bot.run(os.getenv("TOKEN"))

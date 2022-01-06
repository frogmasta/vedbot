import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.listening, name="!")
bot = commands.Bot(command_prefix='!', activity=activity, status=discord.Status.online, intents=intents)


@bot.event
async def on_ready():
    print('VedBot 1.0 is successfully logged in!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command(name='Ved')
async def _ved(ctx):
    await ctx.send("Sexy man!")


bot.run(TOKEN)

import discord
from discord.ext import commands

from config.config import bot_token
from services.bot.register import register_user
from services.bot.swap import swap_currency
from services.bot.transfer import erc721, erc20, eth

description = '''This bot goes on to talk to the chain to get things done'''

intents = discord.Intents.default()
intents.members = False
intents.message_content = False

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

token = bot_token


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def register(ctx):
    register_user(ctx.author.id)
    await ctx.send("this will register users")


@bot.command()
async def transfer_eth(ctx, to_address, amount):
    await ctx.send("https://link.io?q=" + eth(to_address, amount))


@bot.command()
async def transfer_nft(ctx, token_address, to_address, token_id):
    await ctx.send("https://link.io?q=" + erc721(to_address, token_address, token_id))


@bot.command()
async def transfer_erc20(ctx, token_address, to_address, amount):
    await ctx.send("https://link.io?q=" + erc20(to_address, token_address, amount))


@bot.command()
async def swap(ctx, from_currency, to_currency, from_amount):
    swap_currency(from_currency, to_currency, from_amount)
    await ctx.send("this will swap " + from_amount + " " + from_currency + " to " + to_currency)


bot.run(token)

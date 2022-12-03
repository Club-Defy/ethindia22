import discord
from discord.ext import commands

from config.config import baseUrl, bot_token
from services.bot.register import register_user
from services.bot.swap import swap_currency
from services.bot.transfer import erc721, erc20, eth

description = '''This bot goes on to talk to the chain to get things done'''

intents = discord.Intents.default()
intents.members = False
intents.message_content = False

bot = commands.Bot(command_prefix='/', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def register(ctx):
    await ctx.send(register_user(ctx.author.id))


@bot.command()
async def transfer_eth(ctx, to_address, amount):
    await ctx.send(eth(to_address, amount))


@bot.command()
async def transfer_nft(ctx, token_address, to_address, token_id):
    await ctx.send(erc721(to_address, token_address, token_id))


@bot.command()
async def transfer_erc20(ctx, token_address, to_address, amount):
    await ctx.send(erc20(to_address, token_address, amount))


@bot.command()
async def swap_eth(ctx, from_amount, to_currency):
    await ctx.send(swap_eth(from_amount, to_currency))

@bot.command()
async def swap_erc20(ctx, from_amount, from_currency):
    await ctx.send(swap_erc20(from_amount, from_currency))

@bot.command()
async def swap(ctx, from_amount, from_currency, to_currency):
    await ctx.send(swap(from_amount, from_currency, to_currency))

bot.run(bot_token)
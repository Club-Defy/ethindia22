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
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print(f'Disabling default help')
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
async def swap(ctx, from_currency, to_currency, from_amount):
    swap_currency(from_currency, to_currency, from_amount)
    await ctx.send(baseUrl + from_amount + " " + from_currency + " to " + to_currency)

@bot.command()
async def help(ctx):
    cmds = list(bot.all_commands.keys())
    formatted_cmds = '\n'.join([str(elem) for i, elem in enumerate(cmds)])
    embed = discord.Embed(
        title="List of Commands",
        colour=discord.Colour.blue())
    embed.add_field(name='Commands', value=formatted_cmds)

    await ctx.send(embed=embed)

bot.run(bot_token)
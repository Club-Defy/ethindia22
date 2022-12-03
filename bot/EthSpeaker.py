import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

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
    """Adds two numbers together."""
    await ctx.send("this will register users")

@bot.command(description="transfers eth")
async def transfer_eth(ctx, to_address, amount):
    """Adds two numbers together."""
    await ctx.send("this will transfer " + amount + " eth to " + to_address)


@bot.command()
async def transfer_nft(ctx, token_address, to_address, amount):
    """Adds two numbers together."""
    await ctx.send("(nft) this will transfer " + amount + " " + token_address + " to " + to_address)


@bot.command()
async def transfer_erc20(ctx, token_address, to_address, amount):
    """Adds two numbers together."""
    await ctx.send("(erc20) this will transfer " + amount + " " + token_address + " to " + to_address)


@bot.command()
async def swap(ctx, to_address, amount):
    """Adds two numbers together."""
    await ctx.send("this will transfer " + amount + " eth to " + to_address)

bot.run('TOKEN GOES HERE')
import discord
from discord.ext import commands

from config.config import bot_token
from services.bot.register import register_user
from services.bot.swap import swap_erc20_to_erc20, swap_eth_to_erc20, swap_erc20_to_eth
from services.bot.transfer import erc721, erc20, eth, erc20_approve, get_address_from_id
from services.bot.list_nfts import list_erc721

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
async def transfer_eth_discord(ctx, member: discord.User, amount):
    to_address = get_address_from_id(member.id)
    if to_address == "":
        await ctx.send("Discord user not registered with valid ethereum address")
    else:
        await ctx.send(eth(to_address, amount))


@bot.command()
async def transfer_nft(ctx, token_address, to_address, token_id):
    await ctx.send(erc721(to_address, token_address, token_id))


@bot.command()
async def transfer_nft_discord(ctx, token_address, member: discord.User, token_id):
    to_address = get_address_from_id(member.id)
    if to_address == "":
        await ctx.send("Discord user not registered with valid ethereum address")
    else:
        await ctx.send(erc721(to_address, token_address, token_id))


@bot.command()
async def transfer_erc20(ctx, token_address, to_address, amount):
    await ctx.send(erc20(to_address, token_address, amount))


@bot.command()
async def transfer_erc20_discord(ctx, token_address, member: discord.User, amount):
    to_address = get_address_from_id(member.id)
    if to_address == "":
        await ctx.send("Discord user not registered with valid ethereum address")
    else:
        await ctx.send(erc20(to_address, token_address, amount))


@bot.command()
async def swap_eth(ctx, from_amount, to_currency):
    await ctx.send(swap_eth_to_erc20(from_amount, to_currency))


@bot.command()
async def swap_erc20(ctx, from_amount, from_currency):
    await ctx.send(swap_erc20_to_eth(from_amount, from_currency))


@bot.command()
async def swap(ctx, from_amount, from_currency, to_currency):
    await ctx.send(swap_erc20_to_erc20(from_amount, from_currency, to_currency))


@bot.command()
async def approve_erc20(ctx, spender, amount, token_address):
    await ctx.send(erc20_approve(spender, amount, token_address))


@bot.command()
async def help(ctx):
    cmds = list(bot.all_commands.keys())
    formatted_cmds = '\n'.join([str(elem) for i, elem in enumerate(cmds)])
    embed = discord.Embed(
        title="List of Commands",
        colour=discord.Colour.blue())
    embed.add_field(name='Commands', value=formatted_cmds)

    await ctx.send(embed=embed)


@bot.command()
async def list_nfts(ctx, address):
    await ctx.send(embeds=list_erc721(address))


@bot.command()
async def list_my_nfts(ctx):
    address = get_address_from_id(ctx.author.id)
    if address == "":
        await ctx.send("Discord user not registered with valid ethereum address")
    else:
        await ctx.send(embeds=list_erc721(address))


bot.run(bot_token)

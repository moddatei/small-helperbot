import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def help(ctx):
    help_message = (
        "Here are the available commands:\n"
        "/help - Show this help message\n"
        "/ping - Check the bot's latency\n"
        "/ban @user - Ban a user from the server\n"
        "/kick @user - Kick a user from the server"
    )
    await ctx.send(help_message)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency is {round(bot.latency * 1000)}ms')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

bot.run('YOUR_BOT_TOKEN')

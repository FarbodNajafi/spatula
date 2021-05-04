import json
import os
import sqlite3

from discord.ext import commands


class ConnectSQLite:
    """Creates a Sqlite database connection"""

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.conn = sqlite3.connect(self.name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.name:
            self.conn.close()


bot = commands.Bot(command_prefix='>')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def pong(ctx):
    await ctx.send('ping')


@bot.command()
async def rtt(ctx):
    await ctx.send(f'{bot.latency * 1000:.0f}ms')


token: str
with open('secrets.json', 'r') as f:
    _json_ = json.load(f)
    token = _json_['token']

bot.run(token)

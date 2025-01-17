import json
import pathlib

import discord
from discord.ext import commands

import discord_games as games
from discord_games import button_games

bot = commands.Bot(command_prefix='!!', intents=discord.Intents.all())

@bot.command(name='test', aliases=['t'])
@commands.is_owner()
async def test(ctx: commands.Context):

    game = button_games.MemoryGame()
    await game.start(ctx)

if __name__ == '__main__':
    with open(f'{pathlib.Path(__file__).parent}/bot_config.json') as bot_config:
        bot_config = json.load(bot_config)
        token = bot_config['TOKEN']
    
    bot.run(token)
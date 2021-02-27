import random
import os

from discord.ext import commands

bot = commands.Bot(command_prefix="-")


@bot.command()
async def test(context: commands.Context, ability=0, focus=0):
    def roll(): return random.randint(1, 6)
    dice = roll(), roll(), roll()
    doubles = len(set(dice)) != 3
    stunt_points = 0

    if doubles:
        stunt_points = dice[2]

    total = sum(dice, ability + focus)
    name = context.author.display_name
    rolls = f"{dice[0]} :blue_square: + {dice[1]} :blue_square: + {dice[2]} :red_square:"
    await context.send(f"{name}: {rolls} + {ability} + {focus} = **{total} + {stunt_points} SP**")


random.seed(None)
token = os.getenv("TOKEN")
bot.run(token)

import constants
from discord.ext import commands
from profile import Profile


prefix = ',,'
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print('Logged in as {0}'.format(bot.user))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print('Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)


@bot.command()
async def quit(ctx):
    print('Closing bot...')
    await bot.close()


@bot.command()
async def np(ctx):
    print('Adding new profile...')
    profile = Profile(ctx.author)
    await ctx.send(embed=profile)


bot.run(constants.BOT_TOKEN)

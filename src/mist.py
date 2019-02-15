import constants
from discord.ext import commands
from profile import Profile


prefix = ',,'
bot = commands.Bot(command_prefix=prefix)
smashers = {}


@bot.event
async def on_ready():
    for member in bot.get_all_members():
        for role in member.roles:
            if 'shootas' in role.name:
                smashers[member] = Profile(member)
                break
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
async def profile(ctx):
    prof = smashers.get(ctx.author)
    await ctx.channel.send(content='', embed=prof)


@bot.command()
async def switch(ctx, *, content: str):
    prof = smashers.get(ctx.author)
    prof.setSwitchCode(content)


@bot.command()
async def mains(ctx, *, content: str):
    prof = smashers.get(ctx.author)
    prof.setMains(content)


@bot.command()
async def secondaries(ctx, *, content: str):
    prof = smashers.get(ctx.author)
    prof.setSecondaries(content)


bot.run(constants.BOT_TOKEN)

# coding: utf-8

# standard
import configparser
import sys
import traceback

# discord
import discord
from discord.ext import commands


# cogs
EXTENSIONS = [
    'cogs.chat',
]

class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        for extension in EXTENSIONS:
            try:
                await self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

        await self.tree.sync()


def main():

    # read config
    config = configparser.ConfigParser()
    config.read('config.ini')
    discord_token = config['DISCORD']['token']

    # setup intents
    intents = discord.Intents.default()
    intents.members = True

    # run bot
    bot = Bot(
        command_prefix='/',
        help_command=commands.MinimalHelpCommand(),
        intents=intents,
        activity=discord.Activity(type=discord.ActivityType.listening, name='Type /Help'),
        case_insensitive=True)
    bot.run(discord_token)


if __name__ == "__main__":
    main()

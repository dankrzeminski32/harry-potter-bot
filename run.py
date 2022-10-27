import asyncio
import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=".hp ", intents=intents, help_command=None)


async def load_extensions():
    extensions = []

    for filename in extensions:
        await bot.load_extension(filename)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_BOT_TOKEN)


# Main Bot Cycle
asyncio.run(main())

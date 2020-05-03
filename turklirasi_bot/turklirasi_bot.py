#!/usr/bin/env python3.7
import asyncio

from telethon.sync import TelegramClient

from turklirasi_bot import API_KEY, API_HASH, BOT_TOKEN
from turklirasi_bot.modules import ALL_MODULES
from turklirasi_bot.utils.loader import load_modules

BOT = TelegramClient('turklirasi_bot', API_KEY, API_HASH).start(bot_token=BOT_TOKEN)
BOT.parse_mode = 'markdown'
BOT_INFO = {}


def main():
    """Main"""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


async def run():
    """Run the bot."""
    bot_info = await BOT.get_me()
    BOT_INFO.update({'name': bot_info.first_name,
                     'username': bot_info.username, 'id': bot_info.id})
    load_modules(ALL_MODULES, __package__)
    
    async with BOT:
        await BOT.run_until_disconnected()

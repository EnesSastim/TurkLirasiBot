from requests import get

from telethon import events

from turklirasi_bot.turklirasi_bot import BOT

@BOT.on(events.NewMessage(pattern=r'/ip ?(\S*)'))
async def currency(event):
    bot_reply = await event.reply("__Wait...__")
    device = event.pattern_match.group(1)
    ipsw = get(f"https://api.ipsw.me/v4/device/iPhone{device}?type=ipsw").json()
    name = ipsw[f'{"name"}']
    firmwares = ipsw[f'{"firmwares"}']
    version = firmwares[0][f'{"version"}']
    url = firmwares[0][f'{"url"}']
    date = firmwares[0][f'{"releasedate"}'][:10]
    await bot_reply.edit(f"**{name}**\n\n**Latest iOS**: {version}\n\n**Download**:\n{url}\n**{date}**")
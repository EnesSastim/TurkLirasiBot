
from requests import get

from telethon import events

from turklirasi_bot import CURRENCY_API
from turklirasi_bot.turklirasi_bot import BOT

@BOT.on(events.NewMessage(pattern=r'/kur'))
async def currency(event):
    bot_reply = await event.reply("__bakıyorum...__")
    euro = get(f"http://data.fixer.io/api/latest?access_key={CURRENCY_API}").json()
    euro = euro[f'{"rates"}']
    turk = euro[f'{"TRY"}']
    dolar = euro[f'{"USD"}']
    pound = euro[f'{"GBP"}']
    dolar = 1 / dolar
    pound = 1 / pound
    dolar = turk * dolar
    pound = turk * pound
    await bot_reply.edit(f"EUR: {turk}\n"
    f"USD: {'%.8s' % dolar}\n"
    f"GBP: {'%.8s' % pound}")


@BOT.on(events.NewMessage(pattern=r'/cevir (\S*) ?(\S*) ?(\S*)'))
async def currency(event):
    bot_reply = await event.reply("__bakıyorum...__")
    amount = event.pattern_match.group(1)
    currency_from = event.pattern_match.group(3).upper()
    currency_to = event.pattern_match.group(2).upper()
    data = get(f"http://data.fixer.io/api/latest?access_key={CURRENCY_API}").json()
    data = data[f'{"rates"}']
    if currency_from is "EUR":
    	cto = data[f'{currency_to}']
    	result = float(amount) * float(cto)
    	await bot_reply.edit(f"{amount} EUR is:\n`{result:.2f} {currency_to}`")
    elif currency_to is "EUR":
    	cfrom = data[f'{currency_from}']
    	cto = 1 / cfrom
    	result = float(amount) * float(cto)
    	await bot_reply.edit(f"{amount} {currency_from} is:\n`{result:.2f} EUR`")
    else:
    	cfrom = data[f'{currency_from}']
    	cto = data[f'{currency_to}']
    	result = cfrom / cto
    	result = float(amount) * float(result)
    	await bot_reply.edit(f"{amount} {currency_to} is:\n`{result:.2f} {currency_from}`")


from requests import get

from telethon import events

from turklirasi_bot import CURRENCY_API
from turklirasi_bot.turklirasi_bot import BOT

@BOT.on(events.NewMessage(pattern=r'/kur'))
async def currency(event):
    bot_reply = await event.reply("__bakıyorum...__")
    euro = get(f"https://free.currconv.com/api/v7/convert?apiKey={CURRENCY_API}&q=EUR_TRY&compact=ultra").json()
    dolar = get(f"https://free.currconv.com/api/v7/convert?apiKey={CURRENCY_API}&q=USD_TRY&compact=ultra").json()
    pound = get(f"https://free.currconv.com/api/v7/convert?apiKey={CURRENCY_API}&q=GBP_TRY&compact=ultra").json()
    await bot_reply.edit(f"EUR: {euro['EUR_TRY']}\n"
    f"USD: {dolar['USD_TRY']}\n"
    f"GBP: {pound['GBP_TRY']}")


@BOT.on(events.NewMessage(pattern=r'/cevir (\S*) ?(\S*) ?(\S*)'))
async def currency(event):
    bot_reply = await event.reply("__bakıyorum...__")
    amount = event.pattern_match.group(1)
    currency_from = event.pattern_match.group(3).upper()
    currency_to = event.pattern_match.group(2).upper()
    data = get(f"https://free.currconv.com/api/v7/convert?apiKey={CURRENCY_API}&q={currency_from}_{currency_to}&compact=ultra").json()
    result = data[f'{currency_from}_{currency_to}']
    result = float(amount) / float(result)
    result = round(result, 5)
    await bot_reply.edit(f"{amount} {currency_to} is:\n`{result} {currency_from}`")
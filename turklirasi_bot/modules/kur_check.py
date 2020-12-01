import requests
from bs4 import BeautifulSoup

from telethon import events

from turklirasi_bot import CURRENCY_API
from turklirasi_bot.turklirasi_bot import BOT

def get_rate_from_pdov():
    try:
        res = requests.get("http://www.piyasadoviz.com")
        soup = BeautifulSoup(res.text.replace(",", "."), "lxml")
        rates = soup.findAll("li", {"class": "midrow"})
        arrow = soup.findAll("li", {"class": "rrow"})
        return {
            "USD": (rates[4].text),
            "EUR": (rates[10].text),
            "GBP": (rates[16].text)
        }
    except:
        return None

@BOT.on(events.NewMessage(pattern=r'/kur'))
async def currency(event):
    bot_reply = await event.reply("__bakıyorum...__")
    kur = get_rate_from_pdov()
    euro = kur[f'{"EUR"}']
    dolar = kur[f'{"USD"}']
    pound = kur[f'{"GBP"}']
    await bot_reply.edit(f"EUR: {euro}\n"
    f"USD: {dolar}\n"
    f"GBP: {pound}")
from proxygen import ProxyGen
import requests
from telethon import events, Button
import time
from Configs import Config

k =[
  [Button.inline("Https", data="https")],
  [Button.inline("Socks4", data="socks4"), Button.inline("Socks5", data="socks5")],
  [Button.url("Sahibim ⚡", "@SancakBegi")]
  ]


@ProxyGen.on(events.NewMessage(pattern="^[!?/]proxy$"))
async def proxy(event):

    if event.is_group and event.chat_id != Config.LOGS_CHAT:
       await event.reply("**Üzgünüm, sadece PM'de çalışıyorum.**\n__gruptan cikiom hadi bb...__")
       await ProxyGen.delete_dialog(event.chat_id)
       return

    await event.reply(f"**merhaba {event.sender.first_name}**\nBuradan İstediğiniz Proxyleri oluşturabilirsiniz\n__aşağıdaki düğmeye tıklayın __", buttons=k)


@ProxyGen.on(events.CallbackQuery(data="https"))
async def https(event):
    us = (await ProxyGen.get_me()).username
    caption = f"""
<b>‣Generated By - @{event.sender.username}</b>
<b>‣Proxy By - @{us} </b>
<b>© @SancakHack</b>
"""

    k = await event.edit("**oluşturuluyor.**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor..**")
    time.sleep(0.2)
    await event.edit("*oluşturuluyor...**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor....**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor.....**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor......**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor.......**")

    kk = 'https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=5000&country=US&anonymity=elite&ssl=yes'
    re = requests.get(kk, stream = True)
    with open('https_proxies.txt', "wb") as ks:
         for pro in re.iter_content(chunk_size=1024):
           if pro:
              ks.write(pro)
    await k.delete()
    await event.client.send_file(event.chat_id, 'https_proxies.txt', caption=caption, parse_mode="HTML")

@ProxyGen.on(events.CallbackQuery(data="socks4"))
async def socks4(event):
    us = (await ProxyGen.get_me()).username
    caption = f"""
<b>‣Generated By - @{event.sender.username}</b>
<b>‣Proxy By - @{us} </b>
<b>© @SancakHack</b>
"""

    k = await event.edit("**oluşturuluyor.**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor..**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor...**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor....**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor.....**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor......**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor.......**")

    kk = 'https://api.proxyscrape.com?request=getproxies&proxytype=socks4&timeout=5000&country=US&anonymity=elite&ssl=yes'
    re = requests.get(kk, stream = True)
    with open('socks4_proxies.txt', "wb") as ks:
         for pro in re.iter_content(chunk_size=1024):
           if pro:
              ks.write(pro)
    await k.delete()
    await event.client.send_file(event.chat_id, 'socks4_proxies.txt', caption=caption, parse_mode="HTML")

@ProxyGen.on(events.CallbackQuery(data="socks5"))
async def socks5(event):
    us = (await ProxyGen.get_me()).username
    caption = f"""
<b>‣Generated By - @{event.sender.username}</b>
<b>‣Proxy By - @{us} </b>
<b>© @SancakHack</b>
"""

    k = await event.edit("**oluşturuluyor.**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor..**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor...**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor....**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor.....**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor......**")
    time.sleep(0.2)
    await event.edit("**oluşturuluyor.......**")

    kk = 'https://api.proxyscrape.com?request=getproxies&proxytype=socks5&timeout=5000&country=US&anonymity=elite&ssl=yes'
    re = requests.get(kk, stream = True)
    with open('socks5_proxies.txt', "wb") as ks:
         for pro in re.iter_content(chunk_size=1024):
           if pro:
              ks.write(pro)
    await k.delete()
    await event.client.send_file(event.chat_id, 'socks5_proxies.txt', caption=caption, parse_mode="HTML")

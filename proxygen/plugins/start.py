from proxygen import ProxyGen
from telethon import events, Button
from proxygen.plugins.proxy import k
from Configs import Config

btn =[
  [Button.inline("Https", data="https")],
  [Button.inline("Socks4", data="socks4"), Button.inline("Socks5", data="socks5")],
  [Button.url("Sahibim ⚡", "https://t.me/sancakbegi")]
  ]

@ProxyGen.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):

    Text = """
**Selam🇹🇷 {}**
BEN ÜCRETSİZ PROXY ÜRETEN BİR BOTUM
HER TÜRLÜ PROXY ÜRETEBİLİRİM
__Aşağıdaki butona tıklayın!__
""".format(event.sender.first_name)

    if event.is_group and event.chat_id != Config.LOGS_CHAT:
      await event.reply("** gruplarda çalışmıyorum!**\n__görüşürüz sohbetten ayrılıyorum!__")
      await ProxyGen.delete_dialog(event.chat_id)
      return

    await ProxyGen.send_message(Config.LOGS_CHAT, f"botu başlatan [{event.sender.first_name}](tg://user?id={event.sender_id}).")
    await event.reply(Text, buttons=[[Button.inline("Proxy oluştur ", data="proxy")]])

@ProxyGen.on(events.CallbackQuery(data="proxy"))
async def k(event):
    Text = """
**Merhaba {}
Oluşturmak istediğiniz proxy'leri seçin:**
""".format(event.sender.first_name)
    await event.edit(Text, buttons=btn)

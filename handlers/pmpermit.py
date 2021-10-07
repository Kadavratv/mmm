from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhaba, Bu bir müzik asistanı hizmetidir.\n\n ❗️ kurallar:\n   - Sohbete izin yok\n   - İstenmeyen postaya izin verilmez \n\n 🚨 **USERBOT GRUBUNUZA KATILAMAZSA GRUP DAVETİ BAĞLANTISI VEYA KULLANICI ADI GÖNDERİNİZ.**\n\n ⚠️ DİKKAT: Burada bir mesaj gönderiyorsunuz. Yöneticinin iletinizi göreceği anlamına gelir. Msj bırakabilir veya kısa sorular sorabilirsiniz.\n  - Bu kullanıcıyı gizli gruplara eklemeyin. Userbot gizli grublara /asistan komutu ile gelemeyebilir.\n   - Özel bilgileri burada paylaşmayın\n\n")
  return                        
 

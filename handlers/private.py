from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Ben **{bn}** !!
Grubunuzda Müzik Çalmak İçin Çok İyi Ve Açık Kaynaklı Bir Bottur:
🔥 /oynat - yanıtlanan ses dosyasını veya YouTube videosunu link.__ aracılığıyla __oynatılır
🔥 /durdur - Sesli Sohbet Music.__ __Durdurur
🔥 /devam - sesli sohbet Music.__ __Devam ettirir
🔥 /atla - Geçerli Ses Atlanır.__ Çalan Müzik __atlanır
🔥 /son - Sırayı __Temizler ve Sesli Sohbet Müziklerin listesini kaldırır.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💖 Asistan", url="https://t.me/Movingmusicasistan"

                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url="https://t.me/VenomGrub"
                    ),                    
                    InlineKeyboardButton(
                        "🌀 Repo", url="https://t.me/Sohbetdestek" 
                    ), 
                ]
            ]
        )
    )
    


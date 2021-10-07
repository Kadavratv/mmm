from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""Ben **{bn}** !!
Grubunuzda Müzik Çalmak İçin Tasarlandım, Bana Mp3 Formatında Şarkıları Veriniz. Developed by [MahoBey](https://t.me/Mahoaga) Komutlarım Aşağıdaki Gibidir:
🔥 /oynat - yanıtlanan ses dosyasını veya YouTube videosunu link.__ aracılığıyla __oynatılır
🔥 /durdur - Sesli Sohbet Music.__ __Durdurur
🔥 /devam - sesli sohbet Music.__ __Devam ettirir
🔥 /atla - Geçerli Ses Atlanır.__ Çalan Müzik __atlanır
🔥 /son - Sırayı __Temizler ve Sesli Sohbet Müziklerin listesini kaldırır.__
💡 /asistan - Userbot Grubunuza Katılır.
💡 /asistandefol - Userbot Grubunuzdan Ayrılır. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💖 Asistan", url="https://t.me/movingmusic"

                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url="https://t.me/sohbetdestek"
                    ),                    
                    InlineKeyboardButton(
                        "🌀 Repo", url="https://github.com/Mehmetbaba06" 
                    ), 
                ]
            ]
        )
    )
    


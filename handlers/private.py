from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/NGSPzanu8UhefmjbA",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nmən {bot}!\nSesli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [❥︎𝙊𝙬𝙉𝙚𝙍❦︎ 🎙️](https://t.me/KoRoLeVa_97).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrupa Ekle ❱ ➕", url=f"https://t.me/Karabakh_Music_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Karabachassistent"
                    ),
                    InlineKeyboardButton(
                        "💬 Söhbət", url="https://t.me/KMmafiaa"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmirlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿🇩🇪", url=f"https://t.me/Chinara_92"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 Herkes için komutlar", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Adminler için komutlar", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Yaradıcı", url="https://t.me/KoRoLeVa97_bot")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Herkes için Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Yönetici Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Yaradıcı", url="https://t.me/KoRoLeVa97_bot")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Yaradıcı", url="https://t.me/KoRoLeVa97_bot")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler üçün komut menysu 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Yaradıcı", url="https://t.me/KoRoLeVa97_bot")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSesli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [❥︎𝙊𝙬𝙉𝙚𝙍❦︎🎙️](https://t.me/KoRoLeVa_97).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrupa Ekle ❱ ➕", url=f"https://t.me/Karabakh_Music_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Karabachassistent"
                    ),
                    InlineKeyboardButton(
                        "💬 Söhbət", url="https://t.me/https://t.me/KMmafiaa"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Ayarlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🇦🇿🇩🇪", url=f"https://t.me/Chinara_92"
                    )
                ]
                
           ]
        ),
    )

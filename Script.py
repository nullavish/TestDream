class script(object):
    START_TXT = """<b>Hey {}, {}</b> <tg-emoji emoji-id="6321173922398084063">⭐</tg-emoji>
<b>Welcome to </b><tg-emoji emoji-id="5866355487255039002">🚀</tg-emoji><b> No 1 Movies Webseries OTT Search Engine</b><tg-emoji emoji-id="6323306309236038626">🍿</tg-emoji><tg-emoji emoji-id="6321320290588565035">🤖</tg-emoji>

<tg-emoji emoji-id="6321325964240362008">❗️</tg-emoji><b>ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ʙᴏᴛ</b>
<tg-emoji emoji-id="6321325964240362008">❗️</tg-emoji><b>ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀʟʟ ᴍᴏᴠɪᴇs ᴀɴᴅ ᴡᴇʙ sᴇʀɪᴇs</b>

<tg-emoji emoji-id="5258396243666681152">🔎</tg-emoji><i>Just send correct Spelling</i><tg-emoji emoji-id="5454370584861384827">🔍</tg-emoji>

<tg-emoji emoji-id="6321228227964574392">ℹ️</tg-emoji> <b>Jo bhi Movie/Webseries dekhna ho uska naam ENGLISH me naam bheje </b><tg-emoji emoji-id="5371081166013078244">🍿</tg-emoji>

<tg-emoji emoji-id="6321085085294534327">❤️</tg-emoji><b>जो भी मूवी/ वेबसरीज देखना हो english में उसका नाम भेजे</b>
<tg-emoji emoji-id="6323322084650916948">🟩</tg-emoji><tg-emoji emoji-id="6323498813965213364">🟩</tg-emoji><tg-emoji emoji-id="6320925046223150523">🟩</tg-emoji><tg-emoji emoji-id="6320951799574436533">🟩</tg-emoji><tg-emoji emoji-id="6323445633680154253">🟩</tg-emoji><tg-emoji emoji-id="6321303986892708556">🟩</tg-emoji><tg-emoji emoji-id="6323535943957487433">🟩</tg-emoji><tg-emoji emoji-id="6323113439434644381">🟩</tg-emoji>
<blockquote><tg-emoji emoji-id="6309872055261077639">🫙</tg-emoji> <b>If you see ads below the bot's name, please click👆</b><tg-emoji emoji-id="6311998609533443577">❌</tg-emoji> <b>to cancel</b></blockquote>
<tg-emoji emoji-id="5208851133027596379">⬆️</tg-emoji><tg-emoji emoji-id="5208449291592413299">↗️</tg-emoji><tg-emoji emoji-id="5208705232988548657">↘️</tg-emoji><tg-emoji emoji-id="5208473059941431366">⬇️</tg-emoji><tg-emoji emoji-id="5208634091150258712">↙️</tg-emoji><tg-emoji emoji-id="5206382909811866989">⬅️</tg-emoji><tg-emoji emoji-id="5208571109749832230">↖️</tg-emoji><tg-emoji emoji-id="5206558651283684480">➡️</tg-emoji>"""

    GSTART_TXT = """<b>🚩 ᴊᴀɪ ꜱʜʀɪ ʀᴀᴍ 🚩</b>

<b>ʜᴇʏ {},</b>

<b>🤖 ɪ ᴀᴍ <a href=https://t.me/{}>{}</a>, ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.</b>"""

    
    HELP_TXT = """<b>
    
✨ ʜᴏᴡ ᴛᴏ ʀᴇǫᴜᴇꜱᴛ ᴅʀᴀᴍᴀꜱ & ᴍᴏᴠɪᴇꜱ ✨  

1️⃣ ꜱᴇᴀʀᴄʜ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ᴏɴ ɢᴏᴏɢʟᴇ.  
2️⃣ ꜱᴇɴᴅ ᴛʜᴇ ɴᴀᴍᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.  
3️⃣ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ:  

📌 ꜰᴏʀ ꜱᴇʀɪᴇꜱ:  
➤ ᴅʀᴀᴍᴀ ɴᴀᴍᴇ + S01 (ꜰᴏʀ ꜱᴇᴀꜱᴏɴ 1, ᴄʜᴀɴɢᴇ ꜰᴏʀ ᴏᴛʜᴇʀꜱ)  

📌 ꜰᴏʀ ʜɪɴᴅɪ ᴅʀᴀᴍᴀꜱ:  
➤ ᴅʀᴀᴍᴀ ɴᴀᴍᴇ + ʜɪɴᴅɪ  

📌 ꜰᴏʀ ᴍᴏᴠɪᴇꜱ:  
➤ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ + ʏᴇᴀʀ (ᴇx: ᴊᴏᴋᴇʀ 2019)  

🚀 ꜰᴏʟʟᴏᴡ ᴛʜᴇꜱᴇ ꜱᴛᴇᴘꜱ!
</b>"""

    ABOUT_TXT = """<b>╭────[ ᴍʏ ᴅᴇᴛᴀɪʟs ]────⍟
├⍟ Mʏ Nᴀᴍᴇ : <a href=https://t.me/{}>{}</a>
├⍟ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href={}>ᴏᴡɴᴇʀ</a> 
├⍟ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
├⍟ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 𝟹</a> 
├⍟ Dᴀᴛᴀʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
├⍟ Bᴏᴛ Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a> 
├⍟ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]
╰───────────────⍟</b>"""
    RESTART_TXT = """
<b>{} Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code> v1.4 [ Sᴛᴀʙʟᴇ ]</code>
</b>"""

    MULTI_STATUS_TXT = """<b>🗃ᴜsᴇʀs ᴅᴀᴛᴀʙᴀsᴇ 🗃

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - {0}
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - {1}
» ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs - {2}

📤 ᴅᴀᴛᴀʙᴀsᴇ 𝟷 📤

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - {3}
» ᴅʙ sᴛᴏʀᴀɢᴇ - {4}
» ᴄʟᴜsᴛᴇʀ sᴛᴏʀᴀɢᴇ - {5} / 512.00 MB
» ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ - {6}

📥 ᴅᴀᴛᴀʙᴀsᴇ 𝟸 📥

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - {7}
» ᴅʙ sᴛᴏʀᴀɢᴇ - {8}
» ᴄʟᴜsᴛᴇʀ sᴛᴏʀᴀɢᴇ - {9} / 512.00 MB
» ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ - {10}

🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖

» ᴜᴘᴛɪᴍᴇ - {11}
» ʀᴀᴍ - {12}%
» ᴄᴘᴜ - {13}%

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - {14}</b>"""

    STATUS_TXT = """<b>🗃ᴜsᴇʀs ᴅᴀᴛᴀʙᴀsᴇ 🗃

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - {0}
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - {1}
» ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs - {2}

📤 ꜰɪʟᴇs ᴅᴀᴛᴀʙᴀsᴇ 📤

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - {3}
» ᴅʙ sᴛᴏʀᴀɢᴇ - {4}
» ᴄʟᴜsᴛᴇʀ sᴛᴏʀᴀɢᴇ - {5} / 512.00 MB
» ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ - {6}

🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖

» ᴜᴘᴛɪᴍᴇ - {7}
» ʀᴀᴍ - {8}%
» ᴄᴘᴜ - {9}%</b>"""

    LOG_TEXT_G = """#NewGroup
    
Gʀᴏᴜᴘ = {}
Iᴅ = <code>{}</code>
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}
"""

    LOG_TEXT_P = """#NewUser
    
Iᴅ - <code>{}</code>
Nᴀᴍᴇ - {}
"""
    NT_ADMIN_ALRT_TXT = """‼️ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ ‼️"""

    NT_ALRT_TXT = """Not Yours!"""
    
    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,
ʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    PRE_STREAM = """🔒 ᴛʜɪs ꜰᴇᴀᴛᴜʀᴇ ɪs ᴏɴʟʏ ꜰᴏʀ 🏅 ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs

✨ ᴜɴʟᴏᴄᴋ ᴇxᴄʟᴜsɪᴠᴇ ᴄᴏɴᴛᴇɴᴛ ᴀɴᴅ ꜰᴇᴀᴛᴜʀᴇs  
💳 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ"""

    PRE_STREAM_ALERT = """⚠️ ᴘʀᴇᴍɪᴜᴍ ᴄᴏɴᴛᴇɴᴛ ❗  
🔓 ᴜɴʟᴏᴄᴋ ɪᴛ ʙʏ ᴜᴘɢʀᴀᴅɪɴɢ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ"""

    CUDNT_FND = SPELLING_ERROR_TXT = """<b>‼️ ꜱᴘᴇʟʟɪɴɢ ᴍɪꜱᴛᴀᴋᴇ ʙʀᴏ!</b>  
<b>😊 ɴᴏ ᴡᴏʀʀɪᴇꜱ — ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴏɴᴇ ʙᴇʟᴏᴡ 👇</b>

<blockquote>👇 नीचे दिए गए विकल्पों में से movie के नाम की सही spelling चुनें</blockquote>"""


    DEL_MSG = """⚠️ ᴛʜɪꜱ ᴍᴏᴠɪᴇ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ <b><u><code>{}</code></u></b>

<blockquote expandable><b><i>ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ & ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ</i></b></blockquote>"""


    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

📝 ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

⚜️ ᴇxᴀᴍᴘʟᴇ : Jawan or Jawan 2023 

📝 ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

⚜️ ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""
    
    MVE_NT_FND = NOT_FOUND_TXT = """<b>😌 ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.</b>

<blockquote>😌 यह ᴍᴏᴠɪᴇ मुझे ᴍᴇʀᴇ ᴅᴀᴛᴀʙᴀꜱᴇ में नहीं मिली।</blockquote>"""

    ALREADY_AVAILABLE_TXT = """<b>ʜᴇʏ {},
    
ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ ✅

<blockquote>📂 ꜰɪʟᴇꜱ ꜰᴏᴜɴᴅ : {}
🔍 ꜱᴇᴀʀᴄʜ : <code>{}</code></blockquote>

‼️ ᴛʜɪs ɪs ᴀ <u>sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ</u> sᴏ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ ғɪʟᴇs ғʀᴏᴍ ʜᴇʀᴇ...

📝 ꜱᴇᴀʀᴄʜ ʜᴇʀᴇ : 👇</b>"""

    MAINTENANCE_TXT = """<b>🛑 ꜱᴇʀᴠɪᴄᴇ ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ 🛑</b>

<b>ʜᴇʏ {}, ᴡᴇ ᴀʀᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴜᴘᴅᴀᴛɪɴɢ ᴏᴜʀ ꜱʏꜱᴛᴇᴍꜱ ᴛᴏ ꜱᴇʀᴠᴇ ʏᴏᴜ ʙᴇᴛᴛᴇʀ. ᴛʜᴇ ꜱᴇʀᴠɪᴄᴇ ɪꜱ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ ᴅɪꜱᴀʙʟᴇᴅ.</b>

<blockquote>ᴛʜᴇ ꜱᴇʀᴠɪᴄᴇ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ. ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ. 😊</blockquote>"""

    PM_SEARCH_DISABLED_TXT = """<b>🙋 ʜᴇʏ {} 😍,

ʏᴏᴜ ᴄᴀɴ sᴇᴀʀᴄʜ ғᴏʀ ᴍᴏᴠɪᴇs ᴏɴʟʏ ᴏɴ ᴏᴜʀ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ᴍᴏᴠɪᴇs ᴏɴ ᴅɪʀᴇᴄᴛ ʙᴏᴛ. ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ sᴇᴀʀᴄʜ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴍᴏᴠɪᴇ ᴛʜᴇʀᴇ 👇

<blockquote>आप केवल हमारे ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ पर ही ᴍᴏᴠɪᴇ sᴇᴀʀᴄʜ कर सकते हो । 

आपको ᴅɪʀᴇᴄᴛ ʙᴏᴛ पर ᴍᴏᴠɪᴇ sᴇᴀʀᴄʜ करने की ᴘᴇʀᴍɪssɪᴏɴ नहीं है कृपया नीचे दिए गए ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ वाले ʙᴜᴛᴛᴏɴ पर क्लिक करके हमारे ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ को ᴊᴏɪɴ करें और वहां पर अपनी मनपसंद ᴍᴏᴠɪᴇ sᴇᴀʀᴄʜ सर्च करें ।</blockquote></b>"""

    PM_LOG_TXT = """<b>#𝐏𝐌_𝐌𝐒𝐆

👤 ɴᴀᴍᴇ : {}
🆔 ɪᴅ : <code>{}</code>
💬 ᴍᴇssᴀɢᴇ : {}</b>"""

    LINK_EXPIRED_TXT = """<b>‼️ ʟɪɴᴋ ᴇxᴘɪʀᴇᴅ, ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ...</b>"""

    REFER_TXT = """<b>ʜᴀʏ, ʏᴏᴜʀ ʀᴇꜰᴇʀ ʟɪɴᴋ:
    
<code>https://t.me/{}?start=reff_{}</code>

<blockquote>sʜᴀʀᴇ ᴛʜɪs ʟɪɴᴋ ᴡɪᴛʜ ʏᴏᴜʀ ғʀɪᴇɴᴅs. ᴇᴀᴄʜ ᴛɪᴍᴇ ᴛʜᴇʏ ᴊᴏɪɴ, ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ 10 ʀᴇꜰꜰᴇʀᴀʟ ᴘᴏɪɴᴛs ᴀɴᴅ ᴀꜰᴛᴇʀ 100 ᴘᴏɪɴᴛs ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ 1 ᴍᴏɴᴛʜ ᴘʀᴇᴍɪᴜᴍ sᴜʙsᴄʀɪᴘᴛɪᴏɴ.</blockquote></b>"""

    REFER_SELF_ALRT = """<b>Hᴇʏ Dᴜᴅᴇ, Yᴏᴜ Cᴀɴ'ᴛ Rᴇғᴇʀ Yᴏᴜʀsᴇʟғ 🤣!
    
<blockquote>sʜᴀʀᴇ ʟɪɴᴋ ʏᴏᴜʀ ғʀɪᴇɴᴅ ᴀɴᴅ ɢᴇᴛ 10 ʀᴇғᴇʀʀᴀʟ ᴘᴏɪɴᴛ ɪғ ʏᴏᴜ ᴀʀᴇ ᴄᴏʟʟᴇᴄᴛɪɴɢ 100 ʀᴇғᴇʀʀᴀʟ ᴘᴏɪɴᴛs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ 1 ᴍᴏɴᴛʜ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀsʜɪᴘ.</blockquote></b>"""

    REFER_ALREADY_ALRT = """<b>ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴀʟʀᴇᴀᴅʏ ɪɴᴠɪᴛᴇᴅ ❗</b>"""

    REFER_ALREADY_JOINED_ALRT = """<b>‼️ ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ ᴀʟʀᴇᴀᴅʏ ɪɴᴠɪᴛᴇᴅ ᴏʀ ᴊᴏɪɴᴇᴅ</b>"""

    REFER_CONGRATS_ALRT = """<b>🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs! ʏᴏᴜ ᴡᴏɴ 10 ʀᴇꜰᴇʀʀᴀʟ ᴘᴏɪɴᴛ ʙᴇᴄᴀᴜsᴇ ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ sᴜᴄᴄᴇssꜰᴜʟʟʏ ɪɴᴠɪᴛᴇᴅ ☞ {}!</b>"""

    REFER_INVITED_ALRT = """<b>ʏᴏᴜ ʜᴀᴠᴇ ʙᴇᴇɴ sᴜᴄᴄᴇssꜰᴜʟʟʏ ɪɴᴠɪᴛᴇᴅ ʙʏ {}!</b>"""

    FORCESUB_TXT = """<b>👋 ʜᴇʟʟᴏ {}

🛑 ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.

<blockquote>👉 ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.</blockquote></b>"""

    BOT_ADD_TXT = """<b>ᴛʜᴀɴᴋʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {} ❣️

<blockquote>ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs & ᴅᴏᴜʙᴛs ᴀʙᴏᴜᴛ ᴜsɪɴɢ ᴍᴇ ᴄᴏɴᴛᴀᴄᴛ sᴜᴘᴘᴏʀᴛ.</blockquote></b>"""

    CHAT_RESTRICTED_TXT = """<b>ᴄʜᴀᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ 🐞

<blockquote>ᴍʏ ᴀᴅᴍɪɴꜱ ʜᴀꜱ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ ᴍᴇ ꜰʀᴏᴍ ᴡᴏʀᴋɪɴɢ ʜᴇʀᴇ ! ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ɪᴛ ᴄᴏɴᴛᴀᴄᴛ ꜱᴜᴘᴘᴏʀᴛ.</blockquote></b>"""

    LEAVE_CHAT_TXT = """<b>ʜᴇʟʟᴏ ꜰʀɪᴇɴᴅꜱ, 

<blockquote>ᴍʏ ᴀᴅᴍɪɴ ʜᴀꜱ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ, ꜱᴏ ɪ ʜᴀᴠᴇ ᴛᴏ ɢᴏ ! ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴄᴏɴᴛᴀᴄᴛ ꜱᴜᴘᴘᴏʀᴛ.</blockquote></b>"""

    SEARCHING_TXT = """<b><i> 𝖲𝖾𝖺𝗋𝖼𝗁𝗂𝗇𝗀 𝖿ᴏʀ '{}' 🔎</i></b>"""

    TOP_ALRT_MSG = """ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ ǫᴜᴇʀʏ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    MELCOW_ENG = """<b>👋 ʜᴇʏ {},\n\n🍁 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ\n🌟 {} \n\n🔍 ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ 🔎\n\n⚠️ ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ 👇</b>"""
    
    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 
</b>"""

    DREAMXBOTZ_DONATION = DONATE_TXT = """<b>👋 ʜᴇʏ {},</b>

<blockquote>💖 <b>ᴘʟᴇᴀꜱᴇ ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ</b></blockquote>

<b>🔧 ᴛᴏ ᴋᴇᴇᴘ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ᴀʟɪᴠᴇ, ᴀᴅᴅ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇꜱ & ᴜᴘʟᴏᴀᴅ ʙᴇꜱᴛ ᴍᴏᴠɪᴇꜱ/ᴡᴇʙꜱᴇʀɪᴇꜱ ɴᴏɴ-ꜱᴛᴏᴘ ɪɴ ʜɪɢʜ Qᴜᴀʟɪᴛʏ, ᴡᴇ ɴᴇᴇᴅ ʏᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ.
ɪᴛ ʜᴇʟᴘꜱ ᴜꜱ ᴘᴀʏ ꜰᴏʀ ʜᴇʀᴏᴋᴜ & ꜱᴇʀᴠᴇʀ ʀᴇꜱᴏᴜʀᴄᴇꜱ.</b>

<b>🌝 ʏᴏᴜ ᴄᴀɴ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ʏᴏᴜ ʜᴀᴠᴇ.</b>

<blockquote>🎉 <b>ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴ ᴍᴇᴛʜᴏᴅ 👇</b></blockquote>

➤ 📷 Qʀ ᴄᴏᴅᴇ → <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>  
➤ 💸 ᴜᴘɪ ɪᴅ → <code>{}</code>

‼️ <b>ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴅᴏɴᴀᴛɪɴɢ.</b>"""




    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""
    
    CAPTION = """<b><a href="https://t.me/dreamxbotz">{file_name}</a></b>\n\n<b>⚜️ Powered By : <a href="https://t.me/dreamxbotz">[ ᴅʀᴇᴀᴍxʙᴏᴛᴢ ]</a></b>"""

    
    MOVIE_UPDATE_NOTIFY_TXT = """
</b><a href={poster_url}>📥</a><a href={imdb_url}>New {tag} Added</a></b>

<blockquote>✨ ᴛɪᴛʟᴇ : <code>{filename} {year}</code>

🎭 ɢᴇɴʀᴇs : <b>{genres}</b>
📺 ᴏᴛᴛ        : <b>{ott}</b>
🎞️ ǫᴜᴀʟɪᴛʏ : <b>{quality}</b>
🎧 ᴀᴜᴅɪᴏ    : <b>{language}</b>
🔥 ʀᴀᴛɪɴɢ   : <b>{rating}</b>
{episodes}
</blockquote>

🔍 <b>Sᴇᴀʀᴄʜ →</b> {search_link}
"""


    IMDB_TEMPLATE_TXT = """<b><a href={url}>{title} (<a href={url}/releaseinfo>{year}</a>)

ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a>
ɢᴇɴʀᴇ : {genres}
ᴀᴜᴅɪᴏ : {languages}

sʜᴏᴡɴ ɪɴ : {remaining_seconds} <i>sᴇᴄ</i>⚡️
<b>ʀᴇǫ ʙʏ : {message.from_user.mention}</b>"""

    LOGO = r"""
    ██████╗░██████╗░███████╗░█████╗░███╗░░░███╗██╗░░██╗██████╗░░█████╗░████████╗███████╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗░████║╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝╚════██║
    ██║░░██║██████╔╝█████╗░░███████║██╔████╔██║░╚███╔╝░██████╦╝██║░░██║░░░██║░░░░░███╔═╝
    ██║░░██║██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║░██╔██╗░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
    ██████╔╝██║░░██║███████╗██║░░██║██║░╚═╝░██║██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░███████╗
    ╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝

    𝙱𝙾𝚃 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈....
    """


    #PLANS



    PREMIUM_TEXT = """<blockquote><tg-emoji emoji-id="6098427834571694679">⭐</tg-emoji> <b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</b></blockquote>

<tg-emoji emoji-id="6312090079451947005">🫙</tg-emoji> 07 ᴅᴀʏꜱ - 10 ₹  / 10 star<tg-emoji emoji-id="6055634884968320993">⭐</tg-emoji>
<tg-emoji emoji-id="6312090079451947005">🫙</tg-emoji> 15 ᴅᴀʏꜱ - 20 ₹  / 20 star<tg-emoji emoji-id="6055634884968320993">⭐</tg-emoji>
<tg-emoji emoji-id="6312090079451947005">🫙</tg-emoji> 30 ᴅᴀʏꜱ - 40 ₹  / 40 star<tg-emoji emoji-id="6055634884968320993">⭐</tg-emoji>
<tg-emoji emoji-id="6312090079451947005">🫙</tg-emoji> 45 ᴅᴀʏꜱ - 55 ₹  / 55 star<tg-emoji emoji-id="6055634884968320993">⭐</tg-emoji>
<tg-emoji emoji-id="6312090079451947005">🫙</tg-emoji> 60 ᴅᴀʏꜱ - 75 ₹  / 75 star<tg-emoji emoji-id="6055634884968320993">⭐</tg-emoji>

•─────•─────────•─────•
🏷️  

<tg-emoji emoji-id="6312088344285159086">🪪</tg-emoji> ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ

<blockquote><tg-emoji emoji-id="5399884238902277207">❄️</tg-emoji> After sending the screenshot, please give us some time to add you to the premium list</blockquote>"""

    PREMIUM_STAR_TEXT = """<blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: <b><tg-emoji emoji-id="5866355487255039002">🚀</tg-emoji>ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ <tg-emoji emoji-id="6098427834571694679">⭐</tg-emoji></b></blockquote>

ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴇʀᴠɪᴄᴇ ᴜꜱɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛᴀʀꜱ<tg-emoji emoji-id="6055634884968320993">⭐</tg-emoji>  

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ᴛᴀᴋᴇ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀɴᴅ ꜱᴇɴᴅ ɪᴛ ᴛᴏ - 

ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ᴀᴍᴏᴜɴᴛ ᴀɴᴅ ᴘᴜʀᴄʜᴀꜱᴇ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ <tg-emoji emoji-id="5470177992950946662">👇</tg-emoji>"""

    PREMIUM_UPI_TEXT = """<blockquote>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ: ᴜᴘɪ <b><tg-emoji emoji-id="6334433976794483776">🔥</tg-emoji></b></blockquote>

ʏᴏᴜ ᴄᴀɴ ᴘᴜʀᴄʜᴀꜱᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜʀᴏᴜɢʜ ᴜᴘɪ , ɴᴇᴛ ʙᴀɴᴋɪɴɢ. <tg-emoji emoji-id="6334435815040486841">😈</tg-emoji><tg-emoji emoji-id="6334433976794483776">🔥</tg-emoji><tg-emoji emoji-id="6334418068235620318">😏</tg-emoji><tg-emoji emoji-id="6334400411625065971">😨</tg-emoji>

💳 ᴜᴘɪ ɪᴅ - <code>{}</code>

<tg-emoji emoji-id="5870483144100023800">📄</tg-emoji> <b>ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ</b>

<blockquote><tg-emoji emoji-id="5399884238902277207">❄️</tg-emoji> After sending the screenshot, please give us some time to add you to the premium list</blockquote>"""


    PREMIUM_END_TEXT = """<b>ʜᴇʏ {},</b>

<b>ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ.</b>  
<b>ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴜsɪɴɢ ᴏᴜʀ sᴇʀᴠɪᴄᴇ 😊</b>  
<b>ᴄʟɪᴄᴋ ᴏɴ /plan ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴs.</b>

<blockquote>ᴀᴀᴘᴋᴀ <b>ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss</b> ʜᴀᴛᴀ ᴅɪʏᴀ ɢᴀʏᴀ ʜᴀɪ।  
ʜᴀᴍᴀʀɪ sᴇᴠᴀ ᴋᴀ ᴜᴘʏᴏɢ ᴋᴀʀɴᴇ ᴋᴇ ʟɪʏᴇ ᴅʜᴀɴʏᴀᴠᴀᴀᴅ 🥳  
ʜᴀᴍᴀʀɪ ᴀɴʏᴀ ʏᴏᴊɴᴀᴏɴ ᴋɪ ᴊᴀᴀɴᴄʜ ᴋᴀʀɴᴇ ᴋᴇ ʟɪʏᴇ <b>/plan</b> ᴘᴀʀ ᴋʟɪᴄᴋ ᴋᴀʀᴇɪɴ।</blockquote>
"""

    
    BPREMIUM_TXT = """<b><tg-emoji emoji-id="5399861595834692622">☪️</tg-emoji></b><b> PREMIUM FEATURES</b><tg-emoji emoji-id="5381930481036045779">❤️</tg-emoji>
<tg-emoji emoji-id="5208851133027596379">⬆️</tg-emoji><tg-emoji emoji-id="5208449291592413299">↗️</tg-emoji><tg-emoji emoji-id="5208705232988548657">↘️</tg-emoji><tg-emoji emoji-id="5208473059941431366">⬇️</tg-emoji><tg-emoji emoji-id="5208634091150258712">↙️</tg-emoji><tg-emoji emoji-id="5206382909811866989">⬅️</tg-emoji><tg-emoji emoji-id="5208571109749832230">↖️</tg-emoji><tg-emoji emoji-id="5206558651283684480">➡️</tg-emoji>
<tg-emoji emoji-id="5314700597742566172">✍️</tg-emoji> No need to verify
<tg-emoji emoji-id="6087126697579127217">🔗</tg-emoji> No need to open links
<tg-emoji emoji-id="5258389041006518073">📂</tg-emoji> Direct files
<tg-emoji emoji-id="5379891191909196943">❤️</tg-emoji> Ad-free experience
<tg-emoji emoji-id="6086687528583176680">⏫</tg-emoji> High-speed download links
<tg-emoji emoji-id="6311966242659902613">🔄</tg-emoji> Multi-player streaming links
<tg-emoji emoji-id="5873146865637133757">🎤</tg-emoji> Unlimited movies &amp; series
<tg-emoji emoji-id="5247176827016847212">📞</tg-emoji> Full admin support
<tg-emoji emoji-id="5258093637450866522">🤖</tg-emoji> Requests will be completed within 1 hour [if available]

<blockquote>You can get premium by referring your friends, or you can buy the premium service</blockquote>
•─────•─────────•─────•
<tg-emoji emoji-id="6312307035429937116">❗️</tg-emoji> <b>Check your active plan</b> /myplan

<blockquote><tg-emoji emoji-id="5399884238902277207">❄️</tg-emoji> After sending the screenshot, please give us some time to add you to the premium list</blockquote>"""  


    PREPLANS_TXT = PREMIUM_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎖️ <b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴꜱ</b></blockquote>

◉ 07 ᴅᴀʏꜱ - 10 ₹  
◉ 15 ᴅᴀʏꜱ - 20 ₹  
◉ 30 ᴅᴀʏꜱ - 40 ₹  
◉ 45 ᴅᴀʏꜱ - 55 ₹  
◉ 60 ᴅᴀʏꜱ - 75 ₹  

•─────•─────────•─────•

🏷️ <b>ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅꜱ</b>

💸 ᴜᴘɪ ɪᴅ → <code>{}</code>  
📷 ǫʀ ᴄᴏᴅᴇ → <a href='{}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>  

🧾 ᴘᴀʏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ!

‼️ ᴍᴜꜱᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ᴀꜰᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.  
‼️ ᴀꜰᴛᴇʀ ꜱᴇɴᴅɪɴɢ ᴀ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ, ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.

💎 ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ → /myplan</b>"""




    SOURCE_TXT ="""<b>ՏOᑌᖇᑕᗴ ᑕOᗪᗴ : 👇 </b>

This Is An Open-Source Project. You Can Use It Freely, But Selling The Source Code Is Strictly Prohibited.\n
ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʜᴇʀᴇ ◉› :<a href=https://github.com/DreamXBotz/Auto_Filter_Bot.git>𝓓𝓻𝓮𝓪𝓶𝔁𝓑𝓸𝓽𝔃</a>\n """


    
    VERIFICATION_TEXT = """<i>ʜᴇʏ</i><tg-emoji emoji-id="5247133031235329609">👋</tg-emoji><i> {},</i>

<tg-emoji emoji-id="5397976749436842796">⚡</tg-emoji><i> ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ &amp; ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ</i><tg-emoji emoji-id="6086880518643656697">✅</tg-emoji>
<tg-emoji emoji-id="5397976749436842796">⚡</tg-emoji><i> आप आज सत्यापित नहीं हैं, कृपया सत्यापित करें पर क्लिक करें और अगले सत्यापन तक असीमित उपयोग पाएं</i><tg-emoji emoji-id="6086880518643656697">✅</tg-emoji>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 <tg-emoji emoji-id="5427181942934088912">💬</tg-emoji>

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji>
अगर आपको डायरेक्ट फाइल्स चाहिए तो आप प्रीमियम सेवा ले सकते हैं (सत्यापन की आवश्यकता नहीं)<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji></blockquote>

<b><tg-emoji emoji-id="6309670561165352554">📹</tg-emoji> Watch tutorials / ट्यूटोरियल देखें <tg-emoji emoji-id="6088947806662303266">🚫</tg-emoji></b>"""
    

    VERIFY_COMPLETE_TEXT = """<b><i>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    SECOND_VERIFICATION_TEXT = """<i>ʜᴇʏ</i><tg-emoji emoji-id="5247133031235329609">👋</tg-emoji><i> {},</i>

<tg-emoji emoji-id="5397976749436842796">⚡</tg-emoji><i> ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ &amp; ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ</i><tg-emoji emoji-id="6086880518643656697">✅</tg-emoji>
<tg-emoji emoji-id="5397976749436842796">⚡</tg-emoji><i> आप आज सत्यापित नहीं हैं, कृपया सत्यापित करें पर क्लिक करें और अगले सत्यापन तक असीमित उपयोग पाएं</i><tg-emoji emoji-id="6086880518643656697">✅</tg-emoji>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3 <tg-emoji emoji-id="5427181942934088912">💬</tg-emoji>

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji>
अगर आपको डायरेक्ट फाइल्स चाहिए तो आप प्रीमियम सेवा ले सकते हैं (सत्यापन की आवश्यकता नहीं)<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji></blockquote>

<b><tg-emoji emoji-id="6309670561165352554">📹</tg-emoji> Watch tutorials / ट्यूटोरियल देखें <tg-emoji emoji-id="6088947806662303266">🚫</tg-emoji></b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b><i>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.</i></b>"""

    THIRDT_VERIFICATION_TEXT = """<i>ʜᴇʏ</i><tg-emoji emoji-id="5247133031235329609">👋</tg-emoji><i> {},</i>

<tg-emoji emoji-id="5397976749436842796">⚡</tg-emoji><i> ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ &amp; ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ</i><tg-emoji emoji-id="6086880518643656697">✅</tg-emoji>
<tg-emoji emoji-id="5397976749436842796">⚡</tg-emoji><i> आप आज सत्यापित नहीं हैं, कृपया सत्यापित करें पर क्लिक करें और अगले सत्यापन तक असीमित उपयोग पाएं</i><tg-emoji emoji-id="6086880518643656697">✅</tg-emoji>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3 <tg-emoji emoji-id="5427181942934088912">💬</tg-emoji>

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji>
अगर आपको डायरेक्ट फाइल्स चाहिए तो आप प्रीमियम सेवा ले सकते हैं (सत्यापन की आवश्यकता नहीं)<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji></blockquote>

<b><tg-emoji emoji-id="6309670561165352554">📹</tg-emoji> Watch tutorials / ट्यूटोरियल देखें <tg-emoji emoji-id="6088947806662303266">🚫</tg-emoji></b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b><i>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3ʀᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</i></b>"""

    VERIFIED_LOG_TEXT = """ᴜꜱᴇʀ ᴠᴇʀɪꜰɪᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ✓

👤 ɴᴀᴍᴇ:- {} [ <code>{}</code> ]

📆 ᴅᴀᴛᴇ:- <code>{} </code>

#Verificaton_{}_Completed"""


    ADMIN_CMD = """ʜᴇʏ 👋,

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊

• /start - <code>ᴛᴏ ᴜꜱᴇ ᴍʏ ꜰᴇᴀᴛᴜʀᴇꜱ.</code>
• /stats - <code>ɢᴇᴛ ᴛʜᴇ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ ᴀɴᴅ ᴄʜᴀᴛꜱ.</code>
• /del_msg - <code>ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...</code>
• /movie_update - <code>ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code> 
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /verify - <code>ᴛᴜʀɴ ᴏɴ / ᴏꜰꜰ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ (ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ)</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>
• /maintenance - <code>ᴛᴜʀɴ ᴏɴ / ᴏꜰꜰ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ."""

    GROUP_CMD = """ʜᴇʏ 👋,
📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍɪᴢᴇᴅ ɢʀᴏᴜᴘꜱ ⇊

• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""
    

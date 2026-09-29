import telebot, os, yt_dlp
TOKEN = "8902087087:AAEJQWW_66FVhSIUkQVcKeEyMP64rOKD_s0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, "Salom! Men YouTube, Instagram va TikTokdan musiqa yuklovchi botman.\nMenga qoʻshiq nomini yozing yoki video havolasini (silka) yuboring!")

@bot.message_handler(func=lambda m: True)
def download_media(m):
    try:
        text = m.text.strip()
        search_query = text if "http" in text else f"ytsearch:{text}"
        ydl_opts = {"format": "bestaudio/best", "outtmpl": "music.%(ext)s", "noplaylist": True, "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([search_query])
        with open("music.mp3", "rb") as audio: bot.send_audio(m.chat.id, audio, caption="🎵 @UzMusicPlayerBot orqali yuklandi")
        if os.path.exists("music.mp3"): os.remove("music.mp3")
    except Exception as e:
        if os.path.exists("music.mp3"): os.remove("music.mp3")
bot.infinity_polling()

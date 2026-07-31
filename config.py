import os
from dotenv import load_dotenv

load_dotenv()

# توکن ربات تلگرام
BOT_TOKEN = os.getenv("BOT_TOKEN")


# آیدی عددی ادمین‌ها
ADMIN_IDS = [
    int(os.getenv("ADMIN_ID", 0))
]


# کانال عضویت اجباری
CHANNELS = [
    "@RoXeT_VpN"
]


# تنظیمات پنل پاسارگاد
PASARGAD_URL = os.getenv(
    "PASARGAD_URL",
    ""
)

PASARGAD_TOKEN = os.getenv(
    "PASARGAD_TOKEN",
    ""
)


# تنظیمات ربات
BOT_NAME = "MirzaBot"

VERSION = "1.0"

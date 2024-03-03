import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12323023")

API_HASH = os.environ.get("API_HASH", "26f4cc59ffcc290ef279958b49ea37ed")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7137889955:AAG0rWTqxrZkze_I8P9g7X7rfuSGCr7X0ms") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/Team_TRL") 

DB_NAME = os.environ.get("DB_NAME","TELEGRAM FILES")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://gokul2007kannan:<zhx6zZf6wldvdCFY>@cluster0.qos2zcj.mongodb.net/")
 
FLOOD = int(os.environ.get("FLOOD", "1"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/5f5d06dca1f0acf3603ad.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5326845651').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))

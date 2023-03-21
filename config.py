import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20244111")

API_HASH = os.environ.get("API_HASH", "b76d27da2a4220fe109fe9ef0e866530")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6132728857:AAHX16VnWQl1fqto91_7M4H8eQ6IxCkI9cs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "https://t.me/xadmin_bots") 

DB_NAME = os.environ.get("DB_NAME","TELEGRAM FILES")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://kfakeid9:Jobijobi1@musicdb.urlvere.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/aa1faf8dafa22f4a9ce48.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5572938538').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))

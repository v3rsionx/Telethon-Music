import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29405343"))
    API_HASH = os.environ.get("API_HASH", "21cf17b612d3e12d02a8af0bef657759")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6615032399:AAHq72xQJ88yfzH_ssD723QOwd0dkpu7x8o")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQHAsJ8ASe7yaxsyKyX33y4zsDmNylwOoqOy_AeCh0fDfnb_96YQKx8WvKJ6kwZjhOapnx4hyevIYATDpeGzObkIISJ2GXbmFng91o3jyGsO69zlYT0QN6QvG8I3bd2oA7gHz3bpm4W3T_2HaqjEz_UohcuMH4kClixFIYqE67cfIDFdF9j80x3G_1MOCun-bOEVgIY6KBtM3csTEMxiQ6fbiQWa8x4CkjD7qcGuvPqKrjrglxnkKA0y7sH7V1FGg9LgkLUhw4-lZjz5C8-9NS6rKwbtflaC-NggR7krbK6cjvz_klvuFheQjIkS6yWaskURPt5-ODtUtJq1-RobwV8EC9NB1gAAAAFavRptAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "teamxfire_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
